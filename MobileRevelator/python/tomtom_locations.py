#Pluginname="Locations (TomTom)"
#Filename="locations.sqlite"
#Type=App

import struct
import tempfile
import shutil
from Library import tomtom
  
def converttracks(db,fsname):
    conn2=ctx.sqlite_get_deletedrecords(db,"Locations",True)
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    delids=[]
    for i in range(0,rows2):
        delids.append(ctx.sqlite_get_data(conn2,i,0))
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, id, type, latitude, longitude, name, createdOn, modifiedOn from Locations;")
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
        type=ctx.sqlite_get_data(conn,i,2)
        latitude=int(ctx.sqlite_get_data(conn,i,3))/1000000
        longitude=int(ctx.sqlite_get_data(conn,i,4))/1000000
        name=ctx.sqlite_get_data(conn,i,5)
        #fromloc=ctx.getlocation(latitude,longitude)
        createdOn=ctx.sqlite_get_data(conn,i,6)
        modifiedOn=ctx.sqlite_get_data(conn,i,7)
        
        ctx.gui_set_data(i2,0,str(id))
        ctx.gui_set_data(i2,1,track_id)
        ctx.gui_set_data(i2,2,type)
        ctx.gui_set_data(i2,3,latitude)
        ctx.gui_set_data(i2,4,longitude)
        ctx.gui_set_data(i2,5,name)
        #ctx.gui_set_data(i2,6,fromloc)
        ctx.gui_set_data(i2,6,createdOn)
        ctx.gui_set_data(i2,7,modifiedOn)
        ctx.gui_set_data(i2,8,fsname)
        ctx.gui_set_data(i2,9,deleted)
        i2+=1

def main():
    headers=["rowid (int)","id (int)","type (int)","latitude (int)","longitude (QString)","name (QString)","created_Timestamp (int)", "modified_Timestamp (int)","Filename (QString)","Deleted (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("TomTom Locations: Parsing data");
    ctx.gui_setMainProgressBar(0)
    filenames=ctx.pluginfilenames();
    if (len(filenames)>0):
        for fsname in filenames:
            tmpdir = tempfile.mkdtemp()
            db=tomtom.decrypt(ctx,fsname,tmpdir)
            if (db!=-1):
                converttracks(db,fsname)
                ctx.sqlite_close(db)
            shutil.rmtree(tmpdir)
    else:
        db=ctx.sqlite_open("gui",True)
        converttracks(db,"")
    ctx.gui_add_report_relevant_file("/data/com.tomtom.navkit/files/confidential.keystore")
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."