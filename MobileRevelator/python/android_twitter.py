#Pluginname="Twitter (Android)"
#Filename="-*.db"
#Type=App

import os
from enum import Enum
import struct

class datatypes(Enum):
    byte = 1
    integer = 2
    long = 3
    float= 4
    double = 5
    bool = 6
    null = 7
    string1 = 8
    start = 9
    object_2 = 0xA
    end = 0xB
    string2 = 0xD
    bytearray = 0xE

class tag:
    type=0
    value=0
    string=""
    def __init__(self,tg,vv,st):
        self.type=tg
        self.value=vv
        self.string=st

class twitterserialize:

    def __init__(self,input):
        self.pos=0
        self.data=input

    def rshift(self,val, n):
        s = val & 0x80000000
        for i in range(0,n):
            val >>= 1
            val |= s
        return val

    def getTagType(self,buffer):
        return (buffer >> 3) & 31

    def getTagLength(self,buffer):
        taglength=buffer & 7
        if (taglength==0 or taglength==1):
            return 0
        elif (taglength==2):
            return 1
        elif (taglength==3):
            return 2
        elif (taglength==5):
            return 8
        else:
            return 4

    def readByte(self):
        buffer=0
        try:
            buffer = int(struct.unpack('<B', self.data[self.pos:self.pos + 1])[0])
            self.pos += 1
        except:
            buffer=0
        return buffer

    def readTag(self):
        buffer=self.readByte()
        if (buffer==0x19):
            while (1):
                buffer = self.readByte()
                if (buffer==0):
                    break
                if (buffer==int(0x6A)):
                    break
                if (buffer==int(0x4A)):
                    break
        type=self.getTagType(buffer)
        length=self.getTagLength(buffer)
        value=0
        string=""
        if (type==4):
            length=8
        if (type==7):
            value=0
            length=0
            self.pos+=1
        if (length == 1):
            value=(self.readByte())
        elif (length == 2):
            value=(self.readShort())
        elif (length == 4):
            value=(self.readLong())
        elif (length == 8):
            value = (self.readLongLong())
        else:
            value=length
        if (type == datatypes.string1.value):
            string=self.readString(value-1)
            self.pos += value+2
        elif (type == datatypes.string2.value):
            string = self.readString(value)
            self.pos += value

        return tag(type,value,string)

    def readString(self,strlen):
        try:
            msg = self.data[self.pos:self.pos+strlen].decode('utf8')
        except:
            msg=""
        return msg

    def readShort(self):
        value=int(struct.unpack('<H', self.data[self.pos:self.pos + 2])[0])
        self.pos+=2
        return value

    def readLong(self):
        value=int(struct.unpack('<I', self.data[self.pos:self.pos + 4])[0])
        self.pos+=4
        return value

    def readLongLong(self):
        value=int(struct.unpack('<Q', self.data[self.pos:self.pos + 8])[0])
        self.pos+=8
        return value

    def parsearray(self,tag):
        array=[]
        while (tag.type != datatypes.end.value and self.pos<len(self.data)-1):
            tag = self.readTag()
            if (tag.type == datatypes.string1.value or tag.type == datatypes.string2.value):
                array.append(tag.string)
            elif tag.type!=datatypes.start.value and tag.type!=datatypes.end.value:
                array.append(tag.value)

            if (tag.type == datatypes.start.value):
                array+=self.parsearray(tag)
        return array
        
    def parsestrings(self,tag):
        array=[]
        while (tag.type != datatypes.end.value and self.pos<len(self.data)-1):
            tag = self.readTag()
            if (tag.type == datatypes.string1.value or tag.type == datatypes.string2.value):
                array.append(tag.string)
            if (tag.type == datatypes.start.value):
                array+=self.parsestrings(tag)
        return array

    def parse(self):
        str=""
        data=[]
        tag=self.readTag()
        if (tag.type==datatypes.start.value):
            data=self.parsearray(tag)
        return data

    def parsestr(self):
        str=""
        data=[]
        tag=self.readTag()
        if (tag.type==datatypes.start.value):
            data=self.parsestrings(tag)
        return data

        '''
        select conversation_entries.rowid, users.username, users.name, conversation_entries.created, conversation_entries.data, conversation_participants.user_id from conversation_entries LEFT OUTER JOIN users ON users.user_id = conversation_entries.user_id LEFT OUTER JOIN conversation_participants ON conversation_entries.conversation_id=conversation_participants.conversation_id GROUP BY conversation_entries.created;
        '''
    
def convertmessages(db,row):
    conn=ctx.sqlite_run_cmd(db,"select conversation_participants.conversation_id, conversation_participants.user_id, users.username, users.name from conversation_participants OUTER LEFT JOIN users ON conversation_participants.user_id=users.user_id;")
    if (conn==-1):
         #print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    users={}
    for i in range(0,rows):
        convid=ctx.sqlite_get_data(conn,i,0)
        username=ctx.sqlite_get_data(conn,i,2)
        name=ctx.sqlite_get_data(conn,i,3)
        if not convid in users:
            users[str(convid)]=[]
        users[str(convid)].append([username,name])
    ctx.sqlite_cmd_close(conn)
    
    conn=ctx.sqlite_run_cmd(db,"select conversation_entries.rowid, users.username, users.name, conversation_entries.created, conversation_entries.data, conversation_entries.conversation_id from conversation_entries LEFT OUTER JOIN users ON users.user_id = conversation_entries.user_id;")
    if (conn==-1):
         #print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    print("Running twitter status conversion")
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
        id=ctx.sqlite_get_data(conn,i,0)
        #print(id)
        username=ctx.sqlite_get_data(conn,i,1)
        name=ctx.sqlite_get_data(conn,i,2)
        created=ctx.sqlite_get_data(conn,i,3)
        content=bytearray(ctx.sqlite_get_data(conn,i,4).data())
        serial=twitterserialize(content)
        content=serial.parsestr()
        message=content[0]
        conversation_id=ctx.sqlite_get_data(conn,i,5)
        toname=''
        tousername=''
        if str(conversation_id) in users:
            for x in users[conversation_id]:
                if name!=x[1]:
                    toname=x[0]
                    tousername=x[1]
                    break

        ctx.gui_set_data(row,0,id)
        ctx.gui_set_data(row,1,username)
        ctx.gui_set_data(row,2,name)
        ctx.gui_set_data(row,3,toname)
        ctx.gui_set_data(row,4,tousername)
        ctx.gui_set_data(row,5,created)
        ctx.gui_set_data(row,6,message)
        ctx.gui_set_data(row,7,'')
        ctx.gui_set_data(row,8,'')
        ctx.gui_set_data(row,9,'')
        ctx.gui_set_data(row,10,'Message')
        row+=1
        
    ctx.sqlite_cmd_close(conn)
    return row
    
def convertstatuses(db, row):
    conn=ctx.sqlite_run_cmd(db,"select statuses.rowid, users.username, users.name, statuses.in_r_screen_name as 'receiver', statuses.created, statuses.content, statuses.source, statuses.latitude, statuses.longitude, statuses.place_data, statuses.quoted_tweet_data from statuses OUTER LEFT JOIN users ON users.user_id = statuses.author_id;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    print("Running twitter status conversion")
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
        id=ctx.sqlite_get_data(conn,i,0)
        #print(id)
        username=ctx.sqlite_get_data(conn,i,1)
        name=ctx.sqlite_get_data(conn,i,2)
        receiver=ctx.sqlite_get_data(conn,i,3)
        created=ctx.sqlite_get_data(conn,i,4)
        message=""
        try:
           content=bytearray(ctx.sqlite_get_data(conn,i,5).data())
           serial=twitterserialize(content)
           content=serial.parse()
           message=content[0]
        except:
           content=str(ctx.sqlite_get_data(conn,i,5))
           message=content
        
        source=ctx.sqlite_get_data(conn,i,6)
        if source=="Twitter Ads":
            continue
        latitude=ctx.sqlite_get_data(conn,i,7)
        longitude=ctx.sqlite_get_data(conn,i,8)
        place_data=ctx.sqlite_get_data(conn,i,9)
        ctx.gui_set_data(row,0,id)
        ctx.gui_set_data(row,1,username)
        ctx.gui_set_data(row,2,name)
        ctx.gui_set_data(row,3,'')
        ctx.gui_set_data(row,4,'')
        ctx.gui_set_data(row,5,created)
        ctx.gui_set_data(row,6,message)
        ctx.gui_set_data(row,7,source)
        ctx.gui_set_data(row,8,latitude)
        ctx.gui_set_data(row,9,longitude)
        ctx.gui_set_data(row,10,'Timeline')
        row+=1
        
    ctx.sqlite_cmd_close(conn)
    return row
    
def main():
    headers=["rowid (int)","From_Username (QString)","From_Name (QString)","To_Username (QString)","To_Name (QString)","Created (int)","Message (QString)","Source (QString)","Latitude (QString)","Longitude (QString)", "Type (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Twitter: Parsing data");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    row=0
    row=convertstatuses(db,row)
    row=convertmessages(db,row)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."
    