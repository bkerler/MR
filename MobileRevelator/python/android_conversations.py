#Pluginname="Conversations Messenger (Android)"
#Filename="history"
#Type=App

import struct
import sys
from Library import thumbnail
from PythonQt import QtCore

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select fingerprint, name, last_activation from identities;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    oldpos=0
    fingerprint={}
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        fingerprint[str(ctx.sqlite_get_data(conn,i,0))]=[str(ctx.sqlite_get_data(conn,i,1)),str(ctx.sqlite_get_data(conn,i,2))]

    conn=ctx.sqlite_run_cmd(db,"select messages.rowid, messages.axolotl_fingerprint, messages.counterpart, messages.timeSent, messages.body, messages.type, messages.relativeFilePath,  messages.remoteMsgId from messages;")
    if conn==-1:
        print ("Error: "+ctx.sqlite_last_error(db))
        return
    rows=ctx.sqlite_get_data_size(conn)[0]
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        axofingerprint=ctx.sqlite_get_data(conn,i,1)
        contact_alias=""
        if axofingerprint in fingerprint:
            contact_alias=fingerprint[axofingerprint][0]
        counterpart=ctx.sqlite_get_data(conn,i,2)
        timestamp=ctx.sqlite_get_data(conn,i,3)
        body=ctx.sqlite_get_data(conn,i,4)
        type=str(ctx.sqlite_get_data(conn,i,5))
        if (type=="0"):
            type="Message"
        elif (type=="2"):
            type="Image"
        relativeFilePath=ctx.sqlite_get_data(conn,i,6)
        remoteMsgId=ctx.sqlite_get_data(conn,i,7)
        direction=""
        if remoteMsgId=="":
            direction="Received"
        else:
            direction="Sent"
            contact_alias=counterpart
        
        image=QtCore.QByteArray(bytes(b''))
        if (relativeFilePath!=""):
            imagename="/media/0/Conversations/Media/Conversations Images/"+relativeFilePath
            res=thumbnail.generate(ctx,imagename)
            if (res!=-1):
                image=QtCore.QByteArray(bytes(res[1]))
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,type)
        ctx.gui_set_data(i,2,axofingerprint)
        ctx.gui_set_data(i,3,contact_alias)
        ctx.gui_set_data(i,4,timestamp)
        ctx.gui_set_data(i,5,direction)
        ctx.gui_set_data(i,6,body)
        ctx.gui_set_data(i,7,image)
        ctx.gui_set_data(i,8,relativeFilePath)
        
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","type (QString)","contact (QString)","contact_alias (QString)","timestamp (int)","direction (QString)","body (QString)","image (QByteArray)","relativeFilePath (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Conversations Messenger: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."