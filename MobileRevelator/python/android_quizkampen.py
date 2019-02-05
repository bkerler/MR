#Pluginname="Quizkampen (Android)"
#Filename="quizkampen"
#Type=App

import struct
import xml.etree.ElementTree
import tempfile

def convertdata(db):
    #ctx.gui_clearData()
    ctx.gui_setMainLabel("Quizkampen: Extracting userid");
    tmpdir = tempfile.mkdtemp()
    outuid = os.path.join(tmpdir, "userid")
    uid=""
    filenames=["/data/se.feomedia.quizkampen.pl.lite/shared_prefs/PREF_SETTINGS_NAME.xml","/se.feomedia.quizkampen.pl.lite/shared_prefs/PREF_SETTINGS_NAME.xml"]
    for f in filenames:
        if ctx.fs_file_extract(f,outuid):
          ctx.gui_add_report_relevant_file(f)
          e = xml.etree.ElementTree.parse(outuid).getroot()
          for atype in e.findall("long"):
            if atype.get("name")=="current_user":
               uid=atype.get("value")
               print("Userid: "+uid+"\n")
          os.remove(outuid)
          break;

    ctx.gui_setMainLabel("Quizkampen: Extracting users");
    waconn=ctx.sqlite_run_cmd(db,"SELECT DISTINCT id, name from qk_users;")
    if (waconn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    contacts={}
    if waconn!=-1:
      rows=ctx.sqlite_get_data_size(waconn)[0]
      for i in range(0,rows):
          id=str(ctx.sqlite_get_data(waconn,i,0))
          name=str(ctx.sqlite_get_data(waconn,i,1))
          if (id not in contacts):
             if name != None:
                contacts[id]=name
             else:
                contacts[id]=""

    #print(contacts)
    ctx.gui_setMainLabel("Quizkampen: Extracting messages");
    ctx.sqlite_cmd_close(waconn)
    conn=ctx.sqlite_run_cmd(db,"select rowid, to_id, from_id, text, datetime, is_message_read, is_deleted from qk_messages;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    
    oldpos=0
    r=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        rowid=ctx.sqlite_get_data(conn,i,0)
        to_id=str(ctx.sqlite_get_data(conn,i,1))
        to_id_alias=""
        if to_id in contacts:
           to_id_alias=contacts[to_id]
        from_id=str(ctx.sqlite_get_data(conn,i,2))
        from_id_alias=""
        if from_id in contacts:
           from_id_alias=contacts[from_id]
        text=ctx.sqlite_get_data(conn,i,3)
        timestamp=ctx.sqlite_get_data(conn,i,4)
        timestamp=str(timestamp[:-3])
        is_message_read=ctx.sqlite_get_data(conn,i,5)
        is_deleted=ctx.sqlite_get_data(conn,i,6)
        
        ctx.gui_set_data(r,0,rowid)
        ctx.gui_set_data(r,1,to_id)
        ctx.gui_set_data(r,2,to_id_alias)
        ctx.gui_set_data(r,3,from_id)
        ctx.gui_set_data(r,4,from_id_alias)
        ctx.gui_set_data(r,5,text)
        
        print(timestamp)
        ctx.gui_set_data(r,6,timestamp)
        ctx.gui_set_data(r,7,is_message_read)
        ctx.gui_set_data(r,8,is_deleted)
        if (uid==from_id):
            from_me="yes"
        else:
            from_me="no"
        if (uid==""):
            from_me="unknown"
        ctx.gui_set_data(r,9,from_me)
        r+=1
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","to_id (QString)", "to_id_alias (QString)", "from_id (QString)", "from_id_alias (QString)", "text (QString)","timestamp (int)","is_message_read (QString)","is_deleted (QString)", "is_from_me (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Quizkampen: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."