#Pluginname="WhatsApp (Apple)"
#Filename="ChatStorage.sqlite"
#Type=App

import struct
import tempfile
import shutil

def convertdata(db,rowids):
    headers=["rowid (int)","Timestamp (int)","Sent_Timestamp (int)","ZISFROMME (QString)","Contact (QString)","Contact_Alias (QString)","Group (QString)","Group_Alias (QString)","Message (QString)","ZSAVEDINPUT (QString)","ZXMPPTHUMBPATH (QString)","ZTITLE (QString)","ZTHUMBNAILLOCALPATH (QString)","ZVCARDSTRING (QString)","ZAUTHORNAME (QString)","ZMEDIAURLDATE (QString)","ZLATITUDE (QString)","ZLONGITUDE (QString)","ZMEDIAORIGIN (QString)","ZFILESIZE (QString)","ZMOVIEDURATION (QString)"]
    ctx.gui_set_headers(headers)
    
    ctx.gui_setMainLabel("Status: Converting whatsapp group contacts")
    groupcontact=ctx.sqlite_run_cmd(db,"SELECT Z_PK, ZCONTACTNAME, ZMEMBERJID FROM ZWAGROUPMEMBER;")
    rows_groupcontact=ctx.sqlite_get_data_size(groupcontact)[0]
    contacts={}
    oldpos=0
    for i in range(0,rows_groupcontact):
        newpos=int(i/rows_groupcontact*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=str(ctx.sqlite_get_data(groupcontact,i,0))
        name=ctx.sqlite_get_data(groupcontact,i,1)
        jid=ctx.sqlite_get_data(groupcontact,i,2)
        if id not in contacts:
            contacts[id]=[name,jid]
            contacts[jid]=[name,jid]
    ctx.sqlite_cmd_close(groupcontact)
    
    ctx.gui_setMainLabel("Status: Converting whatsapp contacts")
    contact=ctx.sqlite_run_cmd(db,"SELECT ZJID, ZPUSHNAME FROM ZWAPROFILEPUSHNAME;")
    rows_contact=ctx.sqlite_get_data_size(contact)[0]
    oldpos=0
    for i in range(0,rows_contact):
        newpos=int(i/rows_contact*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(contact,i,0)
        name=ctx.sqlite_get_data(contact,i,1)
        if id not in contacts:
            contacts[id]=[name,id]
    ctx.sqlite_cmd_close(contact)
    
    ctx.gui_setMainLabel("Status: Converting whatsapp group info contacts")
    gcontact=ctx.sqlite_run_cmd(db,"SELECT ZCONTACTJID, ZPARTNERNAME FROM ZWACHATSESSION;")
    rows_gcontact=ctx.sqlite_get_data_size(gcontact)[0]
    oldpos=0
    for i in range(0,rows_gcontact):
        newpos=int(i/rows_gcontact*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(gcontact,i,0)
        name=ctx.sqlite_get_data(gcontact,i,1)
        if id not in contacts:
            contacts[id]=[name,id]
    ctx.sqlite_cmd_close(gcontact)
    
    
    ctx.gui_setMainLabel("Status: Converting whatsapp media")
    media=ctx.sqlite_run_cmd(db,"SELECT ZWAMESSAGE.rowid, datetime(ZWAMESSAGE.ZMESSAGEDATE+978307200,'unixepoch','localtime'),  datetime(ZWAMESSAGE.ZSENTDATE+978307200,'unixepoch','localtime'), ZWAMESSAGE.ZFROMJID, ZWAMESSAGE.ZTOJID, ZWAMESSAGE.ZPUSHNAME, ZWAMESSAGE.ZTEXT, ZWAMESSAGE.ZGROUPMEMBER, ZWAMESSAGE.ZISFROMME, ZWAMEDIAITEM.ZXMPPTHUMBPATH, ZWAMEDIAITEM.ZTITLE, ZWAMEDIAITEM.ZTHUMBNAILLOCALPATH, ZWAMEDIAITEM.ZVCARDSTRING, ZWAMEDIAITEM.ZAUTHORNAME, datetime(ZWAMEDIAITEM.ZMEDIAURLDATE+978307200,'unixepoch','localtime'), ZWAMEDIAITEM.ZLATITUDE, ZWAMEDIAITEM.ZLONGITUDE, ZWAMEDIAITEM.ZMEDIAORIGIN, ZWAMEDIAITEM.ZFILESIZE, ZWAMEDIAITEM.ZMOVIEDURATION FROM ZWAMESSAGE, ZWAMEDIAITEM WHERE ZWAMESSAGE.ZMEDIAITEM=ZWAMEDIAITEM.Z_PK;")    
    rows_media=ctx.sqlite_get_data_size(media)[0]
    oldpos=0
    r=0
    results={}
    
    for i in range(0,rows_media):
        newpos=int(i/rows_media*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(media,i,0)
        if id not in rowids:
            data={}
            rowids.append(id)
            ZMESSAGEDATE=ctx.sqlite_get_data(media,i,1)
            ZSENTDATE=ctx.sqlite_get_data(media,i,2)
            ZFROMJID=ctx.sqlite_get_data(media,i,3)
            ZTOJID=ctx.sqlite_get_data(media,i,4)
            ZPUSHNAME=ctx.sqlite_get_data(media,i,5)
            ZTEXT=ctx.sqlite_get_data(media,i,6)
            ZGROUPMEMBER=str(ctx.sqlite_get_data(media,i,7))
            ZISFROMME=ctx.sqlite_get_data(media,i,8)
            
            ZXMPPTHUMBPATH=ctx.sqlite_get_data(media,i,9)
            ZTITLE=ctx.sqlite_get_data(media,i,10)
            ZTHUMBNAILLOCALPATH=ctx.sqlite_get_data(media,i,11)
            ZVCARDSTRING=ctx.sqlite_get_data(media,i,12)
            ZAUTHORNAME=ctx.sqlite_get_data(media,i,13)
            ZMEDIAURLDATE=ctx.sqlite_get_data(media,i,14)
            ZLATITUDE=ctx.sqlite_get_data(media,i,15)
            ZLONGITUDE=ctx.sqlite_get_data(media,i,16)
            ZMEDIAORIGIN=ctx.sqlite_get_data(media,i,17)
            ZFILESIZE=ctx.sqlite_get_data(media,i,18)
            ZMOVIEDURATION=ctx.sqlite_get_data(media,i,19)
            
            ZPARTNERNAME=""
            
            type=""
            if str(ZGROUPMEMBER) != "":
               type="Group"

            data[0]=id;
            data[1]=ZMESSAGEDATE;
            data[2]=ZSENTDATE;
            
            if (ZISFROMME==1):
                data[3]="Sent"
                #To
                data[4]=ZTOJID
                #To_Alias
                if ZTOJID in contacts:
                    data[5]=contacts[ZTOJID][0]
                else:
                    data[5]=""
            else:
                data[3]="Received"
                #From
                if type=="Group":
                  if ZGROUPMEMBER in contacts:
                    data[4]=contacts[ZGROUPMEMBER][1]
                  else:
                    data[4]="GROUPMEMBER:"+str(ZGROUPMEMBER)
                else:
                  data[4]=ZFROMJID
            
                #From_Alias
                if type=="Group":
                  if ZGROUPMEMBER in contacts:
                    data[5]=contacts[ZGROUPMEMBER][0]
                  else:
                    data[5]="GROUPMEMBER:"+str(ZGROUPMEMBER)
                else:
                  if ZFROMJID in contacts:
                    data[5]=contacts[ZFROMJID][0]
                  else:
                    data[5]=""

            #Group-ID and Alias
            if type=="Group":
              if ZFROMJID in contacts:
                data[6]=contacts[ZFROMJID][1]
                data[7]=contacts[ZFROMJID][0]
              else:
                data[6]=ZFROMJID
                data[7]=""
            else:
                data[6]=""
                data[7]=""
                
            data[8]=ZTEXT

            data[9]=""
            
            data[10]=ZXMPPTHUMBPATH
            data[11]=ZTITLE
            data[12]=ZTHUMBNAILLOCALPATH
            data[13]=ZVCARDSTRING
            data[14]=ZAUTHORNAME
            data[15]=ZMEDIAURLDATE
            data[16]=ZLATITUDE
            data[17]=ZLONGITUDE
            data[18]=ZMEDIAORIGIN
            data[19]=ZMOVIEDURATION
            results[r]=data
            r+=1
    ctx.sqlite_cmd_close(media)
    
    
    message=ctx.sqlite_run_cmd(db,"SELECT ZWAMESSAGE.rowid, datetime(ZWAMESSAGE.ZMESSAGEDATE+978307200,'unixepoch','localtime'), datetime(ZWAMESSAGE.ZSENTDATE+978307200,'unixepoch','localtime'), ZWAMESSAGE.ZFROMJID, ZWAMESSAGE.ZTOJID, ZWAMESSAGE.ZPUSHNAME, ZWAMESSAGE.ZTEXT, ZWAMESSAGE.ZGROUPMEMBER, ZWAMESSAGE.ZISFROMME, ZWACHATSESSION.ZPARTNERNAME, ZWACHATSESSION.ZSAVEDINPUT FROM ZWAMESSAGE, ZWACHATSESSION WHERE ZWAMESSAGE.ZCHATSESSION=ZWACHATSESSION.Z_PK;")
    rows_message=ctx.sqlite_get_data_size(message)[0]
    oldpos=0
    
    ctx.gui_setMainLabel("Status: Converting whatsapp message")
    for i in range(0,rows_message):
        newpos=int(i/rows_message*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(message,i,0)
        if id not in rowids:
            data={}
            rowids.append(id)
            ZMESSAGEDATE=ctx.sqlite_get_data(message,i,1)
            ZSENTDATE=ctx.sqlite_get_data(message,i,2)
            ZFROMJID=ctx.sqlite_get_data(message,i,3)
            ZTOJID=ctx.sqlite_get_data(message,i,4)
            ZPUSHNAME=ctx.sqlite_get_data(message,i,5)
            ZTEXT=ctx.sqlite_get_data(message,i,6)
            ZGROUPMEMBER=str(ctx.sqlite_get_data(message,i,7))
            ZISFROMME=ctx.sqlite_get_data(message,i,8)
            
            ZPARTNERNAME=ctx.sqlite_get_data(message,i,9)
            ZSAVEDINPUT=ctx.sqlite_get_data(message,i,10)
            
            type=""
            if str(ZGROUPMEMBER) != "":
               type="Group"

            data[0]=id;
            data[1]=ZMESSAGEDATE;
            data[2]=ZSENTDATE;
            
            if (ZISFROMME==1):
                data[3]="Sent"
                #To
                data[4]=ZTOJID
                #To_Alias
                if ZTOJID in contacts:
                    data[5]=contacts[ZTOJID][0]
                else:
                    data[5]=""
            else:
                data[3]="Received"
                #From
                if type=="Group":
                  if ZGROUPMEMBER in contacts:
                    data[4]=contacts[ZGROUPMEMBER][1]
                  else:
                    data[4]="GROUPMEMBER:"+str(ZGROUPMEMBER)
                else:
                  data[4]=ZFROMJID
            
                #From_Alias
                if type=="Group":
                  if ZGROUPMEMBER in contacts:
                    data[5]=contacts[ZGROUPMEMBER][0]
                  else:
                    data[5]="GROUPMEMBER:"+str(ZGROUPMEMBER)
                else:
                  if ZFROMJID in contacts:
                    data[5]=contacts[ZFROMJID][0]
                  else:
                    data[5]=""
            
            #Group-ID and Alias
            if type=="Group":
              if ZFROMJID in contacts:
                data[6]=contacts[ZFROMJID][1]
                data[7]=contacts[ZFROMJID][0]
              else:
                data[6]=ZFROMJID
                data[7]=""
            else:
                data[6]=""
                data[7]=""
                
            data[8]=ZTEXT
            
            data[9]=ZSAVEDINPUT
            
            data[10]=""
            data[11]=""
            data[12]=""
            data[13]=""
            data[14]=""
            data[15]=""
            data[16]=""
            data[17]=""
            data[18]=""
            data[19]=""
            results[r]=data
            r+=1
            
    ctx.sqlite_cmd_close(message)
    
    ctx.gui_setMainLabel("Status: Converting whatsapp results")
    r=0
    for i in range(0,len(results)):
        entry=results[i]
        ctx.gui_set_data(r,0,entry[0])
        ctx.gui_set_data(r,1,entry[1])
        ctx.gui_set_data(r,2,entry[2])
        ctx.gui_set_data(r,3,entry[3])
        ctx.gui_set_data(r,4,entry[4])
        ctx.gui_set_data(r,5,entry[5])
        ctx.gui_set_data(r,6,entry[6])
        ctx.gui_set_data(r,7,entry[7])
        ctx.gui_set_data(r,8,entry[8])
        ctx.gui_set_data(r,9,entry[9])
        ctx.gui_set_data(r,10,entry[10])
        ctx.gui_set_data(r,11,entry[11])
        ctx.gui_set_data(r,12,entry[12])
        ctx.gui_set_data(r,13,entry[13])
        ctx.gui_set_data(r,14,entry[14])
        ctx.gui_set_data(r,15,entry[15])
        ctx.gui_set_data(r,16,entry[16])
        ctx.gui_set_data(r,17,entry[17])
        ctx.gui_set_data(r,18,entry[18])
        ctx.gui_set_data(r,19,entry[19])
        r+=1
    return rowids


def main():
    ctx.gui_setMainLabel("WhatsApp: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)

    rowids=[]
    ctx.gui_setMainLabel("Status: Converting whatsapp chatstorage.sqlite")
    convertdata(db,rowids)
    ctx.sqlite_close(db)
    
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."