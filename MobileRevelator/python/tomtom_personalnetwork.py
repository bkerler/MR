#Pluginname="PersonalNetwork - Trips (TomTom)"
#Filename="PersonalNetwork.sqlite"
#Type=App

import struct
import tempfile
import shutil
from Library import tomtom
  
def converttrips(db,fsname):
    conn2=ctx.sqlite_get_deletedrecords(db,"Trips",True)
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    delids=[]
    for i in range(0,rows2):
        delids.append(ctx.sqlite_get_data(conn2,i,0))
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, track_id, timestamp, from_latitude, from_longitude, to_latitude, to_longitude from Trips;")
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
        track_id=ctx.sqlite_get_data(conn,i,1)
        timestamp=str(int(ctx.sqlite_get_data(conn,i,2))+946684800)
        from_latitude=int(ctx.sqlite_get_data(conn,i,3))/100000
        from_longitude=int(ctx.sqlite_get_data(conn,i,4))/100000
        fromloc=ctx.getlocation(from_latitude,from_longitude)
        to_latitude=int(ctx.sqlite_get_data(conn,i,5))/100000
        to_longitude=int(ctx.sqlite_get_data(conn,i,6))/100000
        toloc=ctx.getlocation(to_latitude,to_longitude)
        
        ctx.gui_set_data(i2,0,str(id))
        ctx.gui_set_data(i2,1,track_id)
        ctx.gui_set_data(i2,2,timestamp)
        ctx.gui_set_data(i2,3,str(from_latitude))
        ctx.gui_set_data(i2,4,str(from_longitude))
        ctx.gui_set_data(i2,5,fromloc)
        ctx.gui_set_data(i2,6,str(to_latitude))
        ctx.gui_set_data(i2,7,str(to_longitude))
        ctx.gui_set_data(i2,8,toloc)
        ctx.gui_set_data(i2,9,fsname)
        ctx.gui_set_data(i2,10,deleted)
        i2+=1

def main():
    headers=["rowid (int)","track_id (int)","timestamp (int)","from_latitude (QString)","from_longitude (QString)","from_approx_location (QString)","to_latitude (QString)", "to_longitude (QString)", "to_approx_location (QString)","Filename (QString)","Deleted (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("TomTom PersonalNetwork: Parsing data")
    ctx.gui_setMainProgressBar(0)
    filenames=ctx.pluginfilenames();
    if (len(filenames)>0):
        for fsname in filenames:
            tmpdir = tempfile.mkdtemp()
            db=tomtom.decrypt(ctx,fsname,tmpdir)
            if (db!=-1):
                converttrips(db,fsname)
                ctx.sqlite_close(db)
            shutil.rmtree(tmpdir)
    else:
        db=ctx.sqlite_open("gui",True)
        converttrips(db,"")
    ctx.gui_add_report_relevant_file("/data/com.tomtom.navkit/files/confidential.keystore")
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."