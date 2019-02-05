#Pluginname="Google Mail (Android)"
#Filename="mailstore."
#Type=App

import struct
import zlib
import unhtml

def convertdata(db):
    #ctx.gui_clearData()
    conn=ctx.sqlite_run_cmd(db,"select rowid, fromAddress, toAddresses, subject, body, bodyCompressed, datetime(dateSentMs/1000,'unixepoch','localtime'), joinedAttachmentInfos from messages;")
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
        bodycompressed=ctx.sqlite_get_data(conn,i,5)
        time=ctx.sqlite_get_data(conn,i,6)
        attachments=ctx.sqlite_get_data(conn,i,7)
        try:
            bodycompressed=bodycompressed.data()
        except:
            bodycompressed=bodycompressed
        bodydehtml=""
        if len(bodycompressed)>0:
            bodyhtml = zlib.decompress(bodycompressed).decode('UTF-8')
            bodydehtml = unhtml.html_to_text(bodyhtml)

        #print(str(id)+";"+bodydehtml+";"+body)
        sbody=''
        if (body==''):
          sbody=bodydehtml
        else:
          sbody=body
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,fromaddr)
        ctx.gui_set_data(i,2,toaddr)
        ctx.gui_set_data(i,3,subject)
        ctx.gui_set_data(i,4,sbody)
        ctx.gui_set_data(i,5,time)
        ctx.gui_set_data(i,6,attachments)
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","fromAddress (QString)","toAddresses (QString)","subject (QString)","body (QString)","dateSentMs (int)","Attachments (QString)"]
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