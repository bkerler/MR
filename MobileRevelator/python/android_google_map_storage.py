#Pluginname="Google Maps Storage (Android)"
#Filename="gmm_storage.db"
#Type=App

import struct
import datetime

def extractcoordinate(data):
    m=""
    for s in data:
        if s.isdigit() or s=='.':
            m+=s
    return m

def convertdata(db):
    #ctx.gui_clearData()
    conn=ctx.sqlite_run_cmd(db,"select rowid, _data from gmm_storage_table;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    if rows==0:
        return
    oldpos=0
    z=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        data=ctx.sqlite_get_data(conn,i,1).data()
        idx=data.find(b"/dir/")
        if (idx!=-1):
            length=struct.unpack("<B",data[idx-2:idx-1])[0]
            directions=data[idx:idx+length]
            fromlat=""
            fromlon=""
            tolon=""
            tolat=""
            try:
                directions=directions.decode()
            except:
                directions=str(directions)
            fromlat=directions.split("/dir/")[1].split(",")[0]
            fromlon=directions.split(",")[1].split("/")[0]
            endidx=directions.rfind("!1d")
            dd=directions[endidx:]
            if (dd!=-1):
                if len(dd.split("!1d"))>1 and len(dd.split("!2d"))>1:
                    tolat=dd.split("!1d")[1].split("!")[0]
                    tolon=dd.split("!2d")[1].split("!")[0]
            #print(directions)
            timestamp=0
            idx=data.find(b"\x4C\x00\x01\x67\x74\x00\x12\x4C\x6A\x61\x76\x61\x2F\x6C\x61\x6E\x67\x2F\x53\x74\x72\x69\x6E\x67\x3B\x78\x70")
            if (idx!=-1):
                timestamp=struct.unpack(">Q",data[idx+0x1B:idx+0x1B+8])[0]
            ctx.gui_set_data(z,0,id)
            ctx.gui_set_data(z,1,str(timestamp))
            ctx.gui_set_data(z,2,"https://google.com/maps"+directions)
            
            fromlat=extractcoordinate(fromlat)
            fromlon=extractcoordinate(fromlon)
            tolat=extractcoordinate(tolat)
            tolon=extractcoordinate(tolon)
            ctx.gui_set_data(z,3,fromlat)
            ctx.gui_set_data(z,4,fromlon)
            ctx.gui_set_data(z,5,tolat)
            ctx.gui_set_data(z,6,tolon)
            z+=1
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","timestamp (QString)","url (QString)","fromlat (float)","fromlon (float)","tolat (float)","tolon (float)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Google Maps Storage: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."