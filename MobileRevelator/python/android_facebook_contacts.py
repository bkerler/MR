#Pluginname="Facebook Contacts - Katana (Android)"
#Filename="contacts_db2"
#Type=App

import struct
import zlib
import json

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"SELECT rowid, added_time_ms, fbid, first_name, last_name, display_name, huge_picture_url FROM contacts;")
    if (conn!=-1):
        rows=ctx.sqlite_get_data_size(conn)[0]
        if rows==0:
            return
        oldpos=0
        t=0
        for i in range(0,rows):
            newpos=int(i/rows*100)
            if (oldpos<newpos):
                oldpos=newpos
                ctx.gui_setMainProgressBar(oldpos)
            id=ctx.sqlite_get_data(conn,i,0)
            added_time_ms=ctx.sqlite_get_data(conn,i,1)
            fbid=ctx.sqlite_get_data(conn,i,2)
            first_name=ctx.sqlite_get_data(conn,i,3)
            last_name=ctx.sqlite_get_data(conn,i,4)
            display_name=ctx.sqlite_get_data(conn,i,5)
            huge_picture_url=ctx.sqlite_get_data(conn,i,6)
            numbers=""
            ctx.gui_set_data(t,0,id)
            ctx.gui_set_data(t,1,added_time_ms)
            ctx.gui_set_data(t,2,fbid)
            ctx.gui_set_data(t,3,first_name)
            ctx.gui_set_data(t,4,last_name)
            ctx.gui_set_data(t,5,display_name)
            ctx.gui_set_data(t,6,huge_picture_url)
            ctx.gui_set_data(t,7,numbers)
            t+=1
            
    else:
        conn=ctx.sqlite_run_cmd(db,"select rowid, data from contacts;")
        if (conn==-1):
            print ("Error: "+ctx.sqlite_last_error(db))
            return
        rows=ctx.sqlite_get_data_size(conn)[0]
        if rows==0:
            return
        oldpos=0
        t=0
        for i in range(0,rows):
            newpos=int(i/rows*100)
            if (oldpos<newpos):
                oldpos=newpos
                ctx.gui_setMainProgressBar(oldpos)
            id=ctx.sqlite_get_data(conn,i,0)
            data=ctx.sqlite_get_data(conn,i,1)
            dat=json.loads(data)
            added_time_ms=""
            fbid=""
            first_name=""
            last_name=""
            display_name=""
            huge_picture_url=""
            numbers=""
            if "profileFbid" in dat:
                fbid=dat["profileFbid"]
            
            if "name" in dat:
                name=dat["name"]
                if "firstName" in name:
                    first_name=name["firstName"]
                if "lastName" in name:
                    last_name=name["lastName"]
                if "displayName" in name:
                    display_name=name["displayName"]
             
            if "hugePictureUrl" in dat:
                huge_picture_url=dat["hugePictureUrl"]
                
            if "phones" in dat:
                phones=dat["phones"]
                for i in range(0,len(phones)):
                    ph=phones[i]
                    if "universalNumber" in ph:
                        numbers=numbers+ph["universalNumber"]+";"
                

            if (fbid!=""):
                ctx.gui_set_data(t,0,id)
                ctx.gui_set_data(t,1,added_time_ms)
                ctx.gui_set_data(t,2,fbid)
                ctx.gui_set_data(t,3,first_name)
                ctx.gui_set_data(t,4,last_name)
                ctx.gui_set_data(t,5,display_name)
                ctx.gui_set_data(t,6,huge_picture_url)
                ctx.gui_set_data(t,7,numbers)
                t+=1
            
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","added_time_ms (int)","fbid (QString)","first_name (QString)","last_name (QString)","display_name (QString)","huge_picture_url (QString)","numbers (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Facebook Contacts: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."