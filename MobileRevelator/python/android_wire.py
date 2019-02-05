#Pluginname="Wire (Android)"
#Filename="/"
#Type=App

import struct
import tempfile
import json

def convertdata(db,rowids):
    contacts={}
    ctx.gui_setMainLabel("Wire: Preparing contacts");
    contact=ctx.sqlite_run_cmd(db,"select _id, name, email, phone from Users;")
    rows=ctx.sqlite_get_data_size(contact)[0]
    oldpos=0
    r=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(contact,i,0)
        if id not in contacts:
            name=ctx.sqlite_get_data(contact,i,1)
            email=ctx.sqlite_get_data(contact,i,2)
            phone=ctx.sqlite_get_data(contact,i,3)
            cdata={}
            cdata[0]=name
            cdata[1]=email
            cdata[2]=phone
            contacts[id]=cdata
    ctx.sqlite_cmd_close(contact)
    
    ctx.gui_setMainLabel("Wire: Parsing Messages");
    conn=ctx.sqlite_run_cmd(db,"select rowid, conv_id, msg_type, user_id, content, time, members, recipient, email, name, msg_state, expiry_time, expired from Messages;")
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
            conv_id=ctx.sqlite_get_data(conn,i,1)
            msg_type=ctx.sqlite_get_data(conn,i,2)
            user_id=ctx.sqlite_get_data(conn,i,3)
            content=ctx.sqlite_get_data(conn,i,4)
            try:
                ct=json.loads(content)[0]
                print(ct)
                if "content" in ct:
                    content=ct["content"]
            except:
                content=content
            time=ctx.sqlite_get_data(conn,i,5)
            members=ctx.sqlite_get_data(conn,i,6)
            recipient=ctx.sqlite_get_data(conn,i,7)
            email=ctx.sqlite_get_data(conn,i,8)
            name=ctx.sqlite_get_data(conn,i,9)
            msg_state=ctx.sqlite_get_data(conn,i,10)
            expiry_time=ctx.sqlite_get_data(conn,i,11)
            expired=ctx.sqlite_get_data(conn,i,12)

            
            ctx.gui_set_data(r,0,id)
            ctx.gui_set_data(r,1,time)
            ctx.gui_set_data(r,2,user_id)
            
            alias=""
            if user_id in contacts:
               alias=contacts[user_id][0]+";"+contacts[user_id][1]+";"+contacts[user_id][2] 
            ctx.gui_set_data(r,3,alias)
            ctx.gui_set_data(r,4,name)
            if members in contacts:
               members=contacts[members][0]+";"+contacts[members][1]+";"+contacts[members][2] 
            ctx.gui_set_data(r,5,members)
            if recipient in contacts:
               recipient=contacts[recipient][0]+";"+contacts[recipient][1]+";"+contacts[recipient][2]
            ctx.gui_set_data(r,6,recipient)

            ctx.gui_set_data(r,7,email)
            ctx.gui_set_data(r,8,conv_id)
            ctx.gui_set_data(r,9,msg_type)
            ctx.gui_set_data(r,10,msg_state)
            ctx.gui_set_data(r,11,content)
            ctx.gui_set_data(r,12,expiry_time)
            r+=1
    ctx.sqlite_cmd_close(conn)
    return rowids
    
def main():
    headers=["rowid (int)","time (int)","user_id (QString)","alias (QString)","name (QString)","members (QString)","recipient (QString)","email (QString)","conv_id (QString)","msg_type (QString)","msg_state (QString)","content (QString)","expiry_time (QString)","expired (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Wire: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    rowids=[]
    convertdata(db,rowids)
    ctx.sqlite_close(db)
    
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."