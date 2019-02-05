#Pluginname="Lieferheld (Android)"
#Filename="apptimize.db"
#Type=App

import struct
import json

def converttime(val,db):
    conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
    res=ctx.sqlite_get_data(conn,0,0)
    ctx.sqlite_cmd_close(conn)
    return res

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, value from entry_store;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    
    oldpos=0
    i2=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        data=ctx.sqlite_get_data(conn,i,1)
        location=""
        timestamp=""
        description=""
        jdata=json.loads(data)
        if "a" in jdata:
            if "&cd15" in jdata["a"]:
                location+=str(jdata["a"]["&cd15"])+" "
            if "&cd16" in jdata["a"]:
                location+=str(jdata["a"]["&cd16"])+" "
            if "&cd17" in jdata["a"]:
                location+=str(jdata["a"]["&cd17"])+" "

            for x in jdata["a"]:
                if ("&pr" in x) and ("nm" in x):
                    description+=str(jdata["a"][x])+";"

        if "bt" in jdata:
             time=int(jdata["bt"])
             timestamp=converttime(time/1000,db)+";"

        if (location!=""):
             ctx.gui_set_data(i2,0,id)
             ctx.gui_set_data(i2,1,timestamp)
             ctx.gui_set_data(i2,2,location)
             ctx.gui_set_data(i2,3,description)
             i2+=1

def main():
    headers=["rowid (int)","timestamp (int)","location (QString)","description (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Lieferheld: Parsing data");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."