#Pluginname="DB Navigator (Android)"
#Filename="hafas_android.db"
# - added DB Navigator Hafas (18.04.2016)
#Type=App

import struct

def converttimecolumn(dateidx,db):
    for i in range(0,ctx.gui_data_size()[0]):
        if (ctx.gui_get_data(i,dateidx))!=None:
            val=int(ctx.gui_get_data(i,dateidx))/1000
        if (val>0):
            conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
            ctx.gui_set_data(i,dateidx,ctx.sqlite_get_data(conn,0,0))
            ctx.sqlite_cmd_close(conn)

def convertdata(db):
    #ctx.gui_clearData()
    conn=ctx.sqlite_run_cmd(db,"SELECT _id, data from favoritenlist_reqp;")
    if (conn==-1):
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
        dataitems=ctx.sqlite_get_data(conn,i,1).data()
        datastr=dataitems.splitlines()
        try:
           startLocationName=datastr[0].decode('utf-8')
           targetLocationName=datastr[1].decode('utf-8')
        except:
           startLocationName=datastr[0].decode('latin1')
           targetLocationName=datastr[1].decode('latin1')
        for x in range(len(datastr)):
           if "requestTime" in str(datastr[x]):
              requestTime=str(datastr[x]).split("=")[1][:-1]
              break
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,startLocationName)
        ctx.gui_set_data(i,2,targetLocationName)
        ctx.gui_set_data(i,3,requestTime)


def main():
    headers=["_id (int)","startLocationName (QString)","targetLocationName (QString)","requestTime (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("DB Navigator: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_setMainLabel("DB Navigator: Converting timestamp")
    converttimecolumn(3,db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."