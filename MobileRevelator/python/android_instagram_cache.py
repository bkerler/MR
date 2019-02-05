#Pluginname="Instagram Cache (Android)"
#Filename="MainFeed.json"
#Type=App

import os
import json
import tempfile
import datetime
import base64
from PythonQt import QtCore

jpegheader=b"\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00\x84\x00\x1B\x1A\x1A\x29\x1D\x29\x41\x26\x26\x41\x42\x2F\x2F\x2F\x42\x47\x3F\x3E\x3E\x3F\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x01\x1D\x29\x29\x34\x26\x34\x3F\x28\x28\x3F\x47\x3F\x35\x3F\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\x47\xFF\xC0\x00\x11\x08\x00\x14\x00\x2A\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01\xFF\xC4\x01\xA2\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04\x04\x00\x00\x01\x7D\x01\x02\x03\x00\x04\x11\x05\x12\x21\x31\x41\x06\x13\x51\x61\x07\x22\x71\x14\x32\x81\x91\xA1\x08\x23\x42\xB1\xC1\x15\x52\xD1\xF0\x24\x33\x62\x72\x82\x09\x0A\x16\x17\x18\x19\x1A\x25\x26\x27\x28\x29\x2A\x34\x35\x36\x37\x38\x39\x3A\x43\x44\x45\x46\x47\x48\x49\x4A\x53\x54\x55\x56\x57\x58\x59\x5A\x63\x64\x65\x66\x67\x68\x69\x6A\x73\x74\x75\x76\x77\x78\x79\x7A\x83\x84\x85\x86\x87\x88\x89\x8A\x92\x93\x94\x95\x96\x97\x98\x99\x9A\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\x01\x00\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x11\x00\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\x00\x01\x02\x77\x00\x01\x02\x03\x11\x04\x05\x21\x31\x06\x12\x41\x51\x07\x61\x71\x13\x22\x32\x81\x08\x14\x42\x91\xA1\xB1\xC1\x09\x23\x33\x52\xF0\x15\x62\x72\xD1\x0A\x16\x24\x34\xE1\x25\xF1\x17\x18\x19\x1A\x26\x27\x28\x29\x2A\x35\x36\x37\x38\x39\x3A\x43\x44\x45\x46\x47\x48\x49\x4A\x53\x54\x55\x56\x57\x58\x59\x5A\x63\x64\x65\x66\x67\x68\x69\x6A\x73\x74\x75\x76\x77\x78\x79\x7A\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x92\x93\x94\x95\x96\x97\x98\x99\x9A\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFF\xDA\x00\x0C\x03\x01\x00\x02\x11\x03\x11\x00\x3F\x00"

def getdate(date):
    ts=datetime.datetime.utcfromtimestamp(int(date))
    return ts.strftime('%d.%m.%Y %H:%M:%S')
    
def users(e):
    user={}
    if "user" in e:
        userdat=e["user"]
        for t in userdat:
            x=userdat[t]
            if "pk" in t:
                user["pk"]=x
            if "username" in t:
                user["username"]=x
            if "full_name" in t:
                user["full_name"]=x
            if "is_private" in t:
                user["is_private"]="Is_private:"+str(x)+";"
            if "profile_pic_url" in t:
                user["profile_pic_url"]="Profile_pic_url:"+x+";"
            if "is_verified" in t:
                user["is_verified"]="Is_verified:"+str(x)+";"
            if "has_anonymous_profile_picture" in t:
                user["has_anonymous_profile_picture"]="Has_anonymous_profile_picture:"+str(x)+";"
            if "friendship_status" in t:
                friendship_status=userdat["friendship_status"]
                user["friendship_status"]={}
                if "following" in friendship_status:
                    user["friendship_status"]["following"]=friendship_status["following"]
                if "outgoing_request" in friendship_status:
                    user["friendship_status"]["outgoing_request"]=friendship_status["outgoing_request"]
                if "is_bestie" in friendship_status:
                    user["friendship_status"]["is_bestie"]=friendship_status["is_bestie"]  
    return user
            
def convertposts(fentries):
    db=[]
       
    if "media_or_ad" in fentries:
        e=fentries["media_or_ad"]
        entry={}
        report={}
        media_ids=[]
        thumbnail_urls=[]
        large_urls=[]
        media_infos=[]
        report["type"]="Media_Or_Ad"
        report["desc"]=""
        if "media_type" in e:
            media_type=int(e["media_type"])
            if (media_type==2):
                report["desc"]+="Video ["
                if "video_versions" in e:
                    video_versions=e["video_versions"]
                    if (len(video_versions)>0):
                        if "url" in video_versions[0]:
                            report["desc"]+="Url:\""+video_versions[0]["url"]+"\";"
            elif (media_type==1):
                report["desc"]+="Picture ["
                if "image_versions2" in e:
                    image_versions2=e["image_versions2"]
                    if "candidates" in image_versions2:
                        candidates=image_versions2["candidates"]
                        if (len(candidates)>0):
                            if "url" in candidates[0]:
                                report["desc"]+="Url:\""+candidates[0]["url"]+"\";"
            elif (media_type==8):
                report["desc"]+="Carousel ["
                if "carousel_media" in e:
                    carousel_media=e["carousel_media"]
                    #print(carousel_media)
                    for media in carousel_media:
                        if "image_versions2" in media:
                            image_versions2=media["image_versions2"]
                            if "candidates" in image_versions2:
                                candidates=image_versions2["candidates"]
                                if (len(candidates)>0):
                                    if "url" in candidates[0]:
                                        report["desc"]+="Url:\""+candidates[0]["url"]+"\";"
        user=users(e)
        report["timestamp"]=""

        if "taken_at" in e:
            report["timestamp"]=e["taken_at"]
        
        
        report["message"]=""
        if "caption" in e:
            caption=e["caption"]
            if caption!=None:
                if "text" in caption:
                    report["message"]+="\""+caption["text"]+"\";"
        
        if "preview_comments" in e:
            preview_comments=e["preview_comments"]
            report["desc"]+="Comments:"
            report["desc"]+="["
            h=0
            for comments in preview_comments:
                cf=""
                if h==0:
                    cf+=","
                h+=1
                cf+="{"
                subusers=users(comments)
                if "username" in subusers:
                    cf+="Username:\""+subusers["username"]+"\";"
                if "username" in subusers:
                    cf+="Full_Name:\""+subusers["full_name"]+"\";"
                if "text" in comments:
                    cf+="Text:\""+comments["text"]+"\";"
                if "created_at" in comments:
                    cf+="Timestamp:"+getdate(int(comments["created_at"]))+";"
                report["desc"]+=cf+"}"
            report["desc"]+="];"
        
        report["image"]=""    
        if "preview" in e:
            preview=e["preview"]
            sub=base64.b64decode(preview)
            image=bytearray(list(jpegheader))
            image[162]=sub[1]
            image[160]=sub[2]
            image+=bytearray(list(sub[3:]))
            report["image"]=QtCore.QByteArray(bytes(image))
            #print(image)
        
        if "username" in user:
            report["contact"]=user["username"]
        else:
            report["contact"]=""
        if "full_name" in user:
            report["contact_alias"]=user["full_name"]
        else:
            report["contact_alias"]=""
        
        report["location"]=""
        
        report["package"]="com.instagram.android"
        report["deleted"]="0"
        report["category"]="Instagram cache"
        db.append(report)
    return db
    
def convertcontacts(fentries):
    db=[]
    if "suggested_users" in fentries:
        entries=fentries["suggested_users"]
        if "suggestions" in entries:
            for e in entries["suggestions"]:
                user={}
                entry={}
                media_ids=[]
                thumbnail_urls=[]
                large_urls=[]
                media_infos=[]
                if "user" in e:
                    userdat=e["user"]
                    for t in userdat:
                        x=userdat[t]
                        if "pk" in t:
                            user["pk"]=x
                        if "username" in t:
                            user["username"]=x
                        if "full_name" in t:
                            user["full_name"]=x
                        if "is_private" in t:
                            user["is_private"]="Is_private:"+str(x)+";"
                        if "profile_pic_url" in t:
                            user["profile_pic_url"]="Profile_pic_url:"+x+";"
                        if "is_verified" in t:
                            user["is_verified"]="Is_verified:"+str(x)+";"
                        if "has_anonymous_profile_picture" in t:
                            user["has_anonymous_profile_picture"]="Has_anonymous_profile_picture:"+str(x)+";"
                if "thread_title" in e:
                    entry["thread_title"]=e["thread_title"]
                if "algorithm" in e:
                    entry["algorithm"]="Algorithm:"+e["algorithm"]+";"
                if "social_context" in e:
                    entry["social_context"]="Social_Context:"+e["social_context"]+";"
                if "icon" in e:
                    entry["icon"]=e["icon"]
                if "caption" in e:
                    entry["caption"]=e["caption"]
                if "media_ids" in e:
                    entry["media_ids"]=e["media_ids"]
                if "thumbnail_urls" in e:
                    entry["thumbnail_urls"]=e["thumbnail_urls"]
                if "large_urls" in e:
                    entry["large_urls"]=e["large_urls"]
                if "media_infos" in e:
                    entry["media_infos"]=e["media_infos"]
                if "value" in e:
                    entry["value"]=e["value"]
                if "is_new_suggestion" in e:
                    entry["is_new_suggestion"]="Is_new_suggestion:"+str(e["is_new_suggestion"])+";"
                
                report={}
                if "username" in user:
                    report["contact"]=user["username"]
                else:
                    report["contact"]=""
                if "full_name" in user:
                    report["contact_alias"]=user["full_name"]
                else:
                    report["contact_alias"]=""
                
                report["message"]=""
                report["timestamp"]=""
                report["desc"]="";
                if "algorithm" in entry:
                    report["desc"]+=entry["algorithm"]
                if "social_context" in entry:
                    report["desc"]+=entry["social_context"]
                if "is_private" in user:
                    report["desc"]+=user["is_private"]
                if "profile_pic_url" in user:
                    report["desc"]+=user["profile_pic_url"]
                if "is_verified" in user:
                    report["desc"]+=user["is_verified"]
                if "is_new_suggestion" in entry:
                    report["desc"]+=entry["is_new_suggestion"]
                if "has_anonymous_profile_picture" in user:
                    report["desc"]+=user["has_anonymous_profile_picture"]
                report["location"]=""
                report["image"]=""
                report["package"]="com.instagram.android"
                report["deleted"]="0"
                report["category"]="Instagram cache"
                report["type"]="suggestions"
                db.append(report)
    return db

def convertjson(filenames,rr):
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        print(fsname)
        print(filename)
        i=rr
        if ctx.fs_file_extract(fsname,filename):
            print("Running Instagram cache conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,"rb") as rb:
                s= str(rb.read().decode("utf-8"))
                jdata=json.loads(s)
                if "feed_items" in jdata:
                    fitems=jdata["feed_items"]
                    for item in fitems:
                        if arguments["user"]==True:
                            db=convertcontacts(item)
                        elif arguments["user"]==False:
                            db=convertposts(item)
                        else:
                            break
                        rows=len(db)
                        for z in range(0,rows):
                            entry=db[z]
                            oldpos=0
                            newpos=int(z/rows*100)
                            if (oldpos<newpos):
                                oldpos=newpos
                                ctx.gui_setMainProgressBar(oldpos)
                                    
                            ctx.gui_set_data(i,0,i)
                            ctx.gui_set_data(i,1,fsname)
                            ctx.gui_set_data(i,2,entry["category"])
                            ctx.gui_set_data(i,3,entry["type"])
                            ctx.gui_set_data(i,4,entry["package"])
                            ctx.gui_set_data(i,5,entry["timestamp"])
                            ctx.gui_set_data(i,6,entry["contact"])
                            ctx.gui_set_data(i,7,entry["contact_alias"])
                            ctx.gui_set_data(i,8,entry["message"])
                            ctx.gui_set_data(i,9,entry["image"])
                            ctx.gui_set_data(i,10,entry["desc"])
                            ctx.gui_set_data(i,11,entry["location"])
                            ctx.gui_set_data(i,12,entry["deleted"])
                            i+=1
            os.remove(filename)
    

def main():
    ctx.gui_setMainLabel("Instagram Cache: Parsing...");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","fsname (QString)","category (QString)","type (QString)","package (QString)","timestamp (int)","contact (QString)","contact_alias (QString)","message (QString)", "image (QByteArray)","desc (QString)","location (QString)","deleted (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    jsonfiles=[]
    rows=0
    #print(filenames)
    for fname in filenames:
        if ".json".lower() in fname.lower():
            jsonfiles.append(fname)
        elif ".db" in fname.lower():
            convertdatabase(rows)
  
    if len(jsonfiles)!=0:
        convertjson(jsonfiles,rows)
       
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."