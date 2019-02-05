#Pluginname="Google Takeout Location History"
#Filename="Location History.json"
#Type=App

import os
import json
import tempfile
import datetime

def getdate(date):
    ts=datetime.datetime.utcfromtimestamp(int(date))
    return ts.strftime('%d.%m.%Y %H:%M:%S')
        
def convertdata(filenames):
    zfields=[]
    row=0
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            print("Running Google Takeout conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,'rb') as rt:
                dat=json.loads(rt.read().decode())
                desc=""
                if ("locations") in dat:
                    zfield={}
                    for location in dat["locations"]:
                        #print(location)
                        #break
                        zfield["rowid"]=str(row)
                        zfield["timestampMs"]=""
                        zfield["latitudeE7"]=""
                        zfield["longitudeE7"]=""
                        zfield["accuracy"]=""
                        zfield["velocity"]=""
                        zfield["activity"]=""
                        activitystring=""
                        if "activity" in location:
                            for activity in location["activity"]:
                                if "timestampMs" in activity:
                                    activitystring+="Timestamp:"+getdate(int(activity["timestampMs"])/1000)+";"
                                if "activity" in activity:
                                    subactivity=activity["activity"]
                                    if len(subactivity)>0:
                                        if "type" in subactivity[0]:
                                            activitystring+="Type:"+str(subactivity[0]["type"])+";"
                                        if "confidence" in subactivity[0]:
                                            activitystring+="Confidence:"+str(subactivity[0]["confidence"])+";"
                        zfield["activity"]=activitystring
                        zfield["filename"]=fsname
                        if "timestampMs" in location:
                            zfield["timestampMs"]=location["timestampMs"]
                        if "latitudeE7" in location:
                            zfield["latitudeE7"]=location["latitudeE7"]/10000000
                        if "longitudeE7" in location:
                            zfield["longitudeE7"]=location["longitudeE7"]/10000000
                        if "accuracy" in location:
                            zfield["accuracy"]=location["accuracy"]
                        if "velocity" in location:
                            zfield["velocity"]=location["velocity"]
                        if "altitude" in location:
                            zfield["altitude"]=location["altitude"]
                        #zfields.append(zfield)
                        ctx.gui_set_data(row,0,zfield["rowid"])
                        ctx.gui_set_data(row,1,zfield["timestampMs"])
                        ctx.gui_set_data(row,2,zfield["latitudeE7"])
                        ctx.gui_set_data(row,3,zfield["longitudeE7"])
                        if zfield["latitudeE7"] != "":
                            zfield["approx. location"]=ctx.getlocation(zfield["latitudeE7"],zfield["longitudeE7"])
                        ctx.gui_set_data(row,4,zfield["accuracy"])
                        ctx.gui_set_data(row,5,zfield["velocity"])
                        ctx.gui_set_data(row,6,zfield["altitude"])
                        ctx.gui_set_data(row,7,zfield["activity"])
                        ctx.gui_set_data(row,8,zfield["filename"])
                        row+=1
            os.remove(filename)
    #rows=len(zfields)
    #print(zfields)
    #for i in range(0,rows):
    #    zfield=zfields[i]
    #    oldpos=0
    #    newpos=int(i/rows*100)
    #    if (oldpos<newpos):
    #        oldpos=newpos
    #        ctx.gui_setMainProgressBar(oldpos)
    #    ctx.gui_set_data(i,0,zfield["rowid"])
    #    ctx.gui_set_data(i,1,zfield["timestampMs"])
    #    ctx.gui_set_data(i,2,zfield["latitudeE7"])
    #    ctx.gui_set_data(i,3,zfield["longitudeE7"])
    #    ctx.gui_set_data(i,4,zfield["accuracy"])
    #    ctx.gui_set_data(i,5,zfield["velocity"])
    #    ctx.gui_set_data(i,6,zfield["activity"])
    #    ctx.gui_set_data(i,7,zfield["filename"])


def main():
    ctx.gui_setMainLabel("Google Takeout: Parsing Location History");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","timestampMs (QString)", "latitudeE7 (int)","longitudeE7 (int)","accuracy (int)","velocity (int)","altitude (int)","activity (QString)","filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."