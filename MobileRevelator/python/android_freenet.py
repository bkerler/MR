#Pluginname="Freenet Mail (Android)"
#Filename="mail.db"
#Type=App

import struct
import zlib
import unhtml
import json

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select mail.id, mail.[from], mail.[to], mail.subject, mail_body.html, mail_body.plain, mail.received_date, mail.folder_id, mail.has_attachment, attachment.name from mail, mail_body LEFT OUTER JOIN attachment ON attachment.mail == mail._id where mail.id == mail_body._id;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    if rows==0:
        return
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        fromaddr=ctx.sqlite_get_data(conn,i,1)
        toaddr=ctx.sqlite_get_data(conn,i,2)
        subject=ctx.sqlite_get_data(conn,i,3)
        body=unhtml.html_to_text(ctx.sqlite_get_data(conn,i,4))
        bodyhtml=ctx.sqlite_get_data(conn,i,5)
        time=ctx.sqlite_get_data(conn,i,6)
        folder=ctx.sqlite_get_data(conn,i,7)
        has_attachment=ctx.sqlite_get_data(conn,i,8)
        attachments=ctx.sqlite_get_data(conn,i,9)
        try:
            bodyhtml=bodyhtml.data()
        except:
            bodyhtml=bodyhtml
        bodydehtml=""
        if len(bodyhtml)>0:
            bodydehtml = unhtml.html_to_text(bodyhtml)
        sbody=''
        if (body==''):
          sbody=bodydehtml
        else:
          sbody=body
        fromdata=json.loads(fromaddr)
        fromemail=""
        fromalias=""
        if len(fromdata)>0:
            fromdata=fromdata[0]
        if "email" in fromdata:
            fromemail=fromdata["email"]
        if "realname" in fromdata:
            fromalias=fromdata["realname"]    
        todata=json.loads(toaddr)
        toemail=""
        toalias=""
        if len(todata)>0:
            todata=todata[0]
        if "email" in todata:
            toemail=todata["email"]
        if "realname" in todata:
            toalias=todata["realname"]    
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,fromemail)
        ctx.gui_set_data(i,2,fromalias)
        ctx.gui_set_data(i,3,toemail)
        ctx.gui_set_data(i,4,toalias)
        ctx.gui_set_data(i,5,subject)
        ctx.gui_set_data(i,6,sbody)
        ctx.gui_set_data(i,7,time)
        ctx.gui_set_data(i,8,folder)
        ctx.gui_set_data(i,9,attachments)
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","fromAddress (QString)","fromAlias (QString)","toAddresses (QString)","toAlias (QString)","subject (QString)","body (QString)","date (int)","folder (QString)","Attachments (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Google Mail: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."