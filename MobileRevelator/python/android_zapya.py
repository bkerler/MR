#Pluginname="Zapya (Android)"
#Filename="emmsg.db"
#Type=App

import struct
import json
import tempfile
import shutil

def converttime(val,db):
    conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
    res=ctx.sqlite_get_data(conn,0,0)
    ctx.sqlite_cmd_close(conn)
    return res

def extractuserdatabase():
    ctx.gui_setMainLabel("Status: Trying to attach im_user database")
    result={}
    for datadir in ["/data/com.dewmobile.kuaiya.play/databases/im_user.db"]:
        if (ctx.fs_isFile(datadir)==True):
            result["USER"]=datadir;
    if (len(result)>0):
        tmpfile=tempfile.gettempdir()+"/im_user.db"
        if (ctx.fs_file_extract(result["USER"],tmpfile)!=-1):
            ctx.gui_add_report_relevant_file(result["USER"])
            return tmpfile
    return ""

def convertcontacts(db):
    ctx.gui_setMainLabel("Status: Converting zapya contacts")
    waconn=ctx.sqlite_run_cmd(db,"SELECT c_uid, c_nk from user.contact;")
    contacts={}
    oldpos=0
    if waconn!=-1:
      rows=ctx.sqlite_get_data_size(waconn)[0]
      for i in range(0,rows):
          newpos=int(i/rows*100)
          if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
          uid=str(ctx.sqlite_get_data(waconn,i,0))
          name=ctx.sqlite_get_data(waconn,i,1)
          if (uid not in contacts) or (contacts[uid]==uid):
             if name != None:
                contacts[uid]=name
    ctx.sqlite_cmd_close(waconn)
    return contacts
    
def convertdata(db,contacts):
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, msgtime, msgdir, msgbody from chat;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    
    oldpos=0
    i2=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        timestamp=str(ctx.sqlite_get_data(conn,i,1))
        msgdir=ctx.sqlite_get_data(conn,i,2)
        data=ctx.sqlite_get_data(conn,i,3)
        
        fromid=""
        toid=""
        msgtxt=""
        msgtype=""
        subinfo=""
        toalias=""
        fromalias=""
        
        jdata=json.loads(data)
        if "from" in jdata:
            fromid=str(jdata["from"])
            if fromid in contacts:
                fromalias=contacts[fromid]
        if "to" in jdata:
            toid=str(jdata["to"])
            if toid in contacts:
                toalias=contacts[toid]
        if "bodies" in jdata:
            bodies=jdata["bodies"][0]
            if "type" in bodies:
                msgtype=bodies["type"]
            if "msg" in bodies:
                msgtxt=bodies["msg"]
                if "z_msg_type" in msgtxt:
                    msgtxt=""

        if "ext" in jdata:
            ext=jdata["ext"]
            if "z_msg_syn_trans_info" in ext:
                info=ext["z_msg_syn_trans_info"]
                if "thumbPath" in info:
                    subinfo+="thumb=\""+info["thumbPath"]+"\";"
                if "currentBytes" in info:
                    subinfo+="currentBytes=\""+str(info["currentBytes"])+"\";"
                if "url" in info:
                    subinfo+="url=\""+info["url"]+"\";"
                if "toDeviceId" in info:
                    subinfo+="toDeviceId=\""+info["toDeviceId"]+"\";"
                if "thumbUrl" in info:
                    subinfo+="thumbUrl=\""+info["thumbUrl"]+"\";"
                if "path" in info:
                    subinfo+="path=\""+info["path"]+"\";"
            if "opener_key" in ext:
                subinfo+="opener_key=\""+ext["opener_key"]+"\";"
            if "opener_file_path" in ext:
                subinfo+="opener_file_path=\""+ext["opener_file_path"]+"\";"
            if "file_title" in ext:
                subinfo+="file_title=\""+ext["file_title"]+"\";"
            if "sender_thumbnail" in ext:
                subinfo+="sender_thumbnail=\""+ext["sender_thumbnail"]+"\";"
                
                    
        ctx.gui_set_data(i2,0,id)
        ctx.gui_set_data(i2,1,timestamp)
        ctx.gui_set_data(i2,2,fromid)
        ctx.gui_set_data(i2,3,fromalias)
        ctx.gui_set_data(i2,4,toid)
        ctx.gui_set_data(i2,5,toalias)
        ctx.gui_set_data(i2,6,msgdir)
        ctx.gui_set_data(i2,7,msgtype)
        ctx.gui_set_data(i2,8,msgtxt)
        ctx.gui_set_data(i2,9,subinfo)
        i2+=1

def main():
    headers=["rowid (int)","timestamp (int)","from (QString)","fromalias (QString)","to (QString)","toalias (QString)", "msgdir (int)", "msgtype (QString)","msgtxt (QString)","description (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Zapya: Parsing data");
    ctx.gui_setMainProgressBar(0)
    tmpfilename=extractuserdatabase()
    db=ctx.sqlite_open("gui",True)
    tmpconn=0
    if (tmpfilename!=""):
        tmpconn=ctx.sqlite_run_cmd(db,"attach database \""+tmpfilename+"\" as user;")
    contacts=convertcontacts(db)
    if (tmpfilename!=""):
        tmpconn=ctx.sqlite_run_cmd(db,"detach database \""+tmpfilename+"\" as user;")

    contacts=convertcontacts(db)
    convertdata(db,contacts)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    if (tmpconn!=0):
        try:
            os.remove(tmpfilename)
        except:
            tmpfilename=""
    return "Finished running plugin."