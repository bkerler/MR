#Pluginname="SoftAP Google (Android)"
#Type=App

import os
import xml.etree.ElementTree as ET
import tempfile
import struct

def convertdata(filenames):
    zfields=[]
    row=0
    filename=tempfile.gettempdir()+"/"+"softap.conf"
    if ctx.fs_file_extract("/misc/wifi/softap.conf",filename):
        with open(filename,"rb") as rf:
            data=rf.read()
            namelength=int(struct.unpack("b",bytes(data[5:6]))[0])
            name=data[6:6+namelength].decode()
            res=data.find(b"\x00\x00\x00\x04\x00",6+namelength)
            if (res==-1):
                return
            passwordlength=int(struct.unpack("b",bytes(data[res+5:res+6]))[0])
            password=data[res+6:res+6+passwordlength].decode()
            print("Running SoftAP conversion: ")
            zfield = {}
            zfield["ID"]=row
            zfield["Filename"]="/misc/wifi/softap.conf"
            zfield["Category"]="Accounts"
            zfield["Type"]="SoftAP Password"
            zfield["Package"]=""
            zfield["Timestamp"]=""
            zfield["Contact"]=""
            zfield["Contact_Alias"]=""
            zfield["Message"]=""
            zfield["Image"]=""
            zfield["Description"]="Password:\""+password+"\";AP Name:\""+name+"\""
            zfield["Duration"]=""
            zfield["Deleted"]="0"
            zfields.append(zfield)
            row+=1
        os.remove(filename)
    rows=len(zfields)
    
    for i in range(0,rows):
        zfield=zfields[i]
        oldpos=0
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        ctx.gui_set_data(i,0,zfield["ID"])
        ctx.gui_set_data(i,1,zfield["Filename"])
        ctx.gui_set_data(i,2,zfield["Category"])
        ctx.gui_set_data(i,3,zfield["Type"])
        ctx.gui_set_data(i,4,zfield["Package"])
        ctx.gui_set_data(i,5,zfield["Timestamp"])
        ctx.gui_set_data(i,6,zfield["Contact"])
        ctx.gui_set_data(i,7,zfield["Contact_Alias"])
        ctx.gui_set_data(i,8,zfield["Message"])
        ctx.gui_set_data(i,9,zfield["Image"])
        ctx.gui_set_data(i,10,zfield["Description"])
        ctx.gui_set_data(i,11,zfield["Duration"])
        ctx.gui_set_data(i,12,zfield["Deleted"])


def main():
    ctx.gui_setMainLabel("Google SoftAP: Parsing Password");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","Filename (QString)","Category (QString)","Type (QString)","Package (QString)","Timestamp (int)","Contact (QString)","Contact_Alias (QString)","Message (QString)","Image (QByteArray)","Description (QString)","Duration (int)","Deleted (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."