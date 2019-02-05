#Pluginname="GLS Tracking (Android)"
#Type=App

import os
import json
import tempfile

def convertdata(filenames):
    zfields=[]
    row=0
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            print("Running GLS conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,'rb') as rt:
                dat=json.loads(rt.read().decode())
                desc=""
                if ("innerResult") in dat:
                    zfield={}
                    root=dat["innerResult"]
                    if "expeditionDate" in root:
                        desc+="ExpeditionDate:"+root["expeditionDate"]+";"
                    if "recipient" in root:
                        desc+="Recipient:"+root["recipient"]+";"
                    if "recipient" in root:
                        desc+="Sender:"+root["sender"]+";"
                    if "parcelNumber" in root:
                        desc+="ParcelNumber:"+root["parcelNumber"]+";"
                    if "stepList" in root:
                        st=root["stepList"]
                        for child in st:
                                if "dateStep" in child:
                                    desc+="[DateStep:"+child["dateStep"]+";"
                                if "note" in child:
                                    desc+="Note:"+child["note"]+";"
                                if "place" in child:
                                    desc+="Place:"+child["place"]+";"
                                if "timeStep" in child:
                                    desc+="TimeStep:"+child["timeStep"]+";"
                                if "statusTitle" in child:
                                    desc+="Status:"+child["statusTitle"]+"]"
                    zfield["ID"]=str(row)
                    zfield["Type"]=""
                    zfield["Package"]=""
                    zfield["Duration"]=""
                    zfield["Filename"]=fsname
                    zfield["Timestamp"]=""
                    zfield["Other content"]=desc
                    row+=1
                    zfields.append(zfield)
            os.remove(filename)
    rows=len(zfields)
    #print(zfields)
    for i in range(0,rows):
        zfield=zfields[i]
        oldpos=0
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        ctx.gui_set_data(i,0,zfield["ID"])
        ctx.gui_set_data(i,1,zfield["Type"])
        ctx.gui_set_data(i,2,zfield["Package"])
        ctx.gui_set_data(i,3,zfield["Timestamp"])
        ctx.gui_set_data(i,4,zfield["Duration"])
        ctx.gui_set_data(i,5,zfield["Other content"])
        ctx.gui_set_data(i,6,zfield["Filename"])


def main():
    ctx.gui_setMainLabel("GLS: Parsing Parcels");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","Type (QString)", "Package (QString)","Timestamp (int)","Duration (int)","Other_Content (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."