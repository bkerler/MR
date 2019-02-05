#Pluginname="Whatsapp Log (Android)"
#Filename="whatsapp-*.log"
# - added by B.Kerler (06.01.2017)
#Type=App

import sys
import zlib
import io
import os
import tempfile

def main():
    filenames=ctx.pluginfilenames();
    headers=["package (QString)","timestamp (QString)","description (QString)","filename (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Whatsapp Logs: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    report=[]
    lines=[]
    
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if (".gz" in fsname):
            if ctx.fs_file_extract(fsname,filename):
                with open(filename, "rb") as rb:
                    decompressed_data = zlib.decompress(rb.read(), 16 + zlib.MAX_WBITS)
                    lines = io.StringIO(decompressed_data.decode("ISO-8859-1")).readlines()
                os.remove(filename)
        else:
            if ctx.fs_file_extract(fsname,filename):
                with open(filename,"r",encoding="ISO-8859-1") as rb:
                    lines=rb.readlines()
                os.remove(filename)

        i=0
        oldpos=0
        totallines=len(lines)
        while (i<totallines):
            newpos=int(i/totallines*100)
            if (oldpos<newpos):
                oldpos=newpos
                ctx.gui_setMainProgressBar(oldpos)
            list=lines[i].split(" ")
            if (len(list)<6):
                i+=1
                continue
            timestamp = list[0] + " " + list[1].split(".")[0]
            if ("BatteryChange" in lines[i]):
                batinfo=lines[i].split("BatteryChange")
                if len(batinfo)>=2:
                    reportitem = []
                    reportitem.append("BatteryChange")
                    reportitem.append(timestamp)
                    reportitem.append(batinfo[1][1:])
                    reportitem.append(fsname)
                    report.append(reportitem)
            if ("network/info" in lines[i]):
                i+=1
                while (i<totallines):
                    if ("[type: " in lines[i]):
                        if (" CONNECTED" in lines[i]):
                            if ("extra: " in lines[i]):
                                extra=lines[i][lines[i].find("extra: ")+7:].split(",")[0]
                                type = lines[i][lines[i].find("[type: ")+7:].split(",")[0]
                                reportitem = []
                                reportitem.append("network/info "+type)
                                reportitem.append(timestamp)
                                reportitem.append(extra)
                                reportitem.append(fsname)
                                report.append(reportitem)
                    else:
                        i-=1
                        break
                    i+=1
                    
            if ("/screen/" in lines[i]):
                reportitem = []
                reportitem.append("Screen Event")
                reportitem.append(timestamp)
                reportitem.append((lines[i][:-1]).split(" ")[5])
                reportitem.append(fsname)
                report.append(reportitem)

            if ("ScreenLockReceiver" in lines[i]):
                reportitem = []
                reportitem.append("ScreenLock")
                reportitem.append(timestamp)
                reportitem.append((lines[i][:-1]).split(" ")[6])
                reportitem.append(fsname)
                report.append(reportitem)            
            
            if ("ntp update processed;" in lines[i]):
                info=""
                reportitem = []
                reportitem.append("ntp update")
                reportitem.append(timestamp)
                reportitem.append(lines[i][:-1])
                reportitem.append(fsname)
                report.append(reportitem)
            i+=1
    
    i=0
    oldpos=0
    count=len(report)
    #print("Count: "+str(count))
    for item in report:
        newpos=int(i/count*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        ctx.gui_set_data(i,0,item[0])
        ctx.gui_set_data(i,1,item[1])
        ctx.gui_set_data(i,2,item[2])
        ctx.gui_set_data(i,3,item[3])
        i+=1
    ctx.gui_update()
    ctx.gui_setMainProgressBar(0)
    #print(report)
    return "Finished running plugin."