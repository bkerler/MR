#Pluginname="Facebook Orca Calls (Android)"
#Filename="threads_db2"
#Type=App

import struct
import json

def converttime(val,db):
    conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
    res=ctx.sqlite_get_data(conn,0,0)
    ctx.sqlite_cmd_close(conn)
    return res

def convertdata(db):
    fbconn=ctx.sqlite_run_cmd(db,"SELECT fbid, display_name from fb.contacts;")
    if fbconn==-1:
        fbconn=ctx.sqlite_run_cmd(db,"SELECT user_key, name from thread_users;")
    contacts={}
    if fbconn!=-1:
      rows=ctx.sqlite_get_data_size(fbconn)[0]
      for i in range(0,rows):
          fbid=str(ctx.sqlite_get_data(fbconn,i,0))
          if (fbid.find("FACEBOOK")):
             if (len(fbid.split(":"))>1):
                fbid=fbid.split(":")[1]
          display_name=ctx.sqlite_get_data(fbconn,i,1)
          if (fbid not in contacts):
             if display_name != None:
                contacts[fbid]=display_name
    else:
         print ("Error: "+ctx.sqlite_last_error(db))
         return

    conn=ctx.sqlite_run_cmd(db,"SELECT messages.rowid, thread_key, timestamp_ms, sender, xma FROM messages;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    
    oldpos=0
    i2=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        threadkey=ctx.sqlite_get_data(conn,i,1)
        time=ctx.sqlite_get_data(conn,i,2)
        sender=ctx.sqlite_get_data(conn,i,3)
        xma=ctx.sqlite_get_data(conn,i,4)
        if "RTC_CALL" in xma:
            timestamp=converttime(time/1000,db)
            userid=""
            useralias=""
            toalias=""
            duration=0
            sdata=json.loads(sender)
            xdata=json.loads(xma)
            incoming=""
            if "user_key" in sdata:
                userid=sdata["user_key"]
            if "name" in sdata:
                useralias=sdata["name"]
            if threadkey.split(":")[1] in userid.split("FACEBOOK:")[1]:
                toid=threadkey.split(":")[2]
                incoming="1"
                #print(str(i)+":1:"+userid+"-"+toid+"\n")
            else:
                toid=threadkey.split(":")[1]
                incoming="0"
                #print(str(i)+":2:"+userid+"-"+toid+"\n")
            
            if toid in contacts:
                toalias=contacts[toid]
            else:
                toalias=""

            peerID=""
            senderID=""
            answered=""
            duration=0
            if "story_attachment" in xdata:
                if "attachment_properties" in xdata["story_attachment"]:
                    if "RTC_CALL_LOG" in xdata["story_attachment"]["style_list"]:
                        for i in range(0,len(xdata["story_attachment"]["attachment_properties"])):
                            style=""
                            d=xdata["story_attachment"]["attachment_properties"][i]
                            if ("key" in d) and ("value" in d):
                                key=d["key"]
                                value=str(d["value"]["text"])
                                if key=="answered":
                                    answered=value
                                if key=="duration":
                                    duration=int(value)
                                        
                        ctx.gui_set_data(i2,0,id)
                        if (incoming=="1"):
                            ctx.gui_set_data(i2,1,userid)
                            ctx.gui_set_data(i2,2,useralias)
                        else:
                            ctx.gui_set_data(i2,1,"FACEBOOK:"+toid)
                            ctx.gui_set_data(i2,2,toalias)
                        ctx.gui_set_data(i2,3,incoming)
                        ctx.gui_set_data(i2,4,answered)
                        ctx.gui_set_data(i2,5,duration)
                        ctx.gui_set_data(i2,6,timestamp)
                        i2+=1
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","contactID (QString)","contactAlias (QString)","incoming (QString)","answered (QString)","duration (int)","timestamp (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Facebook Orca RTC Calls: Parsing data");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."