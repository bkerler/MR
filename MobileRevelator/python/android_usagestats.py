#Pluginname="Usagestats Google (Android)"
#Type=App

import os
import xml.etree.ElementTree as ET
import tempfile

def checktime(attrib, time):
    timeoffset=0
    if "lastTimeActive" in attrib:
        timeoffset=int(attrib["lastTimeActive"])
    if "lastTimeActiveSystem" in attrib:
        timeoffset=int(attrib["lastTimeActiveSystem"])
    #print (int(timeoffset))
    if (int(timeoffset)<0):
        return -timeoffset
    if (int(timeoffset) > 1000000000000):
        return timeoffset
    return time+timeoffset

def convertdata(filenames):
    zfields=[]
    row=0
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            print("Running Usagestats conversion: "+filename[filename.rfind("/")+1:])
            if ("yearly" in filename):
                os.remove(filename)
                continue
            try:
                timeoffset=int(filename[filename.rfind("/")+1:])
            except:
                os.remove(filename)
                continue
            if (timeoffset==0):
                os.remove(filename)
                continue
            try:
                tree = ET.parse(filename).getroot()
            except:
                os.remove(filename)
                continue
            
            for child in tree:
                tag=child.tag
                #attrib=child.attrib
                #print(tag,attrib)
                if (tag=="packages"):
                    for subchild in child:
                        subtag = subchild.tag
                        attrib = subchild.attrib
                        if (subtag=="package"):
                            zfield = {}
                            zfield["ID"]=row
                            zfield["Filename"]=fsname
                            zfield["Type"]="Usagestats [Event]"
                            zfield["Package"]=attrib["package"]
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            zfield["Duration"]=int(attrib["timeActive"])
                            description="Last event:"
                            flag=int(attrib["lastEvent"])
                            if flag==0:
                                description += "No event"
                            elif flag==1:
                                description += "Move to foreground"
                            elif flag==2:
                                description += "Move to background"
                            elif flag==3:
                                description += "App was in the foreground at the end of day"
                            elif flag==4:
                                description += "App was in the foreground the previous day"
                            elif flag==5:
                                description += "Device Config changed"
                            elif flag==7:
                                description += "User interacted with app"
                            else:
                                description += "Unknown flag: "+str(flag)
                            zfield["Other content"]=description
                            zfields.append(zfield)
                            row+=1
                elif (tag=="configurations"):
                    for subchild in child:
                        subtag = subchild.tag
                        attrib = subchild.attrib
                        description=""
                        if (subtag=="config"):
                            zfield = {}
                            zfield["ID"] = row
                            zfield["Filename"]=fsname
                            zfield["Type"] = "Usagestats [Config]"
                            zfield["Package"] = "Cell info"
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            zfield["Duration"] = int(attrib["timeActive"])
                            if "mcc" in attrib:
                                description = "MCC:"+attrib["mcc"]+" MNC:"+attrib["mnc"]
                                zfield["Other content"] = description
                                row += 1
                                zfields.append(zfield)

                            zfield = {}
                            zfield["ID"] = row
                            zfield["Filename"]=fsname
                            zfield["Type"] = "Usagestats [Config]"
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            zfield["Duration"] = int(attrib["timeActive"])
                            zfield["Package"] = "Locale"
                            if "locale" in attrib:
                                description = attrib["locale"]
                            else:
                                description = ""
                            zfield["Other content"] = description
                            row += 1
                            zfields.append(zfield)

                            zfield = {}
                            zfield["ID"] = row
                            zfield["Filename"]=fsname
                            zfield["Type"] = "Usagestats [Config]"
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            zfield["Duration"] = int(attrib["timeActive"])
                            zfield["Package"] = "Keyboard"
                            keyhid = int(attrib["keyHid"])
                            if keyhid == 0:
                                description="Undefined"
                            elif keyhid == 1:
                                description = "Visible"
                            elif keyhid == 2:
                                description = "Hidden"
                            zfield["Other content"] = description
                            row += 1
                            zfields.append(zfield)

                            zfield = {}
                            zfield["ID"] = row
                            zfield["Filename"]=fsname
                            zfield["Type"] = "Usagestats [Config]"
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            zfield["Duration"] = int(attrib["timeActive"])
                            zfield["ID"] = row
                            zfield["Package"] = "Navigation"
                            navhid = int(attrib["navHid"])
                            if keyhid == 0:
                                description = "Undefined"
                            elif keyhid == 1:
                                description = "Visible"
                            elif keyhid == 2:
                                description = "Hidden"
                            zfield["Other content"] = description
                            row += 1
                            zfields.append(zfield)
                elif (tag=="event-log"):
                    for subchild in child:
                        subtag = subchild.tag
                        attrib = subchild.attrib
                        description=""
                        if (subtag=="event"):
                            zfield["ID"]=row
                            zfield["Filename"]=fsname
                            zfield["Type"]="Usagestats [Event]"
                            zfield["Package"]=attrib["package"]
                            zfield["Timestamp"]=checktime(attrib,timeoffset)
                            if "lastEvent" in attrib:
                                description = "Last event:"
                                flag = int(attrib["lastEvent"])
                                if flag == 0:
                                    description += "No event"
                                elif flag == 1:
                                    description += "Move to foreground"
                                elif flag == 2:
                                    description += "Move to background"
                                elif flag == 5:
                                    description += "Device Config changed"
                                elif flag == 7:
                                    description += "User interacted with app"
                                else:
                                    description += "Unknown flag: " + str(flag)
                            if "class" in attrib:
                                description="Class:"+attrib["class"]+";"+description
                            zfield["Other content"] = description
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
    ctx.gui_setMainLabel("Google Usagestats: Parsing Locations");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","Type (QString)", "Package (QString)","Timestamp (int)","Duration (int)","Other_Content (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."