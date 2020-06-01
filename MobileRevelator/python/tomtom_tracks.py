#Pluginname="Tracks (TomTom)"
#Filename="tracks.sqlite"
#Type=App

import struct
import tempfile
import shutil
from Library import mrtime
from Library import tomtom
from PythonQt import QtCore
                
def converttracks(db,fsname):
    conn2=ctx.sqlite_get_deletedrecords(db,"Tracks",True)
    ctx.gui_setMainLabel("Status: Seeking tracks.")
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    delids=[]
    for i in range(0,rows2):
        delids.append(ctx.sqlite_get_data(conn2,i,0))
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, id, startTime, southWestLat, southWestLon, northEastLat, northEastLon, endTime from Tracks;")
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
        starttimestamp=ctx.sqlite_get_data(conn,i,2)
        if (starttimestamp==""): 
            continue
        endtimestamp=ctx.sqlite_get_data(conn,i,7)
        if (ctx.sqlite_get_data(conn,i,3)==""): 
            continue
        from_latitude=int(ctx.sqlite_get_data(conn,i,3))/100000
        from_longitude=int(ctx.sqlite_get_data(conn,i,4))/100000
        fromloc=ctx.getlocation(from_latitude,from_longitude)
        to_latitude=int(ctx.sqlite_get_data(conn,i,5))/100000
        to_longitude=int(ctx.sqlite_get_data(conn,i,6))/100000
        toloc=ctx.getlocation(to_latitude,to_longitude)
        
        ctx.gui_set_data(i2,0,str(id))
        ctx.gui_set_data(i2,1,track_id)
        ctx.gui_set_data(i2,2,"Route Info")
        ctx.gui_set_data(i2,3,starttimestamp)
        ctx.gui_set_data(i2,4,endtimestamp)
        ctx.gui_set_data(i2,5,str(from_latitude))
        ctx.gui_set_data(i2,6,str(from_longitude))
        ctx.gui_set_data(i2,7,fromloc)
        ctx.gui_set_data(i2,8,str(to_latitude))
        ctx.gui_set_data(i2,9,str(to_longitude))
        ctx.gui_set_data(i2,10,toloc)
        ctx.gui_set_data(i2,11,mrtime.getdate(endtimestamp))
        ctx.gui_set_data(i2,12,fsname)
        ctx.gui_set_data(i2,13,deleted)
        i2+=1

def converttrackchunks(db,fsname):
    conn2=ctx.sqlite_get_deletedrecords(db,"TrackChunks",True)
    ctx.gui_setMainLabel("Status: Seeking Track Chunks.")
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    delids=[]
    for i in range(0,rows2):
        delids.append(ctx.sqlite_get_data(conn2,i,0))
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, track_id, points from TrackChunks;")
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
        points=ctx.sqlite_get_data(conn,i,2).data()
        #print(id)
        for i in range(0,len(points),0x28):
            lat, lon, unknown, year, month, day, hour, min, sec, msec = struct.unpack("<iiiiiiiiii",points[i:i+0x28])
            from_latitude=int(lat)/100000
            from_longitude=int(lon)/100000
            fromloc=ctx.getlocation(from_latitude,from_longitude)
            endtimestamp=mrtime.packDate(day+1,month+1,year,hour,min,sec,msec)
            ctx.gui_set_data(i2,0,str(id))
            ctx.gui_set_data(i2,1,track_id)
            ctx.gui_set_data(i2,2,"Route")
            ctx.gui_set_data(i2,3,endtimestamp)
            ctx.gui_set_data(i2,4,"")
            ctx.gui_set_data(i2,5,str(from_latitude))
            ctx.gui_set_data(i2,6,str(from_longitude))
            ctx.gui_set_data(i2,7,fromloc)
            ctx.gui_set_data(i2,8,"")
            ctx.gui_set_data(i2,9,"")
            ctx.gui_set_data(i2,10,"")
            ctx.gui_set_data(i2,11,mrtime.getdate(endtimestamp))
            ctx.gui_set_data(i2,12,fsname)
            ctx.gui_set_data(i2,13,deleted)
            i2+=1
        
def main():
    headers=["rowid (int)","track_id (int)","type (QString)","starttimestamp (int)","endtimestamp (int)","southWestLat (QString)","northEastLon (QString)","southWest_approx_location (QString)","northEastLat (QString)", "northEastLon (QString)", "northEast_approx_location (QString)","endtimestamp_decoded (QString)","Filename (QString)","Deleted (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("TomTom Tracks: Parsing data");
    ctx.gui_setMainProgressBar(0)

    filenames=ctx.pluginfilenames();
    if (len(filenames)>0):
        for fsname in filenames:
            tmpdir = tempfile.mkdtemp()
            db=tomtom.decrypt(ctx,fsname,tmpdir)
            if (db!=-1):
                ctx.gui_setMainLabel("Status: Seeking tracks.")
                converttracks(db,fsname)
                ctx.gui_setMainLabel("Status: Seeking trackchunks.")
                converttrackchunks(db,fsname)
                ctx.sqlite_close(db)
            shutil.rmtree(tmpdir)
    else:
        db=ctx.sqlite_open("gui",True)
        converttracks(db,"")
        converttrackchunks(db,"")
    ctx.gui_add_report_relevant_file("/data/com.tomtom.navkit/files/confidential.keystore")
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."
