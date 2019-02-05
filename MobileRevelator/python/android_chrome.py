#Pluginname="Chrome Bookmarks (Android)"
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
            print("Running Bookmarks conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,'rb') as rt:
                dat=json.loads(rt.read().decode())
                if ("roots") in dat:
                    root=dat["roots"]
                    if "bookmark_bar" in root:
                        root=root["bookmark_bar"]
                        if "children" in root:
                            for child in root["children"]:
                                zfield={}
                                zfield["ID"]=str(row)
                                zfield["Type"]=""
                                zfield["Package"]=""
                                zfield["Duration"]=""
                                zfield["Filename"]=fsname
                                if "date_added" in child:
                                    zfield["Timestamp"]=str(child["date_added"])
                                if "name" in child:
                                    zfield["Package"]="Title: \""+child["name"]+"\""
                                if "url" in child:
                                    zfield["Other content"]=child["url"]
                                if "meta_info" in child:
                                    if "last_visited" in child["meta_info"]:
                                        zfield["Timestamp"]=str(child["meta_info"]["last_visited"])
                                    if "last_visited_desktop" in child["meta_info"]:
                                        zfield["Timestamp"]=str(child["meta_info"]["last_visited_desktop"])
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
    ctx.gui_setMainLabel("Chrome: Parsing Bookmarks");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","Type (QString)", "Package (QString)","Timestamp (int)","Duration (int)","Other_Content (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."