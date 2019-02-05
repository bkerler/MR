#Pluginname="Analytics_DB2 (Android)"
#Filename="analytics_db2"
#Type=App

import struct
import json

def converttime(val,db):
    conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
    res=ctx.sqlite_get_data(conn,0,0)
    ctx.sqlite_cmd_close(conn)
    return res

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, datetime(timestamp/1000,'unixepoch','localtime'), timestamp, data from events;")
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
        stimestamp=ctx.sqlite_get_data(conn,i,1)
        timestamp=ctx.sqlite_get_data(conn,i,2)
        data=ctx.sqlite_get_data(conn,i,3)
        result=""

        jdata=json.loads(data)
        if "name" in jdata:
          if (jdata["name"]=="device_status"):
            if "extra" in jdata:
               if "battery" in jdata["extra"]:
                  result+="Battery: "+str(jdata["extra"]["battery"])+";"
               if "charge_state" in jdata["extra"]:
                  result+="Charge_State:"+jdata["extra"]["charge_state"]+";"
               if "wifi_enabled" in jdata["extra"]:
                  result+="Wifi_Enabled:"+str(jdata["extra"]["wifi_enabled"])+";"
               if "wifi_connected" in jdata["extra"]:
                  result+="Wifi_Connected:"+str(jdata["extra"]["wifi_connected"])+";"
               if "airplane_mode_on" in jdata["extra"]:
                  result+="Airplane_mode_on:"+str(jdata["extra"]["airplane_mode_on"])+";"
               if "time_since_boot_ms" in jdata["extra"]:
                  time=int(timestamp)-int(jdata["extra"]["time_since_boot_ms"])
                  result+="Last boot:"+converttime(time,db)+";"
               ctx.gui_set_data(i2,0,id)
               ctx.gui_set_data(i2,1,stimestamp)
               ctx.gui_set_data(i2,2,result)
               i2+=1
          if (jdata["name"]=="device_info"):
            if "extra" in jdata:
               if "sim_info" in jdata["extra"]:
                  result+="Sim_info:\""+str(jdata["extra"]["sim_info"])+"\";"
               if "phone_number_by_library" in jdata["extra"]:
                  result+="Phone_number_by_library:\""+str(jdata["extra"]["phone_number_by_library"])+"\";"
               ctx.gui_set_data(i2,0,id)
               ctx.gui_set_data(i2,1,stimestamp)
               ctx.gui_set_data(i2,2,result)
               i2+=1
    ctx.sqlite_cmd_close(conn)
    
def main():
    headers=["rowid (int)","timestamp (int)","result (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Analytics_DB2: Parsing Analytics");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."