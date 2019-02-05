#Pluginname="Booking.com Searches (Android)"
#Filename="history.db"
#Type=App

def convertdata(db):
    #ctx.gui_clearData()
    ctx.gui_setMainLabel("Status: Converting booking.com searches")
    conn=ctx.sqlite_run_cmd(db,"select rowid, row_id, GROUP_CONCAT(name || \"=\" || value,\";\") from extra_searches_columns group by row_id;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    ctx.gui_setMainLabel("Status: Converting booking.com searches")
    oldpos=0
    r=0
    for i in range(0,rows):
        entry={}
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        row_id=ctx.sqlite_get_data(conn,i,1)
        data=ctx.sqlite_get_data(conn,i,2).split(";")
        for x in data:
            tmp=x.split("=")
            entry[tmp[0]]=tmp[1]

        ctx.gui_set_data(r,0,id)
        if ("createdEpoch" in entry):
            ctx.gui_set_data(r,1,entry["createdEpoch"])
        else:
            ctx.gui_set_data(r,1,"")
        if ("city" in entry):
            ctx.gui_set_data(r,2,entry["city"])
        else:
            ctx.gui_set_data(r,2,"")
        if ("latitude" in entry):
            ctx.gui_set_data(r,3,entry["latitude"])
        else:
            ctx.gui_set_data(r,3,"")
        if ("longitude" in entry):
            ctx.gui_set_data(r,4,entry["longitude"])
        else:
            ctx.gui_set_data(r,4,"")
        if ("location_name" in entry):
            ctx.gui_set_data(r,5,entry["location_name"])
        else:
            ctx.gui_set_data(r,5,"")
        r+=1
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","timestamp (int)","city (QString)","latitude (QString)","longitude (QString)","location_name (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Booking.com: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.sqlite_close(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."