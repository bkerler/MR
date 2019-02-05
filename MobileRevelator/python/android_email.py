#Pluginname="Android EMail (Android)"
#Filename="EmailProvider.db"
#Type=App

import struct
import zlib
import tempfile

def extractbodydatabase():
    ctx.gui_setMainLabel("Status: Trying to attach email database")
    result={}
    for datadir in ["/data/com.android.email/databases/EmailProviderBody.db","com.android.email/db/EmailProviderBody.db","com.android.email/databases/EmailProviderBody.db"]:
        if (ctx.fs_isFile(datadir)==True):
            result["Body"]=datadir;
    if (len(result)>0):
        tmpfile=tempfile.gettempdir()+"/EmailProviderBody.db"
        if (ctx.fs_file_extract(result["Body"],tmpfile)!=-1):
            return tmpfile
    return ""

def convertdata(db):
    #ctx.gui_clearData()
    conn=ctx.sqlite_run_cmd(db,"select Message.rowid, fromList, toList, subject, body.Body.textContent, body.Body.htmlContent, flagAttachment, datetime(Message.timeStamp/1000,'unixepoch','localtime') from Message LEFT OUTER JOIN body.Body on Message._id=body.Body.messageKey;")
    if (conn==-1):
        conn=ctx.sqlite_run_cmd(db,"select Message.rowid, Message.fromList, toList, subject, '-1', '-1', flagAttachment, datetime(Message.timeStamp/1000,'unixepoch','localtime') from Message;")
    if (conn==-1):
        conn=ctx.sqlite_run_cmd(db,"select Message.rowid, fromList, toList, subject, body.Body.textContent, body.Body.htmlContent, '', datetime(Message.timeStamp/1000,'unixepoch','localtime') from Message LEFT OUTER JOIN body.Body on Message._id=body.Body.messageKey;")
    if (conn==-1):
        conn=ctx.sqlite_run_cmd(db,"select Message.rowid, Message.fromList, toList, subject, '-1', '-1', '', datetime(Message.timeStamp/1000,'unixepoch','localtime') from Message;")
    if (conn==-1):
        conn=ctx.sqlite_run_cmd(db,"select messages.rowid, messages.sender_list, messages.to_list, messages.subject, messages.text_content, messages.html_content, 'Name:' || attachments.name || ';Size:' || attachments.size, datetime(messages.internal_date/1000,'unixepoch','localtime') from messages LEFT OUTER JOIN attachments on messages.id=attachments.message_id;")
    if (conn==-1):
            print ("Error: "+ctx.sqlite_last_error(db))
            return
    rows=ctx.sqlite_get_data_size(conn)[0]
    if rows==0:
        return
    oldpos=0
    t=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        fromaddr=ctx.sqlite_get_data(conn,i,1)
        toaddr=ctx.sqlite_get_data(conn,i,2)
        if len(fromaddr)==0 and len(toaddr)==0:
            continue
        fromaddr=fromaddr.split("\x02")
        toaddr=toaddr.split("\x02")
        subject=ctx.sqlite_get_data(conn,i,3)
        bodytext=ctx.sqlite_get_data(conn,i,4) 
        bodyhtml=ctx.sqlite_get_data(conn,i,5)
        flagAttach=ctx.sqlite_get_data(conn,i,6)
        time=ctx.sqlite_get_data(conn,i,7)
        if (len(bodytext)>0):
            body=ctx.htmltotext(bodytext)
        else:
            body=ctx.htmltotext(bodyhtml)
        ctx.gui_set_data(t,0,id)
        ctx.gui_set_data(t,1,fromaddr[0])
        if (len(fromaddr)>1):
            ctx.gui_set_data(t,2,fromaddr[1])
        else:
            ctx.gui_set_data(t,2,"")
        ctx.gui_set_data(t,3,toaddr[0])
        if (len(toaddr)>1):
            ctx.gui_set_data(t,4,toaddr[1])
        else:
            ctx.gui_set_data(t,4,"")
        ctx.gui_set_data(t,5,subject)
        ctx.gui_set_data(t,6,body)
        ctx.gui_set_data(t,7,flagAttach)
        ctx.gui_set_data(t,8,time)
        t+=1
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","fromList (QString)","fromAlias (QString)","toList (QString)","toAlias (QString)","subject (QString)","body (QString)","flagAttachment (int)","timeStamp (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Google Mail: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    tmpfilename=extractbodydatabase()
    tmpconn=0
    if (tmpfilename!=""):
        tmpconn=ctx.sqlite_run_cmd(db,"attach database \""+tmpfilename+"\" as body;")
    #else:
    #    tmpconn=ctx.sqlite_run_cmd(db,"attach database \"c:/ToDo/com.android.email/databases/EmailProviderBody.db\" as body;")
    convertdata(db)
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