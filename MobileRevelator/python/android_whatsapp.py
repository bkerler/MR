#Pluginname="WhatsApp (Android)"
#Filename="msgstore.db"
#Type=App

import struct
import tempfile
import shutil

def extractwadatabase():
    ctx.gui_setMainLabel("Status: Trying to attach wa database")
    result={}
    for datadir in ["/data/com.whatsapp/databases/wa.db","/com.whatsapp/databases/wa.db","/data/user/150/com.whatsapp/databases/wa.db"]:
        if (ctx.fs_isFile(datadir)==True):
            result["WA"]=datadir;
    if (len(result)>0):
        tmpfile=tempfile.gettempdir()+"/wa.db"
        if (ctx.fs_file_extract(result["WA"],tmpfile)!=-1):
            return tmpfile
    return ""

def convertdata(db,contacts,rowids,subtype,filename):
    conn=ctx.sqlite_run_cmd(db,"SELECT messages.rowid, messages.timestamp, messages.key_remote_jid, messages.remote_resource, messages.key_from_me, messages.data, messages.media_url, messages.media_duration, messages.media_caption, message_thumbnails.thumbnail, messages.raw_data, messages.participant_hash, messages.media_name FROM messages OUTER LEFT JOIN message_thumbnails ON message_thumbnails.key_id=messages.key_id;")
    if (conn==-1):
        conn=ctx.sqlite_run_cmd(db,"SELECT messages.rowid, timestamp, key_remote_jid, remote_resource, key_from_me, data, media_url, media_duration, media_caption, '', raw_data, participant_hash, media_name FROM messages;")
        if (conn==-1):
            conn=ctx.sqlite_run_cmd(db,"SELECT messages.rowid, timestamp, key_remote_jid, remote_resource, key_from_me, data, media_url, media_duration, '', '', raw_data, '', media_name FROM messages;")
            if (conn==-1):
                print ("Error: "+ctx.sqlite_last_error(db))
                return rowids
    rows=ctx.sqlite_get_data_size(conn)[0]
    oldpos=0
    r=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        if id not in rowids:
            rowids.append(id)
            timestamp=ctx.sqlite_get_data(conn,i,1)
            key_remote_jid=ctx.sqlite_get_data(conn,i,2)
            if key_remote_jid=="-1":
               continue
            remote_resource=ctx.sqlite_get_data(conn,i,3)
            key_from_me=ctx.sqlite_get_data(conn,i,4)
            data=ctx.sqlite_get_data(conn,i,5) 
            media_url=ctx.sqlite_get_data(conn,i,6)
            media_duration=ctx.sqlite_get_data(conn,i,7)
            media_caption=ctx.sqlite_get_data(conn,i,8)
            raw_data=ctx.sqlite_get_data(conn,i,9)
            if (raw_data=="") or (raw_data is None):
                raw_data=ctx.sqlite_get_data(conn,i,10) 
            participant_hash=ctx.sqlite_get_data(conn,i,11)
            media_name=ctx.sqlite_get_data(conn,i,12)
            type=""
            if participant_hash != "":
               type="Group"

            name=""
            if key_remote_jid in contacts:
               name=contacts[key_remote_jid]

            ctx.gui_set_data(r,0,id)
            ctx.gui_set_data(r,1,timestamp)
            if type=="Group":
              ctx.gui_set_data(r,2,remote_resource)
            else:
              ctx.gui_set_data(r,2,key_remote_jid)
            ctx.gui_set_data(r,3,name)
            if type=="Group":
              ctx.gui_set_data(r,4,key_remote_jid)
            else:
              ctx.gui_set_data(r,4,remote_resource)
            ctx.gui_set_data(r,5,key_from_me)
            ctx.gui_set_data(r,6,data)
            if (media_name!="" and media_url!=""):
                media_name=media_name+":"+media_url
            elif (media_url!=""):
                media_name=media_url
            ctx.gui_set_data(r,7,media_name)
            ctx.gui_set_data(r,8,media_duration)
            ctx.gui_set_data(r,9,media_caption)
            ctx.gui_set_data(r,10,raw_data)
            ctx.gui_set_data(r,11,type)
            ctx.gui_set_data(r,12,subtype)
            ctx.gui_set_data(r,13,filename)
            r+=1
    ctx.sqlite_cmd_close(conn)
    return rowids

def convertcontacts(db):
    #ctx.gui_clearData()
    ctx.gui_setMainLabel("Status: Converting whatsapp contacts")
    waconn=ctx.sqlite_run_cmd(db,"SELECT jid, wa_name, display_name from wa.wa_contacts;")
    contacts={}
    oldpos=0
    if waconn!=-1:
      rows=ctx.sqlite_get_data_size(waconn)[0]
      for i in range(0,rows):
          newpos=int(i/rows*100)
          if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
          jid=str(ctx.sqlite_get_data(waconn,i,0))
          wa_name=ctx.sqlite_get_data(waconn,i,1)
          display_name=ctx.sqlite_get_data(waconn,i,2)
          if (jid not in contacts) or (contacts[jid]==jid):
             if wa_name != None:
                contacts[jid]=wa_name
             elif display_name != None:
                contacts[jid]=display_name
             else:
                contacts[jid]=jid

    ctx.sqlite_cmd_close(waconn)
    return contacts

def findbackups():
    files=[]
    allfiles=ctx.fs_filelist()
    filecount=len(allfiles)
    for file in allfiles:
        if ("WhatsApp/Databases/msgstore" in file) and (".crypt" in file):
            files.append(file)
    return files

def main():
    headers=["rowid (int)","timestamp (int)","key_remote_jid (QString)","alias (QString)","group_id (QString)","key_from_me (QString)","data (QString)","media_name_url (QString)","media_duration (QString)","media_caption (QString)","raw_data (QByteArray)","type (QString)","deleted (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("WhatsApp: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    tmpfilename=extractwadatabase()
    db=ctx.sqlite_open("gui",True)
    tmpconn=0
    if (tmpfilename!=""):
        tmpconn=ctx.sqlite_run_cmd(db,"attach database \""+tmpfilename+"\" as wa;")
    contacts=convertcontacts(db)
    if (tmpfilename!=""):
        tmpconn=ctx.sqlite_run_cmd(db,"detach database \""+tmpfilename+"\" as wa;")
    rowids=[]
    ctx.gui_setMainLabel("Status: Converting whatsapp msgstore.db")
    convertdata(db,contacts,rowids,0,ctx.sqlite_get_filename("gui"))
    ctx.sqlite_close(db)
    
    #Searching for backup data
    backupfiles=findbackups()
    ctx.gui_setMainLabel("WhatsApp: Extracting key");
    tmpdir = tempfile.mkdtemp()
    outkey = os.path.join(tmpdir, "key")
    error=""
    if (len(backupfiles)>0):
        import whatsapp_decrypt
        keyfiles=[]
        for kf in ["/data/com.whatsapp/files/key","/data/user/150/com.whatsapp/files/key"]:
            if ctx.fs_file_extract(kf, outkey):
                keyfiles.append(kf)
        for keyfile in keyfiles:
            ctx.gui_add_report_relevant_file(keyfile)
            for cryptfile in backupfiles:
                fname=cryptfile[cryptfile.rfind("/")+1:]
                outdb = os.path.join(tmpdir,fname)
                if ctx.fs_file_extract(cryptfile,outdb):
                    ret=whatsapp_decrypt.decryptwhatsapp(outdb,outdb+".dec",outkey)
                    if (ret==""):
                        continue
                    ctx.gui_setMainLabel("Status: Converting whatsapp backup: "+fname)
                    db=ctx.sqlite_open(outdb+".dec",True)
                    convertdata(db,contacts,rowids,1,cryptfile)
                    ctx.sqlite_close(db)
                else:
                     continue
    
    shutil.rmtree(tmpdir)
      
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    if (tmpconn!=0):
        try:
            os.remove(tmpfilename)
        except:
            tmpfilename=""
    return "Finished running plugin."