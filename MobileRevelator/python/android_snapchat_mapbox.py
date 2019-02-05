#Pluginname="Snapchat (MapBox)"
#Filename="mbgl-offline.db"
#Type=App

import struct
import tempfile
import shutil
from Library import mrtime
from Library import googlecoord
                
def converttiles(db):
    conn2=ctx.sqlite_get_deletedrecords(db,"tiles",True)
    ctx.gui_setMainLabel("Status: Seeking tiles.")
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    delids=[]
    for i in range(0,rows2):
        delids.append(ctx.sqlite_get_data(conn2,i,0))
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, id, z, x, y, accessed from tiles;")
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
        id=int(ctx.sqlite_get_data(conn,i,0))
        if (id in delids):
            deleted=str("1")
        else:
            deleted=str("0")
        z=ctx.sqlite_get_data(conn,i,2)
        x=ctx.sqlite_get_data(conn,i,3)
        y=ctx.sqlite_get_data(conn,i,4)
        timestamp=ctx.sqlite_get_data(conn,i,5)
        coord=googlecoord.getcoord(x,y,z)
        latstr=coord[0]
        lonstr=coord[1]
        
        ctx.gui_set_data(i2,0,str(id))
        ctx.gui_set_data(i2,1,timestamp)
        ctx.gui_set_data(i2,2,latstr)
        ctx.gui_set_data(i2,3,lonstr)
        ctx.gui_set_data(i2,4,str(z))
        ctx.gui_set_data(i2,5,deleted)
        i2+=1

        
def main():
    headers=["rowid (int)","accessed (int)","Latitude (QString)","Longitude (QString)","Zoom Level (int)","Deleted (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Snapchat Map Tiles: Parsing data");
    ctx.gui_setMainProgressBar(0)

    db=ctx.sqlite_open("gui",True)
    converttiles(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."