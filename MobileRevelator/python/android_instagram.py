#Pluginname="Instagram (Android)"
#Filename="direct.db"
#Type=App

import os
import json
import tempfile

def convertdata(e):
    db=[]
    thread_id=""
    thread_title=""
    fromid=""
    fromalias=""
    toid=""
    toalias=""
    timestamp=""
    i=0
    reps = []
    
    if "thread_id" in e:
        thread_id=e["thread_id"]
    if "thread_title" in e:
        thread_title=e["thread_title"]
     #if "inviter" in e:
    #    inviter=e["inviter"]
    #    if "username" in inviter:
    #        fromid=inviter["username"]
    #    if "full_name" in inviter:
    #        fromalias=inviter["full_name"]
    if "recipients" in e:
        for recipients in e["recipients"]:
            if "username" in recipients:
                toid=recipients["username"]
            if "full_name" in recipients:
                toalias=recipients["full_name"]
            replist=[toid,toalias]
            reps.append(replist)
    if "cached_messages" in e:
        for cached_messages in e["cached_messages"]:
            #print(cached_messages)
            fromid = ""
            fromaliases = ""
            if "user" in cached_messages:
                user = cached_messages["user"]
                if "username" in user:
                    fromid=user["username"]
                if "full_name" in user:
                    fromalias=user["full_name"]
            if "timestamp" in cached_messages:
                timestamp=cached_messages["timestamp"]
            if "content_type" in cached_messages:
                content_type = cached_messages["content_type"]
                if (content_type=="TEXT"):
                    desc = content_type
                    text=cached_messages["text"]
                    toids=""
                    toaliases=""
                    for h in reps:
                        toids+="\""+h[0]+"\""+"\n"
                        toaliases+="\""+h[1]+"\""+"\n"
                    toids = toids[:-1]
                    toaliases = toaliases[:-1]
                    entry=[thread_id,thread_title,fromid,fromalias,toids,toaliases,timestamp,text,desc]
                    db.append(entry)
                    #print(entry)
                else:
                    desc = content_type
                    text = ""
                    toids = ""
                    toaliases = ""
                    for h in reps:
                        toids += "\""+h[0]+"\"" + ";"
                        toaliases += "\""+h[1]+"\""+";"
                    toids=toids[:-1]
                    toaliases=toaliases[:-1]
                    entry = [thread_id, thread_title, fromid, fromalias, toids, toaliases, timestamp, text, desc]
                    db.append(entry)
                    #print(entry)
    return db

def convertdata_new(e,threads):
    db=[]
    thread_id=""
    thread_title=""
    fromid=""
    fromalias=""
    toids=""
    toaliases=""
    timestamp=""
    status=""
    i=0
    reps = []
    if "thread_key" in e:
        thread_key=e["thread_key"]
        if "thread_id" in thread_key:
            thread_id=thread_key["thread_id"]
            toids=threads[thread_id]
    
    if "status" in e:
        status=e["status"]

    if "user" in e:
        user = e["user"]
        if "username" in user:
            fromid=user["username"]
        if "full_name" in user:
            fromalias=user["full_name"]
    
    if "timestamp" in e:
        timestamp=e["timestamp"]

    if "content_type" in e:
        content_type = e["content_type"]
        if (content_type=="TEXT"):
            desc = content_type
            text=e["text"]
            entry=[thread_id,thread_title,fromid,fromalias,toids,"",timestamp,text,desc]
            db.append(entry)
        elif (content_type=="MEDIA_SHARE"):
            desc = content_type
            text=""
            if "media_share" in e:
                media_share = e["media_share"]
                #for h in media_share:
                #    print(h)
                
                if "image_versions2" in media_share:
                    image_versions2 = media_share["image_versions2"]
                    if "candidates" in image_versions2:
                        candidates=image_versions2["candidates"]
                        for m in candidates:
                            if "url" in m:
                                desc+=";"
                                desc+=m["url"]
                                break
                if "caption" in media_share:
                    caption=media_share["caption"]
                    #for h in caption:
                    #    print(h)
                    desc+=";Caption:["
                    if "text" in caption:
                        desc+="Text:\""+caption["text"]+"\""
                        
                    if "user" in caption:
                        user = caption["user"]
                        if "username" in user:
                            desc+=";username:\""+user["username"]+"\""
                            fromid=user["username"]
                        if "full_name" in user:
                            desc+=";Alias:\""+user["full_name"]+"\""
                            fromalias=user["full_name"]
                    desc+="]"
                    #print(desc)
                    
            entry=[thread_id,thread_title,fromid,fromalias,toids,toaliases,timestamp,text,desc]
            db.append(entry)
            #print(entry)
        else:
            desc = content_type
            text = ""
            entry = [thread_id, thread_title, fromid, fromalias, toids, toaliases, timestamp, text, desc]
            db.append(entry)
            #print(entry)
    return db

def convertjson(filenames,rr):
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        #print(filename)
        i=rr
        if ctx.fs_file_extract(fsname,filename):
            print("Running Instagram conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,"rb") as rb:
                s= str(rb.read().decode("utf-8"))
                jdata=json.loads(s)
                if "entries" in jdata:
                    entries=jdata["entries"]
                    for e in entries:
                        db=convertdata(e)
                        rows=len(db)
                        for z in range(0,rows):
                            entry=db[z]
                            oldpos=0
                            newpos=int(z/rows*100)
                            if (oldpos<newpos):
                                oldpos=newpos
                                ctx.gui_setMainProgressBar(oldpos)
                            ctx.gui_set_data(i,0,i)
                            ctx.gui_set_data(i,1,entry[0])
                            ctx.gui_set_data(i,2,entry[1])
                            ctx.gui_set_data(i,3,entry[2])
                            ctx.gui_set_data(i,4,entry[3])
                            ctx.gui_set_data(i,5,entry[4])
                            ctx.gui_set_data(i,6,entry[5])
                            ctx.gui_set_data(i,7,entry[6])
                            ctx.gui_set_data(i,8,entry[7])
                            ctx.gui_set_data(i,9,entry[8])
                            ctx.gui_set_data(i,10,fsname)
                            i+=1
            os.remove(filename)
    #print(db)

def convertdatabase(rr):
    db=ctx.sqlite_open("gui",True)
    conn=ctx.sqlite_run_cmd(db,"select rowid, timestamp, message_type, text, message, user_id from messages;")
    conn2=ctx.sqlite_run_cmd(db,"select thread_id, thread_info from threads;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    rows2=ctx.sqlite_get_data_size(conn2)[0]
    oldpos=0
    threads={}
    
    for i in range(0,rows2):
        newpos=int(i/rows2*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        thread_id=ctx.sqlite_get_data(conn2,i,0)
        thread_info=ctx.sqlite_get_data(conn2,i,1)
        details=json.loads(thread_info)
        
        if "recipients" in details:
            recipients=details["recipients"]
            users=""
            for u in recipients:
                if "username" in u:
                    username=u["username"]
                if "full_name" in u:
                    full_name=u["full_name"]
                users+=username+"[\""+full_name+"\"];"
            threads[thread_id]=users
        
    v=[]
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        s=ctx.sqlite_get_data(conn,i,4)
        data=json.loads(s)
        v.append(convertdata_new(data,threads))
      
    rows=len(v)
    for i in range(rr,rows+rr):
        oldpos=0
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        for entry in v[i]:
            ctx.gui_set_data(i,0,i)
            ctx.gui_set_data(i,1,entry[0])
            ctx.gui_set_data(i,2,entry[1])
            ctx.gui_set_data(i,3,entry[2])
            ctx.gui_set_data(i,4,entry[3])
            ctx.gui_set_data(i,5,entry[4])
            ctx.gui_set_data(i,6,entry[5])
            ctx.gui_set_data(i,7,entry[6])
            ctx.gui_set_data(i,8,entry[7])
            ctx.gui_set_data(i,9,entry[8])
    ctx.sqlite_close(db)

def main():
    ctx.gui_setMainLabel("Instagram: Parsing...");
    ctx.gui_setMainProgressBar(0)
    headers=["rowid (int)","thread_id (QString)", "thread_title (QString)","fromid (QString)","fromalias (QString)","toids (QString)","toaliases (QString)","timestamp (QString)", "text (QString)", "desc (QString)","Filename (QString)"]
    ctx.gui_set_headers(headers)
    filenames=ctx.pluginfilenames()
    print(filenames)
    try:
        if (filename==""):
            filename="direct.db"
    except:
        filename="direct.db"
    
    jsonfiles=[]
    rows=0
    for fname in filenames:
        if ".json".lower() in fname.lower():
            jsonfiles.append(fname)
        elif ".db" in fname.lower():
            convertdatabase(rows)
    
    if len(jsonfiles)!=0:
        convertjson(jsonfiles,rows)

    if "direct.db" in filename.lower():
        convertdatabase(rows)
        
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."