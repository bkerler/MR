#Pluginname="Android Chrome Sync Data (Android)"
#Filename="SyncData.sqlite3"
#Type=App

import struct
from PythonQt import QtCore

def getlen(buf,pos):
        shift=0
        while (shift<64):
            b = int.from_bytes(buf[pos:pos+1],byteorder='little')
            pos+=1
            if (b & 0x80)==0:
                return pos
            shift+=7
        return pos

def getdata(buf,pos):
        result=0
        shift=0
        while (shift<64):
            b = int.from_bytes(buf[pos:pos+1],byteorder='little')
            pos+=1
            result |= (b & 0x7F) << shift
            if (b & 0x80)==0:
                return result
            shift+=7
        return result

def convertdata(db):
    #ctx.gui_clearData()
    conn=ctx.sqlite_run_cmd(db,"select rowid, mtime, non_unique_name, server_non_unique_name, specifics from metas;")
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
        mtime=ctx.sqlite_get_data(conn,i,1)
        non_unique_name=ctx.sqlite_get_data(conn,i,2)
        server_non_unique_name=ctx.sqlite_get_data(conn,i,3)
        title=""
        if (non_unique_name==server_non_unique_name):
            title=non_unique_name
        else:
            title=non_unique_name+" ["+server_non_unique_name+"]"
        rawdata=ctx.sqlite_get_data(conn,i,4)
        data=QtCore.QByteArray(rawdata)
        if (mtime==0):
            continue
        if (title==""):
            continue
        if (data.length()<8):
            continue
        buf=data.data()
        a=getlen(buf,0)
        b=getlen(buf,a)
        c=getlen(buf,b)
        urllen=getdata(buf,c)
        urlpos=getlen(buf,c)
        length=bytearray(data.data())[urlpos]
        info=data.data()[urlpos:urlpos+urllen]
        url=""
        if "http" in str(info):
            url=info.decode()
        elif "session_sync" in str(info):
            urlpos=urlpos+urllen+0x10
            urlpos=getlen(buf,urlpos)
            urlpos=getlen(buf,urlpos)
            urllen=getdata(buf,urlpos)
            urlpos=getlen(buf,urlpos)
            try:
                url=data.data()[urlpos:urlpos+urllen].decode()
            except:
                try:
                    dat=bytes(data.data()[urlpos-1:urlpos+urllen])
                    dats=dat[0:8+str(dat[9:]).find("/")]
                    url=dats.decode()
                except:
                    url=str(data.data()[urlpos:urlpos+urllen])
        else:
            url=""
        if url=="":
            continue
        ctx.gui_set_data(t,0,id)
        ctx.gui_set_data(t,1,title)
        ctx.gui_set_data(t,2,url)
        ctx.gui_set_data(t,3,mtime)
        t+=1
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","title (QString)","url (QString)","timestamp (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Google Chrome SyncData: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."