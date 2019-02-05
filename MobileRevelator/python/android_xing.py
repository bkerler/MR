#Pluginname="Xing (Android)"
#Filename="conversations.db"
#Type=App

import struct

def convertdata(db):
    #ctx.gui_clearData()
    waconn=ctx.sqlite_run_cmd(db,"SELECT _id, im_skype, company_name, bussiness_province, birthdate, display_name, page_name, bussiness_city, occupation_title from users.users_table;")
    if (waconn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    contacts={}
    if waconn!=-1:
      rows=ctx.sqlite_get_data_size(waconn)[0]
      for i in range(0,rows):
          id=str(ctx.sqlite_get_data(waconn,i,0))
          skype=str(ctx.sqlite_get_data(waconn,i,1))
          company_name=str(ctx.sqlite_get_data(waconn,i,2))
          bussiness_province=str(ctx.sqlite_get_data(waconn,i,3))
          birthdate=str(ctx.sqlite_get_data(waconn,i,4))
          display_name=str(ctx.sqlite_get_data(waconn,i,5))
          page_name=str(ctx.sqlite_get_data(waconn,i,6))
          bussiness_city=str(ctx.sqlite_get_data(waconn,i,7))
          occupation_title=str(ctx.sqlite_get_data(waconn,i,8))
          if (id not in contacts) or (contacts[id]==id):
             if display_name != None:
                contacts[id]=display_name
             elif page_name != None:
                contacts[id]=page_name
             else:
                contacts[id]=id

    attconn=ctx.sqlite_run_cmd(db,"select msg_id, file_name from attachments_table;")
    attachments={}
    if attconn!=-1:
      attrows=ctx.sqlite_get_data_size(attconn)[0]
      for i in range(0,attrows):
          id=str(ctx.sqlite_get_data(attconn,i,0))
          filename=str(ctx.sqlite_get_data(attconn,i,1))
          if (id not in attachments):
                attachments[id]=filename
          else:
                attachments[id]+=";"+filename

    conn=ctx.sqlite_run_cmd(db,"select messages_table.rowid, date, _id, body, sender, has_attachments from messages_table;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    
    oldpos=0
    r=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        rowid=ctx.sqlite_get_data(conn,i,0)
        timestamp=ctx.sqlite_get_data(conn,i,1)
        id=ctx.sqlite_get_data(conn,i,2)
        body=ctx.sqlite_get_data(conn,i,3)
        sender_id=ctx.sqlite_get_data(conn,i,4)
        has_attachments=ctx.sqlite_get_data(conn,i,5)
        
        name=""
        sender_name=""
        attaches=""
        if id in attachments:
           attaches=attachments[id]
        if sender_id in contacts:
           sender_name=contacts[sender_id]
        ctx.gui_set_data(r,0,rowid)
        ctx.gui_set_data(r,1,timestamp)
        ctx.gui_set_data(r,2,sender_id)
        ctx.gui_set_data(r,3,sender_name)
        ctx.gui_set_data(r,4,body)
        ctx.gui_set_data(r,5,attaches)
        r+=1
    ctx.sqlite_cmd_close(attconn)
    ctx.sqlite_cmd_close(waconn)
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","timestamp (int)","_sender (QString)","_sender_alias (QString)","body (QString)","Attachments (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Xing: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."