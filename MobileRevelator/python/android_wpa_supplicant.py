#Pluginname="WPA_Supplicant Google (Android)"
#Type=App

import os
import xml.etree.ElementTree as ET
import tempfile
import struct

def searchtext(text,endtext,data):
    start = data.find(text)
    slen = len(text)
    if (start != -1):
        end = data.find(endtext, start+slen)
        if (end != -1):
            return data[start + slen:end]
    return b""

def convertdata(filenames):
    zfields=[]
    row=0
    for fsname in filenames:
        print("Running WPA_Supplicant conversion: "+fsname)
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            with open(filename,"rb") as rf:
                data=rf.read()
                start=0
                offsetdb=[]
                while (start>=0):
                    start=data.find(b"network={",start)
                    if (start!=-1):
                        end=data.find(b"}",start+len("network={"))
                        if (end!=-1):
                            offsetdb.append([start,end])
                            start=end
                        else:
                            break
                    else:
                        break

                for offset in offsetdb:
                    text=data[offset[0]:offset[1]]
                    ssid=searchtext(b"ssid=\"",b"\"",text)
                    psk=searchtext(b"psk=\"",b"\"",text)
                    if (psk==b""):
                        hashpsk=searchtext(b"psk=", b"\x0A", text)
                    keymgmt=searchtext(b"key_mgmt=", b"\x0A", text)
                    desc="SSID:\""+ssid.decode()+"\";"
                    if (psk==b""):
                        desc+="Hashed PSK:\""+hashpsk.decode()+"\";"
                    else:
                        desc+="PSK:\""+psk.decode()+"\";"
                    desc+="Key_Mgmt:"+keymgmt.decode()
                    
                    zfield = {}
                    zfield["ID"]=row
                    zfield["Filename"]=fsname
                    zfield["Category"]="Accounts"
                    zfield["Type"]="WPA_Supplicant Password"
                    zfield["Package"]=""
                    zfield["Timestamp"]=""
                    zfield["Contact"]=""
                    zfield["Contact_Alias"]=""
                    zfield["Message"]=""
                    zfield["Image"]=""
                    zfield["Description"]=desc
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
    ctx.gui_setMainLabel("Google WPA_Supplicant: Parsing Password");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","Filename (QString)","Category (QString)","Type (QString)","Package (QString)","Timestamp (int)","Contact (QString)","Contact_Alias (QString)","Message (QString)","Image (QByteArray)","Description (QString)","Duration (int)","Deleted (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."