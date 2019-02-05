#Pluginname="Facebook app_analytics (Android)"
#Type=App

import os
import struct
import json
import tempfile

def convertdata(filenames):
    zfields=[]
    for fsname in filenames:
        print("Running Facebook conversion: " + fsname[fsname.rfind("/") + 1:])
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            with open(filename, "rb") as ff:
                try:
                    data = str(ff.read().decode("utf-8"))+str("]}")
                    jdata = json.loads(data)
                except:
                    continue
                row = 0
                timestamp=""
                uid=""
                desc=""
                if "time" in jdata:
                    timestamp = str(jdata["time"])
                if "uid" in jdata:
                    uid=str(jdata["uid"])
                if "data" in jdata:
                    fbdata=jdata["data"]
                    for subdata in fbdata:
                        if "extra" in subdata:
                            extra=subdata["extra"]
                            #if ("network_type" in extra) or ("battery" in extra) or ("connection" in extra) or ("text" in extra):
                            zfield = {}
                            zfield["ID"] = row
                            zfield["Filename"]=fsname
                            zfield["Type"] = "Generic"
                            if uid!="":
                                zfield["Contact"] = uid
                            else:
                                zfield["Contact"] = ""
                            zfield["Timestamp"] = timestamp
                            description = ""
                            if "suggestions_at_end_of_session" in extra:
                                zfield["Type"] = "Suggestions"
                                dt=extra["suggestions_at_end_of_session"]
                                for d in dt:
                                    if "text" in d:
                                        description += "suggestion: \"" + d["text"] + "\";"
                            if "dest_module_uri" in extra:
                                zfield["Type"] = "Uri"
                                if "dest_module_uri" in extra:
                                    description+="dest_module_uri: "+extra["dest_module_uri"]+";"
                                if "click_point" in extra:
                                    description+="click_point: "+extra["click_point"]+";"
                                if "source_module" in extra:
                                    description+="source_module: "+extra["source_module"]+";"
                            if "video_id" in extra:
                                    zfield["Type"] = "Video"
                                    if "video_id" in extra:
                                        description+="video_id: "+extra["video_id"]+";"
                                    if "video_last_start_time_position" in extra:
                                        description+="video_last_start_time_position: "+str(extra["video_last_start_time_position"])+";"
                                    if "video_play_reason" in extra:
                                        description+="video_play_reason: "+extra["video_play_reason"]+";"
                                    if "video_time_position" in extra:
                                        description+="video_time_position: "+str(extra["video_time_position"])+";"
                            if "network_type" in extra:
                                    description+="network_type: "+extra["network_type"]+";"
                            if "network_subtype" in extra:
                                    description+="network_subtype: "+extra["network_subtype"]+";"
                            if "connqual" in extra:
                                    description+="connqual: "+extra["connqual"]+";"
                            if "was_backgrounded" in extra:
                                    description+="was_backgrounded: "+str(extra["was_backgrounded"])+";"
                            if "airplane_mode_on" in extra:
                                    description+="airplane_mode_on: "+str(extra["airplane_mode_on"])+";"
                            if "battery" in extra:
                                    zfield["Type"] = "Battery"
                                    if "battery" in extra:
                                        description+="battery: "+str(extra["battery"])+";"
                                    if "charge_state" in extra:
                                        description+="charge_state: "+extra["charge_state"]+";"
                                    if "battery_health" in extra:
                                        description+="battery_health: "+extra["battery_health"]+";"
                                    #description = json.dumps(extra, separators=(',',':'))
                            if (len(description)>1):
                                zfield["Other content"] = description
                                zfields.append(zfield)
                                row += 1
            os.remove(filename)
    rows = len(zfields)
    # print(zfields)
    for i in range(0, rows):
        zfield = zfields[i]
        oldpos = 0
        newpos = int(i / rows * 100)
        if (oldpos < newpos):
            oldpos = newpos
            ctx.gui_setMainProgressBar(oldpos)
        ctx.gui_set_data(i, 0, zfield["ID"])
        ctx.gui_set_data(i, 1, zfield["Type"])
        ctx.gui_set_data(i, 2, zfield["Contact"])
        ctx.gui_set_data(i, 3, zfield["Timestamp"])
        ctx.gui_set_data(i, 4, zfield["Other content"])
        ctx.gui_set_data(i, 5, zfield["Filename"])


def main():
    ctx.gui_setMainLabel("Facebook App Analytics: Parsing ...");
    ctx.gui_setMainProgressBar(0)
    headers = ["rowid (int)", "Type (QString)", "Contact (QString)", "Timestamp (int)", "Other_Content (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."