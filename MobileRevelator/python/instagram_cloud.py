#Pluginname="Instagram Cloud"
#Filename=".json"
#Type=App
#arguments="arguments={}\narguments["media"]=True\narguments["messages"]=True\narguments["comments"]=True\n"
import os
import json
import tempfile
import datetime

def getdate(date):
    ts=datetime.datetime.utcfromtimestamp(int(date))
    return ts.strftime('%d.%m.%Y %H:%M:%S')
        
def initzfield(fsname):
    zfield={}
    zfield["sender"]=""
    zfield["desc"]=""
    zfield["receipients"]=""
    zfield["message"]=""
    zfield["timestamp"]=""
    zfield["desc"]=""
    zfield["media_caption"]=""
    zfield["media_location"]=""
    zfield["media_path"]=""
    zfield["media_type"]=""
    zfield["comments"]=""
    zfield["like"]=""
    zfield["first_name"]=""
    zfield["last_name"]=""
    zfield["contact_id"]=""
    zfield["filename"]=fsname
    return zfield
    
def convertdata(filenames):
    db={}
    row=0
    for fsname in filenames:
        if "messages" in arguments:
            if "messages.json" in fsname and arguments["messages"]==True:
                filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
                if ctx.fs_file_extract(fsname,filename):
                    print("Running Instagram messages conversion: "+filename[filename.rfind("/")+1:])
                    with open(filename,'rb') as rt:
                        dat=json.loads(rt.read().decode())
                        desc=""
                        for val in dat:
                            participants=[]
                            if ("participants") in val:
                                participants=val["participants"]
                            if ("conversation") in val:
                                conversations=val["conversation"]
                                for conversation in conversations:
                                    zfield=initzfield(fsname)
                                    if "created_at" in conversation:
                                       zfield["timestamp"]=conversation["created_at"][:-13]
                                    if "sender" in conversation:
                                       zfield["sender"]=conversation["sender"]
                                       tmp=""
                                       for member in participants:
                                           if zfield["sender"] != member:
                                                 tmp+="\""+member+"\";"
                                       zfield["receipients"]=tmp[:-1]
                                    if "text" in conversation:
                                       zfield["message"]=conversation["text"]
                                    if "heart" in conversation:
                                       zfield["message"]+=conversation["heart"]
                                    if "story_share" in conversation:
                                       zfield["desc"]="Story_Share:\""+conversation["story_share"]+"\";"
                                    if "mentioned_username" in conversation:
                                       zfield["desc"]+="Mentioned_Username:\""+conversation["mentioned_username"]+"\";"
                                    db[row]=zfield
                                    row+=1
                    os.remove(filename)
        
        if "media" in arguments:
            if "media.json" in fsname and arguments["media"]==True:
                filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
                if ctx.fs_file_extract(fsname,filename):
                    print("Running Instagram media conversion: "+filename[filename.rfind("/")+1:])
                    with open(filename,'rb') as rt:
                        dat=json.loads(rt.read().decode())
                        #stories, profile, photos, videos, direct
                        for val in dat:
                             stories=dat[val]
                             for story in stories:
                                    zfield=initzfield(fsname)
                                    if "taken_at" in story:
                                       zfield["timestamp"]=story["taken_at"]
                                    if "media_type" in story:
                                       zfield["media_type"]=val
                                    if "caption" in story:
                                       zfield["media_caption"]=story["caption"]
                                    if "path" in story:
                                       zfield["media_path"]=story["path"]
                                    if "location" in story:
                                       zfield["media_location"]=story["location"]
                                    db[row]=zfield
                                    row+=1
                                    
                    os.remove(filename)
        if "comments" in arguments:
            if "comments.json" in fsname  and arguments["comments"]==True:
                filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
                if ctx.fs_file_extract(fsname,filename):
                    print("Running Instagram comments conversion: "+filename[filename.rfind("/")+1:])
                    with open(filename,'rb') as rt:
                        dat=json.loads(rt.read().decode())
                        for val in dat:
                             media_comments=dat[val]
                             for comment in media_comments:
                                zfield=initzfield(fsname)
                                zfield["timestamp"]=comment[0]
                                zfield["comments"]=comment[1]
                                zfield["sender"]=comment[2]
                                db[row]=zfield
                                row+=1
                    os.remove(filename)
        if "contacts" in arguments:
            if "contacts.json" in fsname  and arguments["contacts"]==True:
                filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
                if ctx.fs_file_extract(fsname,filename):
                    print("Running Instagram contacts conversion: "+filename[filename.rfind("/")+1:])
                    with open(filename,'rb') as rt:
                        dat=json.loads(rt.read().decode())
                        for contact in dat:
                            zfield=initzfield(fsname)
                            if "first_name" in contact:
                                zfield["first_name"]=contact["first_name"]
                            if "last_name" in contact:
                                zfield["last_name"]=contact["last_name"]
                            if "contact" in contact:
                                zfield["contact_id"]=contact["contact"]
                            db[row]=zfield
                            row+=1
                    os.remove(filename)
                
    row=0
    for item in db:
          zfield=db[item]   
          ctx.gui_set_data(row,0,str(row))
          ctx.gui_set_data(row,1,zfield["sender"])
          ctx.gui_set_data(row,2,zfield["receipients"])
          ctx.gui_set_data(row,3,item)
          ctx.gui_set_data(row,4,zfield["message"])
          ctx.gui_set_data(row,5,zfield["media_type"])
          ctx.gui_set_data(row,6,zfield["media_path"])
          ctx.gui_set_data(row,7,zfield["media_caption"])
          ctx.gui_set_data(row,8,zfield["media_location"])
          ctx.gui_set_data(row,9,zfield["comments"])
          ctx.gui_set_data(row,10,zfield["like"])
          ctx.gui_set_data(row,11,zfield["desc"])
          ctx.gui_set_data(row,12,zfield["filename"])                                
          ctx.gui_set_data(row,13,zfield["first_name"])
          ctx.gui_set_data(row,14,zfield["last_name"])
          ctx.gui_set_data(row,15,zfield["contact_id"])
          row+=1


def main():
    ctx.gui_setMainLabel("Instagram: Parsing Cloud data");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","sender (QString)", "receipients (QString)","timestamp (QString)","message (QString)","media_type (QString)","media_path (QString)","media_caption (QString)","media_location (QString)","comments (QString)","like (QString)","desc (QString)","filename (QString)","first_name (QString)","last_name (QString)","contact_id (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."