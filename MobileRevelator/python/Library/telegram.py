# - added Telegram 3.7.0 (01.06.2016)
from datetime import datetime
from Library.java import JavaFunc

class Telegram(object):
    def __init__(self,tdata,mdata,tusertable,tchattable):
        self.textdata=tdata
        self.data=None
        self.mediadata=mdata
        self.usertable=tusertable
        self.chattable=tchattable
        return

    def getDate(self,value):
        dt=datetime.fromtimestamp(value)
        return dt.strftime("%d.%m.%Y %H:%M:%S")
        #return str(value)
        
    class TelegramPhoto:
        TL_photo={
            "TL_photo":0x9288DD29,
            "TL_photo_layer55":0xCDED42FE,
            "TL_photo_old":0x22B56751,
            "TL_photo_old2":0xC3838076,
            "TL_photoEmpty":0x2331B22D
        }

    def getphoto(self,value):
        for key in self.TelegramPhoto.TL_photo.keys():
            if self.TelegramPhoto.TL_photo[key]==value:
                return key
        return ""

    class TelegramSendMessageAction:
        TL_SendMessageAction={
            "TL_sendMessageGeoLocationAction":0x176F8BA1,
            "TL_sendMessageChooseContactAction":0x628CBC6F,
            "TL_sendMessageRecordRoundAction":0x88F27FBC,
            "TL_sendMessageUploadDocumentAction_old":0x8FAEE98E,
            "TL_sendMessageUploadVideoAction_old":0x92042FF7,
            "TL_sendMessageUploadPhotoAction_old":0x990A3C1A,
            "TL_sendMessageRecordVideoAction":0xA187D66F,
            "TL_sendMessageUploadDocumentAction":0xAA0CD9E4,
            "TL_sendMessageUploadPhotoAction":0xD1D34A26,
            "TL_sendMessageRecordAudioAction":0xD52F73F7,
            "TL_sendMessageGamePlayAction":0xDD6A8F48,
            "TL_sendMessageUploadAudioAction_old":0xE6AC8A6F,
            "TL_sendMessageUploadVideoAction":0xE9763AEC,
            "TL_sendMessageUploadAudioAction":0xF351D7AB,
            "TL_sendMessageCancelAction":0xFD5EC8F5,
            "TL_sendMessageTypingAction":0x16BF744E,
            "TL_sendMessageUploadRoundAction":0x243E1C66
        }

    def getsendmessage(self,value):
        for key in self.TelegramSendMessageAction.TL_SendMessageAction.keys():
            if self.TelegramSendMessageAction.TL_SendMessageAction[key]==value:
                return key
        return ""
        
    class TelegramTypes:
      TL_message={
        "TL_message_layer72":0x90DDDC11,
        "TL_message_old6":0x2BEBFA86,
        "TL_message_secret_old":0x555555f8,
        "TL_message_secret_layer72":0x555555f9, 
        "TL_message_secret":0x555555fa, 
        "TL_message_old7":0x5ba66c13,
        "TL_messageEmpty":0x83E5DE54,
        "TL_messageService":0x9E19A1F6, 
        "TL_messageService_old":0x9F8D60BB,
        "TL_messageForwarded_old2":0xA367E716,
        "TL_message_old3":0xA7AB1991,
        "TL_messageService_layer48":0xc06b9607,
        "TL_message_layer68":0xC09BE45F,
        "TL_message_old4":0xC3060325,
        "TL_message_layer47":0xC992E15C,
        "TL_message_old5":0xF07814C8,
        "TL_messageForwarded_old":0x5F46804,
        "TL_messageService_old2":0x1D86F70E,
        "TL_message_old":0x22EB6ABA,
        "TL_message_old2":0x567699B3,
        "TL_message":0x44F9B43D
        }

    def getmessage(self,value):
        for key in self.TelegramTypes.TL_message.keys():
            if self.TelegramTypes.TL_message[key]==value:
                return key
        return hex(value)

    class TelegramFlags:
        MESSAGE_FLAG_UNREAD = 1
        MESSAGE_FLAG_OUT = 2
        MESSAGE_FLAG_TRUE = 0x997275b5
        MESSAGE_FLAG_FALSE = 0xbc799737

    class TelegramMedia:
     TL_media={
        "TL_messageMediaDocument_layer68":0xF3E02EA8,
        "TL_messageMediaGame" : 0xFDB19008,
        "TL_messageMediaUnsupported_old" : 0x29632a36,
        "TL_messageMediaDocument_old" : 0x2fda2204,
        "TL_messageMediaPhoto_layer68" : 0x3D8CE53D,
        "TL_messageMediaEmpty" : 0x3ded6320,
        "TL_messageMediaGeo"   : 0x56e0d474,
        "TL_messageMediaVideo_layer45" : 0x5BCF1675,
        "TL_messageMediaContact" : 0x5e7d2f39,
        "TL_messageMediaVenue" : 0x2EC0533F,
        "TL_messageMediaDocument_layer74":0x7C4414D3,
        "TL_messageMediaDocument" : 0x9CB070D7,
        "TL_messageMediaInvoice":0x84551347,
        "TL_messageMediaUnsupported" : 0x9F84F49E,
        "TL_messageMediaVideo_old" : 0xa2d24290,
        "TL_messageMediaWebPage" : 0xA32DD600,
        "TL_messageMediaPhoto_layer74" : 0xB5223B0F,
        "TL_messageMediaAudio_layer45" : 0xc6b68300,
        "TL_messageMediaPhoto_old" : 0xc8c45a2a,
        "TL_messageMediaVenue_layer71" : 0x7912B71F,
        "TL_messageMediaGeoLive" : 0x7C3C2609,
        "TL_messageMediaPhoto" : 0x695150D7
    }

    def getmedia(self,value):
        for key in self.TelegramMedia.TL_media.keys():
            if self.TelegramMedia.TL_media[key]==value:
                return key
        return hex(value)

    class TelegramMessageEntity:
        MessageEntity={
            "TL_messageEntityMention":0xFA04579D,
            "TL_messageEntityCode":0x28A20571,
            "TL_messageEntityEmail":0x64E475C2,
            "TL_messageEntityBotCommand":0x6CEF8AC7,
            "TL_messageEntityUrl":0x6ED02538,
            "TL_messageEntityHashtag":0x6F635B0D,
            "TL_messageEntityPre":0x73924BE0,
            "TL_messageEntityTextUrl":0x76A6D327,
            "TL_messageEntityItalic":0x826F8B60,
            "TL_messageEntityUnknown":0xBB92BA95,
            "TL_messageEntityBold":0xBD610BC9
        }

    def getmessageentity(self,value):
        for key in self.TelegramMessageEntity.MessageEntity.keys():
            if self.TelegramMessageEntity.MessageEntity[key]==value:
                return key
        return ""

    class TelegramUserSelf:
        TL_userSelf_old = 0x720535EC
        TL_userSelf_old3 = 0x1C60E608
        TL_userSelf_old2 = 0x7007B451
        TL_userRequest_old = 0x22E8CEB0
        TL_userRequest_old2 = 0xD9CCC4EF

    def telegramflag(self,flag):
        flags=""
        if ((flag&1)==self.TelegramFlags.MESSAGE_FLAG_UNREAD):
                    flags="UNREAD";
        if ((flag&2)==self.TelegramFlags.MESSAGE_FLAG_OUT):
            if (flags==""):
                    flags="OUT"
            else:
                    flags+=",OUT"
        return flags

    def TL_geoPoint(self):
        long=self.data.getdouble()
        lat=self.data.getdouble()
        return "Lon: "+str(long)+" Lat: "+str(lat)

    def GeoPoint(self):
        type=self.data.readInt32()
        if (type==0x1117DD5F):
            return ""
        elif (type==0x2049D70C):
            return TL_geoPoint()

    def TL_fileLocation(self):
        dc_id = self.data.readInt32();
        volume_id = self.data.readInt64();
        local_id = self.data.readInt32();
        secret = self.data.readInt64();
        return "FileLoc[Local_ID:"+str(local_id)+"]"

    def TL_fileEncryptedLocation(self):
        dc_id = self.data.readInt32()
        volume_id = self.data.readInt64()
        local_id = self.data.readInt32()
        secret = self.data.readInt64()
        key = self.data.readByteArray()
        iv = self.data.readByteArray()
        msg="FileEncLoc[Local_ID:"+str(local_id)+";"
        msg+="Key: "+key+";"
        msg+="IV: "+iv+";"
        msg+="]"
        return msg

    def TL_fileLocationUnavailable(self):
        volume_id = self.data.readInt64()
        local_id = self.data.readInt32()
        secret = self.data.readInt64()
        return "FileUnavail[Local_ID:"+str(local_id)+" ]"

    def FileLocation(self):
        type=self.data.readInt32()
        if (type==0x53D69076):
            return self.TL_fileLocation()
        elif (type==0x55555554):
            return self.TL_fileEncryptedLocation()
        elif (type==0x7C596B46):
            return self.TL_fileLocationUnavailable()
        return "FileLocation: Data error: "+hex(type)

    def TL_photoSize(self):
        type=self.data.readString()
        location=self.FileLocation()
        w=self.data.readInt32()
        h=self.data.readInt32()
        size=self.data.readInt32()
        msg="TL_photosize - ["
        msg+="Type:"+type+" "
        msg+=location
        msg+=" Width: "+str(w)
        msg+=" Height: "+str(h)
        msg+=" Size: "+str(size)
        return msg

    def TL_photoCachedSize(self):
        type=self.data.readString()
        location=self.FileLocation()
        w=self.data.readInt32()
        h=self.data.readInt32()
        bytes=self.data.readByteArray()
        return "TL_photoCachedSize - [Type:"+type+" "+location+" Width: "+str(w)+" Height: "+str(h)+" Bytes: "+bytes

    def PhotoSize(self):
        type=self.data.readInt32()
        if (type==0x77BFB61B):
            return self.TL_photoSize()
        elif (type==0xE9A734FA):
            return self.TL_photoCachedSize()
        elif (type==0x0E17E23C):
            return "Empty"

        return "Unknown PhotoSize: "+hex(type)

    def TL_photo_layer55(self):
        msg="TL_photo_layer55 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        #user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        v2=self.data.readInt32()
        inf=""
        count=0
        if (v2==0x1CB5C415):
            count=self.data.readInt32()
            i=0
            for sub in range(count):
                inf+="Item "+str(i)+":"+self.PhotoSize()+" "
                i+=1
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        #msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        if (count!=0):
            msg+="Itemcount: "+hex(count)
            msg+="["+inf+"]"
        return msg

    def TL_photo(self):
        msg="TL_photo - "
        flags=self.data.readInt32()
        has_stickers="False"
        if (flags&1)!=0:
            has_stickers="True"
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        v2=self.data.readInt32()
        inf=""
        count=0
        if (v2==0x1CB5C415):
            count=self.data.readInt32()
            i=0
            for sub in range(count):
                inf+="Item "+str(i)+":"+self.PhotoSize()+" "
                i+=1
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Has Stickers: "+has_stickers+";"
        msg+="Date: "+date+";"
        if (count!=0):
            msg+="Itemcount: "+hex(count)
            msg+="["+inf+"]"
        return msg
        
    def TL_photo_old(self):
        msg="TL_photo_old - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        caption=self.data.readString()
        geo=self.GeoPoint()
        np=self.data.readInt32()
        items=self.data.readInt32()
        inf=""
        for i in range(items):
            inf+="Item "+str(i)+":"+self.PhotoSize()+" "
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Caption: "+caption+";"
        if (geo!=""):
            msg+="Geo: "+geo+";"
        if (items!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        return msg

    def TL_photo_old2(self):
        msg="TL_photo_old2 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        geo=self.GeoPoint()
        subtype=self.data.readInt32()
        inf=""
        items=0
        if (subtype == 0x1CB5C415):
            items=self.data.readInt32()
            for i in range(items):
                inf+="Item "+str(i)+":"+self.PhotoSize()+" "

        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        if (geo!=""):
            msg+="Geo: "+geo+";"
        if (items!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        return msg

    def Photo(self):
        subtype=self.data.readInt32()
        type=self.getphoto(subtype)
        if (type=="TL_photo"):
            return self.TL_photo()
        elif (type=="TL_photo_old"):
            return self.TL_photo_old()
        elif (type=="TL_photo_old2"):
            return self.TL_photo_old2()
        elif (type=="TL_photoEmpty"):
            return "Photo: Empty"
        elif (type=="TL_photo_layer55"):
            return self.TL_photo_layer55()
        print("[Unknown Photo : "+hex(subtype)+"]")
        return ""

    def TL_messageMediaPhoto_old(self):
        photo="Photo:"+self.Photo()
        return photo

    def TL_messageMediaPhoto_layer68(self):
        photo="Photo:"+self.Photo()
        caption="Caption:"+self.data.readString()
        return caption+photo
        
    def TL_messageMediaPhoto_layer74(self):
        flags=self.data.readInt32()
        photo=""
        caption=""
        ttl_seconds=""
        if (flags&1)!=0:
            photo=self.Photo()
        else:
            return "Photo: Empty"
        if (flags&2)!=0:
            caption="Caption:\""+self.data.readString()+"\";"
        if (flags&4)!=0:
            ttl_seconds="Set_TTL_Seconds:"+str(self.data.readInt32())+";"
        return photo+";"+caption+ttl_seconds

    def TL_messageMediaPhoto(self):
        flags=self.data.readInt32()
        photo=""
        ttl_seconds=""
        if (flags&1)!=0:
            photo=self.Photo()
        else:
            return "Photo: Empty"
        if (flags&4)!=0:
            ttl_seconds="TTL_Seconds:"+str(self.data.readInt32())+";"
        return photo+";"+ttl_seconds
        
    def TL_game(self):
        msg="TL_game - "
        flags=self.data.readInt32()
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        short_name=self.data.readString()
        title=self.data.readString()
        description=self.data.readString()
        photo=self.Photo();
        document=""
        if ((flags&1)!=0):
            document=self.Document()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Short_Name: "+short_name+";"
        msg+="Title: "+title+";"
        msg+="Description: "+description+";"
        msg+="[Photo: "+photo+"];"
        msg+="[Document: "+document+"];"
        return msg

    def TL_messageMediaGame(self):
        subtype=self.data.readInt32() #0xBDF9653B
        return self.TL_game();

    def TL_messageMediaContact(self):
        phone_number = self.data.readString()
        first_name = self.data.readString()
        last_name = self.data.readString()
        user_id = self.data.readInt32()
        return "Contact [Number: "+phone_number+";First name: "+first_name+";Last name: "+last_name+";User ID: "+self.gettelegramuser(user_id)+"]"

    def TL_audio_layer45(self):
        msg="TL_audio_layer45 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        duration=self.data.readInt32()
        mime_type=self.data.readString()
        size=self.data.readInt32()
        dc_id=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Date: "+date+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Mime_Type: "+str(mime_type)+";"
        msg+="Size: "+str(size)+";"
        return msg

    def TL_audio_old2(self):
        msg="TL_audio_old2 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        duration=self.data.readInt32()
        mime_type=self.data.readString()
        size=self.data.readInt32()
        dc_id=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Mime_Type: "+str(mime_type)+";"
        msg+="Size: "+str(size)+";"
        return msg

    def TL_audio_old(self):
        msg="TL_audio_old - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        duration=self.data.readInt32()
        size=self.data.readInt32()
        dc_id=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Size: "+str(size)+";"
        return msg

    def TL_audioEncrypted(self):
        msg="TL_audioEncrypted - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        duration=self.data.readInt32()
        size=self.data.readInt32()
        dc_id=self.data.readInt32()
        key=self.data.readByteArray();
        iv=self.data.readByteArray();
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_Id: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Size: "+str(size)+";"
        msg+="Key: "+key+";"
        msg+="IV: "+iv+";"
        return msg

    class TelegramChat:
        TChat={
            "TL_chatForbidden_old":0xFB0CCC41,
            "TL_chatForbidden":0x7328BDB,
            "TL_channel":0xCB44B1C,
            "TL_channelForbidden":0x289DA732,
            "TL_channelForbidden_layer52":0x2D85832C,
            "TL_channel_layer48":0x4B1B7506,
            "TL_channel_old":0x678E9587,
            "TL_chat_old":0x6E9C9BC7,
            "TL_chat_old2":0x7312BC48,
            "TL_geoChat":0x75EAEA5A,
            "TL_channelForbidden_layer67":0x8537784F,
            "TL_chatEmpty":0x9BA2D800,
            "TL_channel_layer67":0xA14DCA52,
            "TL_chat":0xD91CDD54
        }

    def getchat(self,value):
        for key in self.TelegramChat.TChat.keys():
            if self.TelegramChat.TChat[key]==value:
                return key
        return ""

    def TL_chatForbidden_old(self):
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:\""+self.data.readString()+";"
        date="Date:"+self.getDate(self.data.readInt32())+";"
        return "chatForbidden_old ["+id+title+date+"]"

    def TL_chatForbidden(self):
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:\""+self.data.readString()+";"
        return "chatForbidden ["+id+title+"]"

    def TL_channelForbidden(self):
        flags=self.data.readInt32()
        broadcast="Broadcast:"
        if (flags&0x20)!=0:
            broadcast+="True"
        else:
            broadcast+="False"
        broadcast+=";"
        megagroup="Megagroup:"
        if (flags&0x100)!=0:
            megagroup+="True"
        else:
            megagroup+="False"
        megagroup+=";"
        
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        until_date=""
        if (flags&0x10000)!=0:
            until_date="Until_Date:"+self.getDate(self.data.readInt32())+";"
        return "channelForbidden ["+broadcast+megagroup+id+access_hash+title+until_date+"]"

    def TL_channelForbidden_layer67(self):
        flags=self.data.readInt32()
        broadcast="Broadcast:"
        if (flags&0x20)!=0:
            broadcast+="True"
        else:
            broadcast+="False"
        broadcast+=";"
        megagroup="Megagroup:"
        if (flags&0x100)!=0:
            megagroup+="True"
        else:
            megagroup+="False"
        megagroup+=";"
        
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        return "channelForbidden_layer67 ["+broadcast+megagroup+id+access_hash+title+"]"
        
    def TL_channelForbidden_layer52(self):
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        return "channelForbidden_layer52 ["+id+access_hash+title+"]"

    def returnfl(self,val,title):
        tmp=title+":"
        if (flags&val)!=0:
            tmp+="True"
        else:
            tmp+="False"
        tmp+=";"
        return tmp
    
    def TL_chatPhoto(self):
        photo_small="Photo_Small:"+self.FileLocation()+";"
        photo_big="Photo_Big:"+self.FileLocation()+";"
        return "ChatPhoto ["+photo_small+photo_big+"]"
        
    def ChatPhoto(self):
        type=self.data.readInt32()
        if (type==0x37C1011C):
            return "Photo: Empty"
        elif (type==0x6153276A):
            return self.TL_chatPhoto()
        else:
            return "ChatPhoto [Unknown type:"+hex(type)+"]"
        
    def TL_channel_layer48(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        kicked=self.returnfl(2,"Kicked")
        left=self.returnfl(4,"Left")
        moderator=self.returnfl(0x10,"Moderator")
        broadcast=self.returnfl(0x20,"Broadcast")
        verified=self.returnfl(0x80,"Verified")
        megagroup=self.returnfl(0x100,"Megagroup")
        restricted=self.returnfl(0x200,"Restricted")
        democracy=self.returnfl(0x400,"Democracy")
        signatures=self.returnfl(0x800,"Signatures")
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        username=""
        if (flags&0x40)!=0:
            username="Username:\""+self.data.readString()+"\";"
        photo=self.ChatPhoto()
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        restriction_reason=""
        if (flags&0x200)!=0:
            restriction_reason="Restriction_Reason:\""+self.data.readString()+"\";"
        return "Channel_layer48 ["+creator+kicked+left+moderator+broadcast+verified+megagroup+restricted+democracy+signatures+id+access_hash+title+username+photo+date+version+restriction_reason+"]"

    def TL_channel(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        left=self.returnfl(4,"Left")
        broadcast=self.returnfl(0x20,"Broadcast")
        verified=self.returnfl(0x80,"Verified")
        megagroup=self.returnfl(0x100,"Megagroup")
        restricted=self.returnfl(0x200,"Restricted")
        democracy=self.returnfl(0x400,"Democracy")
        signatures=self.returnfl(0x800,"Signatures")
        min=self.returnfl(0x1000,"Min")
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        username=""
        if (flags&0x40)!=0:
            username="Username:\""+self.data.readString()+"\";"
        photo=self.ChatPhoto()
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        restriction_reason=""
        if (flags&0x200)!=0:
            restriction_reason="Restriction_Reason:\""+self.data.readString()+"\";"
        admin_rights=""
        if (flags&0x4000)!=0:
            admin_rights="Admin_Rights:\""+self.data.readString()+"\";"
        banned_rights=""
        if (flags&0x8000)!=0:
            banned_rights="Banned_Rights:\""+self.data.readString()+"\";"
        return "Channel ["+creator+left+broadcast+verified+megagroup+restricted+democracy+signatures+min+id+access_hash+title+username+photo+date+version+restriction_reason+admin_rights+banned_rights+"]"

    def TL_channel_layer67(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        kicked=self.returnfl(2,"Kicked")
        left=self.returnfl(4,"Left")
        moderator=self.returnfl(0x10,"Moderator")
        broadcast=self.returnfl(0x20,"Broadcast")
        verified=self.returnfl(0x80,"Verified")
        megagroup=self.returnfl(0x100,"Megagroup")
        restricted=self.returnfl(0x200,"Restricted")
        democracy=self.returnfl(0x400,"Democracy")
        signatures=self.returnfl(0x800,"Signatures")
        min=self.returnfl(0x1000,"Min")
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        username=""
        if (flags&0x40)!=0:
            username="Username:\""+self.data.readString()+"\";"
        photo=self.ChatPhoto()
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        restriction_reason=""
        if (flags&0x200)!=0:
            restriction_reason="Restriction_Reason:\""+self.data.readString()+"\";"
        return "Channel_layer67 ["+creator+kicked+left+moderator+broadcast+verified+megagroup+restricted+democracy+signatures+min+id+access_hash+title+username+photo+date+version+restriction_reason+"]"
        
    def TL_channel_old(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        kicked=self.returnfl(2,"Kicked")
        left=self.returnfl(4,"Left")
        moderator=self.returnfl(0x10,"Moderator")
        broadcast=self.returnfl(0x20,"Broadcast")
        verified=self.returnfl(0x80,"Verified")
        megagroup=self.returnfl(0x100,"Megagroup")
        explicit=self.returnfl(0x200,"Explicit_Content")
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        username=""
        if (flags&0x40)!=0:
            username="Username:\""+self.data.readString()+"\";"
        photo=self.ChatPhoto()
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        return "Channel_old ["+creator+kicked+left+moderator+broadcast+verified+megagroup+explicit+id+access_hash+title+username+photo+date+version+"]"
        
    def TL_chat_old(self):
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:\""+self.data.readString()+";"
        photo=self.ChatPhoto()
        participants_count="Participants_Count:"+str(self.data.readInt32())+";"
        date="Date:"+self.getDate(self.data.readInt32())+";"
        left="Left:"+self.data.readBool()+";"
        version="Version:"+str(self.data.readInt32())+";"
        return "Chat_old ["+id+title+photo+date+left+version+"]"

    def TL_inputChannel(self):
        channel_id="Channel_ID:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        return "InputChannel ["+channel_id+access_hash+"]"
        
    def InputChannel(self):
        type=self.data.readInt32()
        if (type==0xAFEB712E):
            return self.TL_inputChannel()
        elif (type==0xEE8C1E86):
            return ""
        else:
            return "InputChannel [Unknown type:"+hex(type)+"]"
        
    def TL_chat(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        kicked=self.returnfl(2,"Kicked")
        left=self.returnfl(4,"Left")
        admins_enabled=self.returnfl(0x8,"Admins_Enabled")
        admin=self.returnfl(0x10,"Admin")
        deactivated=self.returnfl(0x20,"Deactivated")
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:\""+self.data.readString()+";"
        photo=self.ChatPhoto()
        participants_count="Participants_Count:"+str(self.data.readInt32())+";"
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        migrated_to=""
        if (flags&0x40)!=0:
            migrated_to=self.InputChannel()
        return "Chat_old2 ["+creator+kicked+left+admins_enabled+admin+deactivated+id+title+username+photo+participants_count+date+version+migrated_to+"]"
        
    def TL_chat_old2(self):
        flags=self.data.readInt32()
        creator=self.returnfl(1,"Creator")
        kicked=self.returnfl(2,"Kicked")
        left=self.returnfl(4,"Left")
        admins_enabled=self.returnfl(0x8,"Admins_Enabled")
        admin=self.returnfl(0x10,"Admin")
        deactivated=self.returnfl(0x20,"Deactivated")
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:\""+self.data.readString()+";"
        photo=self.ChatPhoto()
        participants_count="Participants_Count:"+str(self.data.readInt32())+";"
        date="Date:"+self.getDate(self.data.readInt32())+";"
        version="Version:"+str(self.data.readInt32())+";"
        return "Chat_old2 ["+creator+kicked+left+admins_enabled+admin+deactivated+id+title+username+photo+participants_count+date+version+"]"

    def TL_chatEmpty(self):
        id="Id:"+str(self.data.readInt32())+";"
        title="Title:Deleted;"
        return "chatEmpty ["+id+title+"]"
        
    def TL_geoPoint(self):
        long=str(self.data.readDouble())
        lat=str(self.data.readDouble())
        return "Longitude:"+long+";Latitude:"+lat+";"
        
    def geoPoint(self):
        type=self.data.readInt32()
        if (type==0x1117DD5F):
            return ""
        elif (type==0x2049D70C):
            return self.TL_geoPoint()
            
    def TL_geoChat(self):
        id="Id:"+str(self.data.readInt32())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        title="Title:\""+self.data.readString()+";"
        address="Address:\""+self.data.readString()+";"
        venue="Venue:\""+self.data.readString()+";"
        geo=self.geoPoint()
        photo=self.ChatPhoto()
        participants_count="Participants_Count:"+str(self.data.readInt32())+";"
        date="Date:"+self.getDate(self.data.readInt32())+";"
        checked_in="Checked_In:"+str(self.data.readBool())+";"
        version="Version:"+str(self.data.readInt32())+";"
        return "geoChat ["+creator+kicked+left+admins_enabled+admin+deactivated+id+title+username+photo+participants_count+date+version+"]"
        
    def Chat(self):
        subtype=self.data.readInt32()
        type=self.getchat(subtype)
        if type=="TL_chatForbidden_old":
            return self.TL_chatForbidden_old()
        elif type=="TL_chatForbidden":
            return self.TL_chatForbidden()
        elif type=="TL_channel":
            return self.TL_channel()
        elif type=="TL_channelForbidden":
            return self.TL_channelForbidden()
        elif type=="TL_channelForbidden_layer52":
            return self.TL_channelForbidden_layer52()
        elif type=="TL_channel_layer48":
            return self.TL_channel_layer48()
        elif type=="TL_channel_old":
            return self.TL_channel_old()
        elif type=="TL_chat_old":
            return self.TL_chat_old()
        elif type=="TL_chat_old2":
            return self.TL_chat_old2()
        elif type=="TL_geoChat":
            return self.TL_geoChat()
        elif type=="TL_channelForbidden_layer67":
            return self.TL_channelForbidden_layer67()
        elif type=="TL_chatEmpty":
            return self.TL_chatEmpty()
        elif type=="TL_channel_layer67":
            return self.TL_channel_layer67()
        elif type=="TL_chat":
            return self.TL_chat()
        else:
            return "Chat [Unknown type:"+hex(subtype)+"]"
            
    class TelegramPageBlock:
        TL_PageBlock={
            "TL_pageBlockAuthorDate":0xBAAFE5E0,
            "TL_pageBlockHeader":0xBFD064EC,
            "TL_pageBlockPreformatted":0xC070D93E,
            "TL_pageBlockEmbed":0xCDE200D1,
            "TL_pageBlockAnchor":0xCE0D37B0,
            "TL_pageBlockEmbed_layer60":0xD935D8FB,
            "TL_pageBlockVideo":0xD9D71866,
            "TL_pageBlockDivider":0xDB20B188,
            "TL_pageBlockPhoto":0xE9C69982,
            "TL_pageBlockChannel":0xEF1751B5,
            "TL_pageBlockSubheader":0xF12BB6E1,
            "TL_pageBlockCollage":0x8B31C4F,
            "TL_pageBlockSlideshow":0x130C8963,
            "TL_pageBlockUnsupported":0x13567E8A,
            "TL_pageBlockBlockquote":0x263D7C26,
            "TL_pageBlockEmbedPost":0x292C7BE9,
            "TL_pageBlockAudio":0x31B81A7F,
            "TL_pageBlockCover":0x39F23300,
            "TL_pageBlockList":0x3A58C7F4,
            "TL_pageBlockAuthorDate_layer60":0x3D5B64F2,
            "TL_pageBlockParagraph":0x1182402406,
            "TL_pageBlockFooter":0x1216809369,
            "TL_pageBlockPullquote":0x1329878739,
            "TL_pageBlockTitle":0x1890305021,
            "TL_pageBlockSubtitle":0x8FFA9A1F
        }

    def getpageblock(self,value):
        for key in self.TelegramPageBlock.TL_PageBlock.keys():
            if self.TelegramPageBlock.TL_PageBlock[key]==value:
                return key
        return ""

    def RichText(self):
        type=self.data.readInt32()
        if (type==0x6724ABC4):
            return "<bold>"+self.RichText()+"</bold>"
        elif (type==0x6C3F19B9):
            return "<fixed>"+self.RichText()+"</fixed>"
        elif (type==0x744694E0):
            return "\""+self.data.readString()+"\""
        elif (type==0x7E6260D7):
            flag=self.data.readInt32()
            txt=""
            if (flag==0x1CB5C415):
                count=self.data.readInt32()
                for x in range(0,count):
                    txt+=self.RichText()  
            return "<Concat>"+txt+"</Concat>"   
        elif (type==0x9BF8BB95):
            return "<Strike>"+self.RichText()+"</Strike>"  
        elif (type==0xC12622C4):
            return "<ul>"+self.RichText()+"</ul>"  
        elif (type==0xD912A59C):
            return "<i>"+self.RichText()+"</i>"
        elif (type==0xDC3D824F):
            return ""
        elif (type==0xDE5A0DD6):
            return "<email>Text:\""+self.RichText()+"\";Email:\""+self.data.readString()+"\"</email>"
        elif (type==0x3C2884C1):
            return "<url>Text:\""+self.RichText()+"\";Url:\""+self.data.readString()+"\";WebPage_Id:"+str(self.data.readInt64())+"</email>"
            
    def TL_pageBlockAuthorDate(self):
        author=self.RichText()
        published_date=self.data.readInt32()
        return "<Author>"+author+"</Author>"+"<Published_Date>"+self.getDate(published_date)+"</Published_Date>"
        
    def TL_pageBlockHeader(self):
        return "<header>"+self.RichText+"</header>"
        
    def TL_pageBlockPreformatted(self):
        return "<pre>"+self.RichText+"</pre>;<Language>"+self.data.readString()+"</Language>"
        
    def TL_pageBlockEmbed(self):
        flags=self.data.readInt32()
        full_width="False"
        if (flags&1)!=0:
            full_width="True"
        full_width="Full_Width:"+full_width+";"
        
        allow_scrolling="False"
        if (flags&8)!=0:
            allow_scrolling="True"
        allow_scrolling="Allow_Scrolling:"+allow_scrolling+";"
        
        url=""
        if (flags&1)!=0:
            url="Url:\""+self.data.readString()+"\";"
        
        html=""
        if (flags&4)!=0:
            html="HTML:\""+self.data.readString()+"\";"
        
        poster_photo_id=""
        if (flags&0x10)!=0:
            poster_photo_id=str(self.data.readInt64())
        
        w="Width:"+str(self.data.readInt32())+";"
        h="Height:"+str(self.data.readInt32())+";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<embed>"+full_width+allow_scrolling+url+html+poster_photo_id+w+h+caption+"</embed>"
        
    def TL_pageBlockAnchor(self):
        return "<a>"+self.data.readString()+"</a>"
        
    def TL_pageBlockEmbed_layer60(self):
        flags=self.data.readInt32()
        full_width="False"
        if (flags&1)!=0:
            full_width="True"
        full_width="Full_Width:"+full_width+";"
        
        allow_scrolling="False"
        if (flags&8)!=0:
            allow_scrolling="True"
        allow_scrolling="Allow_Scrolling:"+allow_scrolling+";"
        
        url=""
        if (flags&1)!=0:
            url="Url:\""+self.data.readString()+"\";"
        
        html=""
        if (flags&4)!=0:
            html="HTML:\""+self.data.readString()+"\";"
        
        w="Width:"+str(self.data.readInt32())+";"
        h="Height:"+str(self.data.readInt32())+";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<embed>"+full_width+allow_scrolling+url+html+poster_photo_id+w+h+caption+"</embed>"
        
    def TL_pageBlockVideo(self):
        flags=self.data.readInt32()
        auto_play="False"
        if (flags&1)!=0:
            auto_play="True"
        auto_play="Auto_Play:"+auto_play+";"
        
        loop="False"
        if (flags&2)!=0:
            loop="True"
        loop="Loop:"+loop+";"
        
        video_id="Video_Id:"+str(self.data.readInt64())+";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<video>"+auto_play+loop+video_id+caption+"</video>"
        
    def TL_pageBlockDivider(self):
        return "<div>"
        
    def TL_pageBlockPhoto(self):
        photo_id="Photo_Id:"+str(self.data.readInt64())+";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<photo>"+photo_id+caption+"</photo>"
        
    def TL_pageBlockChannel(self):
        channel=self.Chat()
        return "Channel ["+channel+"]"
        
    def TL_pageBlockSubheader(self):
        return "<subheader>"+self.RichText+"</subheader>"
        
    def TL_pageBlockCollage(self):
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            caption="Caption:\""+self.RichText()+"\";"
        return "<BlockCollage>"+pageblock+caption+"</BlockCollage>"
        
    def TL_pageBlockSlideshow(self):
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            caption="Caption:\""+self.RichText()+"\";"
        return "<BlockSlideshow>"+pageblock+caption+"</BlockSlideshow>"
        
    def TL_pageBlockUnsupported(self):
        return ""
        
    def TL_pageBlockBlockquote(self):
        text="Text:\""+self.data.readString()+"\";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<quote>"+text+caption+"</quote>"
        
    def TL_pageBlockEmbedPost(self):
        url="Url:\""+self.data.readString()+"\";"
        webpage_id="webpage_id:"+str(self.data.readInt64())+";"
        author_photo_id="author_photo_id:"+str(self.data.readInt64())+";"
        author="Author:\""+self.data.readString()+"\";"
        date="Date:\""+self.getDate(self.data.readInt32())+"\";"
        magic=0x1CB5C415
        pageblock=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            caption="Caption:\""+self.RichText()+"\";"
        return "<EmbedPost>"+url+webpage_id+author_photo_id+author+date+pageblock+caption+"</EmbedPost>"
        
    def TL_pageBlockAudio(self):
        audio_id="Audio_Id:"+str(self.data.readInt64())+";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<audio>"+photo_id+caption+"</audio>"
        
    def TL_pageBlockCover(self):
        return "<cover>"+self.PageBlock()+"</cover>"
        
    def TL_pageBlockList(self):
        ordered=self.data.readBool()
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+=self.RichText()
        return "<BlockList>"+pageblock+caption+"</BlockList>"
        
    def TL_pageBlockAuthorDate_layer60(self):
        author_text="Author_Text:\""+self.data.readString()+"\";"
        author="Author:\""+self.data.readString()+"\";"
        date="Published_Date:\""+self.getDate(self.data.readInt32())+"\";"
        return "<BlockAuthorDate_layer60>"+author_text+author+date+"</BlockAuthorDate_layer60>"
        
    def TL_pageBlockParagraph(self):
        return "<p>"+self.RichText()+"</p>"
        
    def TL_pageBlockFooter(self):
        return "<footer>"+self.RichText()+"</footer>"
        
    def TL_pageBlockPullquote(self):
        text="Text:\""+self.data.readString()+"\";"
        caption="Caption:\""+self.RichText()+"\";"
        return "<pullquote>"+text+caption+"</pullquote>"
        
    def TL_pageBlockTitle(self):
        return "<title>"+self.RichText()+"</title>"
        
    def TL_pageBlockSubtitle(self):
        return "<subtitle>"+self.RichText()+"</subtitle>"
    
    def PageBlock(self):
        subtype=self.data.readInt32()
        type=self.getpageblock(subtype)
        if type=="TL_pageBlockAuthorDate":
            return self.TL_pageBlockAuthorDate()
        elif type=="TL_pageBlockHeader":
            return self.TL_pageBlockHeader()
        elif type=="TL_pageBlockPreformatted":
            return self.TL_pageBlockPreformatted()
        elif type=="TL_pageBlockEmbed":
            return self.TL_pageBlockEmbed()
        elif type=="TL_pageBlockAnchor":
            return self.TL_pageBlockAnchor()
        elif type=="TL_pageBlockEmbed_layer60":
            return self.TL_pageBlockEmbed_layer60()
        elif type=="TL_pageBlockVideo":
            return self.TL_pageBlockVideo()
        elif type=="TL_pageBlockDivider":
            return self.TL_pageBlockDivider()
        elif type=="TL_pageBlockPhoto":
            return self.TL_pageBlockPhoto()
        elif type=="TL_pageBlockChannel":
            return self.TL_pageBlockChannel()
        elif type=="TL_pageBlockSubheader":
            return self.TL_pageBlockSubheader()
        elif type=="TL_pageBlockCollage":
            return self.TL_pageBlockCollage()
        elif type=="TL_pageBlockSlideshow":
            return self.TL_pageBlockSlideshow()
        elif type=="TL_pageBlockUnsupported":
            return self.TL_pageBlockUnsupported()
        elif type=="TL_pageBlockBlockquote":
            return self.TL_pageBlockBlockquote()
        elif type=="TL_pageBlockEmbedPost":
            return self.TL_pageBlockEmbedPost()
        elif type=="TL_pageBlockAudio":
            return self.TL_pageBlockAudio()
        elif type=="TL_pageBlockCover":
            return self.TL_pageBlockCover()
        elif type=="TL_pageBlockList":
            return self.TL_pageBlockList()
        elif type=="TL_pageBlockAuthorDate_layer60":
            return self.TL_pageBlockAuthorDate_layer60()
        elif type=="TL_pageBlockParagraph":
            return self.TL_pageBlockParagraph()
        elif type=="TL_pageBlockFooter":
            return self.TL_pageBlockFooter()
        elif type=="TL_pageBlockPullquote":
            return self.TL_pageBlockPullquote()
        elif type=="TL_pageBlockTitle":
            return self.TL_pageBlockTitle()
        elif type=="TL_pageBlockSubtitle":
            return self.TL_pageBlockSubtitle()
        else:
            return "PageBlock [Unknown type:"+hex(subtype)+"]"
        
    def TL_pagePart_layer67(self):
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            type=self.data.readInt32()
            if (type==magic):
                count=self.data.readInt32()
                for v in range(0,count):
                    photo+="Photo Id("+str(v)+"):"+self.data.Photo()+";"
                type=self.data.readInt32()
                if (type==magic):
                    count=self.data.readInt32()
                    for v in range(0,count):
                        document+="Document Id("+str(v)+"):"+self.data.Document()+";"
        return "PagePart_layer67 ["+pageblock+photo+document+"]"

    def TL_pageFull_layer67(self):
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        photo=""
        document=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            type=self.data.readInt32()
            if (type==magic):
                count=self.data.readInt32()
                for v in range(0,count):
                    photo+="Photo Id("+str(v)+"):"+self.Photo()+";"
                type=self.data.readInt32()
                if (type==magic):
                    count=self.data.readInt32()
                    for v in range(0,count):
                        document+="Document Id("+str(v)+"):"+self.Document()+";"
        return "PageFull_layer67 ["+pageblock+photo+document+"]"
        
    def TL_pageFull(self):
        type=self.data.readInt32()
        magic=0x1CB5C415
        pageblock=""
        photo=""
        document=""
        if (type==magic):
            count=self.data.readInt32()
            for v in range(0,count):
                pageblock+="PageBlock Id("+str(v)+"):"+self.PageBlock()+";"
            type=self.data.readInt32()
            if (type==magic):
                count=self.data.readInt32()
                for v in range(0,count):
                    photo+="Photo Id("+str(v)+"):"+self.Photo()+";"
                type=self.data.readInt32()
                if (type==magic):
                    count=self.data.readInt32()
                    for v in range(0,count):
                        document+="Document Id("+str(v)+"):"+self.Document()+";"
        return "PageFull ["+pageblock+photo+document+"]"

    def Page(self):
        type=self.data.readInt32()
        if (type==0x8DEE6C44):
            return self.TL_pagePart_layer67()
        elif (type==0xD7A19D69):
            return self.TL_pageFull_layer67()
        elif (type==0x556EC7AA):
            return self.TL_pageFull()
        elif (type==0x8E3F9EBE):
            return self.TL_pagePart()
        else:
            return "Page [Unknown type:"+hex(type)+"]"
            
    def Audio(self):
        type=self.data.readInt32()
        if (type==0x427425E7):
            return self.TL_audio_old()
        elif (type==0x555555F6):
            return self.TL_audioEncrypted()
        elif (type==0x586988D8):
            return "Audio: Empty"
        elif (type==0xC7AC6496):
            return self.TL_audio_old2()
        elif (type==0xF9E35055):
            return self.TL_audio_layer45()

    def TL_webPage_old(self):
        msg="TL_webPage_old - "
        flags=self.data.readInt32()
        id=self.data.readInt64()
        url=self.data.readString()
        display_url=self.data.readString()
        type=""
        site_name=""
        title=""
        description=""
        photo=""
        embed_type=""
        embed_width=0x0
        embed_height=0x0
        duration=0
        author=""

        if ((flags&1)!=0):
            type=self.data.readString()
        if ((flags&2)!=0):
            site_name=self.data.readString()
        if ((flags&4)!=0):
            title=self.data.readString()
        if ((flags&8)!=0):
            description=self.data.readString()
        if ((flags&0x10)!=0):
            photo=self.Photo()
        if ((flags&0x20)!=0):
            embed_type=self.data.readString()
        if ((flags&0x40)!=0):
            embed_width=self.data.readInt32()
            embed_height=self.data.readInt32()
        if ((flags&0x80)!=0):
            duration=self.data.readInt32()
        if ((flags&0x100)!=0):
            author=self.data.readString()

        msg+="Id: "+str(id)+";"
        msg+="Url: "+url+";"
        msg+="Display_Url: "+display_url+";"
        if (type!=""):
            msg+="Type: "+type+";"
        if (site_name!=""):
            msg+="Site_name: "+site_name+";"
        if (title!=""):
            msg+="Title: "+title+";"
        if (description!=""):
            msg+="Description: "+description+";"
        if (photo!=""):
            msg+="Photo: "+photo+";"
        if (embed_type!=""):
            msg+="Embed_Type: "+embed_type+";"
        if (embed_width!=0x0):
            msg+="Embed_Width: "+str(embed_width)+";"
        if (embed_height!=0x0):
            msg+="Embed_Height: "+str(embed_height)+";"
        if (duration!=0):
            msg+="Duration: "+str(duration)+";"
        if (author!=""):
            msg+="Author: "+author+";"
        return msg

    def TL_webPage_layer58(self):
        msg="TL_webPage_layer58 - "
        flags=self.data.readInt32()
        id=self.data.readInt64()
        url=self.data.readString()
        display_url=self.data.readString()
        type=""
        site_name=""
        title=""
        description=""
        photo=""
        embed_type=""
        embed_width=0x0
        embed_height=0x0
        duration=0
        author=""
        document=""

        if ((flags&1)!=0):
            type=self.data.readString()
        if ((flags&2)!=0):
            site_name=self.data.readString()
        if ((flags&4)!=0):
            title=self.data.readString()
        if ((flags&8)!=0):
            description=self.data.readString()
        if ((flags&0x10)!=0):
            photo=self.Photo()
        if ((flags&0x20)!=0):
            embed_type=self.data.readString()
        if ((flags&0x40)!=0):
            embed_width=self.data.readInt32()
            embed_height=self.data.readInt32()
        if ((flags&0x80)!=0):
            duration=self.data.readInt32()
        if ((flags&0x100)!=0):
            author=self.data.readString()
        if ((flags&0x200)!=0):
            document=self.Document()

        msg+="Id: "+str(id)+";"
        msg+="Url: "+url+";"
        msg+="Display_Url: "+display_url+";"
        if (type!=""):
            msg+="Type: "+type+";"
        if (site_name!=""):
            msg+="Site_name: "+site_name+";"
        if (title!=""):
            msg+="Title: "+title+";"
        if (description!=""):
            msg+="Description: "+description+";"
        if (photo!=""):
            msg+="Photo: "+photo+";"
        if (embed_type!=""):
            msg+="Embed_Type: "+embed_type+";"
        if (embed_width!=0x0):
            msg+="Embed_Width: "+str(embed_width)+";"
        if (embed_height!=0x0):
            msg+="Embed_Height: "+str(embed_height)+";"
        if (duration!=0):
            msg+="Duration: "+str(duration)+";"
        if (author!=""):
            msg+="Author: "+author+";"
        if (document!=""):
            msg+="Document: "+document+";"
        return msg

    def TL_webPage(self):
        msg="TL_webPage - "
        flags=self.data.readInt32()
        id=self.data.readInt64()
        url=self.data.readString()
        display_url=self.data.readString()
        hash=self.data.readInt32()
        type=""
        site_name=""
        title=""
        description=""
        photo=""
        embed_type=""
        embed_url=""
        embed_width=0x0
        embed_height=0x0
        duration=0
        author=""
        document=""
        cached_page=""

        if ((flags&1)!=0):
            type=self.data.readString()
        if ((flags&2)!=0):
            site_name=self.data.readString()
        if ((flags&4)!=0):
            title=self.data.readString()
        if ((flags&8)!=0):
            description=self.data.readString()
        if ((flags&0x10)!=0):
            photo=self.Photo()
        if ((flags&0x20)!=0):
            embed_url=self.data.readString()
            embed_type=self.data.readString()
        if ((flags&0x40)!=0):
            embed_width=self.data.readInt32()
            embed_height=self.data.readInt32()
        if ((flags&0x80)!=0):
            duration=self.data.readInt32()
        if ((flags&0x100)!=0):
            author=self.data.readString()
        if ((flags&0x200)!=0):
            document=self.Document()
        if ((flags&0x400)!=0):
            cached_page=self.Page()
            
        msg+="Id: "+str(id)+";"
        msg+="Url: "+url+";"
        msg+="Display_Url: "+display_url+";"
        msg+="Hash: "+str(hash)+";"
        if (type!=""):
            msg+="Type: "+type+";"
        if (site_name!=""):
            msg+="Site_name: "+site_name+";"
        if (title!=""):
            msg+="Title: "+title+";"
        if (description!=""):
            msg+="Description: "+description+";"
        if (photo!=""):
            msg+="Photo: "+photo+";"
        if (embed_type!=""):
            msg+="Embed_Type: "+embed_type+";"
        if (embed_url!=""):
            msg+="Embed_Url: "+embed_url+";"
        if (embed_width!=0x0):
            msg+="Embed_Width: "+str(embed_width)+";"
        if (embed_height!=0x0):
            msg+="Embed_Height: "+str(embed_height)+";"
        if (duration!=0):
            msg+="Duration: "+str(duration)+";"
        if (author!=""):
            msg+="Author: "+author+";"
        if (document!=""):
            msg+="Document: "+document+";"
        if (cached_page!=""):
            msg+="Cached_Page: "+cached_page+";"
        return msg

    def TL_webPagePending(self):
        msg="TL_webPagePending - "
        id=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        msg+="Id: "+str(id)+";"
        msg+="Date: "+date+";"
        return msg

    def TL_webPageUrlPending(self):
        url=self.data.readString()
        return "Url [\""+str(url)+"\"];"

    def WebPage(self):
        type=self.data.readInt32()
        if (type==0x5F07B4BC):
            return self.TL_webPage()
        elif (type==0x85849473):
            return "WebPage: NotModified"
        elif (type==0xA31EA0B5):
            return self.TL_webPage_old()
        elif (type==0xC586DA1C):
            return self.TL_webPagePending()
        elif (type==0xCA820ED7):
            return self.TL_webPage_layer58()
        elif (type==0xD41A5167):
            return self.TL_webPageUrlPending()
        elif (type==0xEB1477E8):
            return "WebPage: Empty"
        print ("Unknown WebPage: "+hex(type))
        return ""

    def TL_documentAttributeAudio_old(self):
        duration=self.data.readInt32()
        return "Audio [Duration:"+str(duration)+"];"
        
    def TL_documentAttributeAudio_layer45(self):
        duration="Duration:"+self.data.readInt32()+";"
        title="Title:"+self.data.readString()+";"
        performer="Performer:"+self.data.readString()+";"
        return "Audio_layer45 ["+duration+title+performer+"];"

    def TL_documentAttributeFilename(self):
        filename=self.data.readString()
        return "Filename ["+filename+"];"

    def TL_documentAttributeVideo_layer65(self):
        duration=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        return "Video [Duration:"+str(duration)+";W:"+str(w)+";H:"+str(h)+"];"

    def TL_documentAttributeImageSize(self):
        duration=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        return "ImageSize [W:"+str(w)+";H:"+str(h)+"];"

    def TL_documentAttributeSticker_old2(self):
        alt=self.data.readString()
        return "Sticker_old2 [Alt:"+alt+"];"

    class TelegramDocumentAttribute:
        TL_DocumentAttribute={
            "TL_documentAttributeImageSize":0x6C37C15C,
            "TL_documentAttributeHasStickers":0x9801D2F7,
            "TL_documentAttributeAudio":0x9852F9C6,
            "TL_documentAttributeSticker_old2":0x994C9882,
            "TL_documentAttributeAudio_layer45":0xDED218E0,
            "TL_documentAttributeSticker_old":0xFB0A5727,
            "TL_documentAttributeAudio_old":0x51448E5,
            "TL_documentAttributeVideo":0xEF02CE6,
            "TL_documentAttributeAnimated":0x11B58939,
            "TL_documentAttributeFilename":0x15590068,
            "TL_documentAttributeSticker_layer55":0x3A556302,
            "TL_documentAttributeVideo_layer65":0x5910CCCB,
            "TL_documentAttributeSticker":0x6319D612
        }

    def getdocumentattribute(self,value):
        for key in self.TelegramDocumentAttribute.TL_DocumentAttribute.keys():
            if self.TelegramDocumentAttribute.TL_DocumentAttribute[key]==value:
                return key
        return ""
    
    def TL_documentAttributeAudio(self):
        flags=self.data.readInt32()
        voice="Voice:False"
        if (flags&0x400)!=0:
            voice="Voice:True"
        voice=voice+";"
        duration="Duration:"+str(self.data.readInt32())+";"
        title=""
        performer=""
        waveform=""
        
        if (flags&1)!=0:
            title="Title:\""+self.data.readString()+"\";"
        if (flags&2)!=0:
            performer="Performer:\""+self.data.readString()+"\";"
        if (flags&4)!=0:
            wave=self.data.readByteArray()
            waveform="Waveform:\""
            for x in range(0,len(wave)):
                waveform=waveform+hex(int(wave[x]))
            waveform=waveform+"\";"
        return "Audio ["+voice+duration+title+performer+waveform+"];"
    
    def TL_documentAttributeVideo(self):
        flags=self.data.readInt32()
        round_message="Round_Message:False"
        if (flags&0x400)!=0:
            round_message="Round_Message:True"
        round_message=round_message+";"
        duration="Duration:"+str(self.data.readInt32())+";"
        w="Width:"+str(self.data.readInt32())+";"
        h="Height:"+str(self.data.readInt32())+";"
        return "Video ["+round_message+duration+w+h+"];"
        
    def TL_inputStickerSetShortName(self):
        short_name="Short_Name:\""+self.data.readString()+"\""
        return "InputStickerSet: ["+short_name+"];"
        
    def TL_inputStickerSetID(self):
        id="ID:\""+str(self.data.readInt64())+"\";"
        access_hash="Access_Hash:\""+str(self.data.readInt64())+"\""
        return "InputStickerSet: ["+id+access_hash+"];"
        
    def InputStickerSet(self):
        type=self.data.readInt32()
        if (type==0x861CC8A0):
            return self.TL_inputStickerSetShortName()
        elif (type==0x9DE7A269):
            return self.TL_inputStickerSetID()
        elif (type==0xFFB62B95):
            return "InputStickerSet: Empty"
        print ("Unknown InputStickerSet: "+hex(type))
        return ""

    def TL_maskCoords(self):
        n="N:"+str(self.data.readInt32())+";"
        x="X:"+str(self.data.readDouble())+";"
        y="Y:"+str(self.data.readDouble())+";"
        zoom="Zoom:"+str(self.data.readDouble())+";"
        return n+x+y+zoom
        
    def TL_documentAttributeSticker(self):
        flags=self.data.readInt32()
        mask="Mask:False"
        if (flags&0x2)!=0:
            mask="Mask:True"
        mask=mask+";"
        alt="Alt:"+self.data.readString()+";"
        stickerset=self.InputStickerSet()
        mask_coords=""
        if (flags&1)!=0:
            mask_coords="Mask_Coords:"+self.TL_maskCoords()+";"
        return "AttributeSticker ["+mask+alt+stickerset+mask_coords+"];"
        
    def TL_documentAttributeSticker_layer55(self):
        alt=self.data.readString()
        return "Sticker_layer55 [Alt"+alt+"];"
        
    def DocumentAttribute(self):
        actionflag=self.data.readInt32()
        action=self.getdocumentattribute(actionflag)

        if (action=="TL_documentAttributeImageSize"):
            return self.TL_documentAttributeImageSize()
        elif (action=="TL_documentAttributeHasStickers"):
            return "TL_documentAttributeHasStickers"
        elif (action=="TL_documentAttributeAudio"):
            return self.TL_documentAttributeAudio()
        elif (action=="TL_documentAttributeSticker_old2"):
            return self.TL_documentAttributeSticker_old2()
        elif (action=="TL_documentAttributeAudio_layer45"):
            return self.TL_documentAttributeAudio_layer45()
        elif (action=="TL_documentAttributeSticker_old"):
            return "TL_documentAttributeSticker_old;"
        elif (action=="TL_documentAttributeAudio_old"):
            return self.TL_documentAttributeAudio_old()
        elif (action=="TL_documentAttributeVideo"):
            return self.TL_documentAttributeVideo()
        elif (action=="TL_documentAttributeAnimated"):
            return "TL_documentAttributeAnimated;"
        elif (action=="TL_documentAttributeFilename"):
            return self.TL_documentAttributeFilename()
        elif (action=="TL_documentAttributeSticker_layer55"):
            return self.TL_documentAttributeSticker_layer55()
        elif (action=="TL_documentAttributeVideo_layer65"):
            return self.TL_documentAttributeVideo_layer65()
        elif (action=="TL_documentAttributeSticker"):
            return self.TL_documentAttributeSticker()
        else:
            return "Unknown: DocumentAttribute: "+hex(actionflag)+"/"+action

    def TL_messageMediaInvoice(self):
        msg="TL_messageMediaInvoice - "
        flags=self.data.readInt32()
        test="True"
        shipping_address_requested="False"
        if (flags&2)!=0:
            shipping_address_requested="True"
        if (flags&8)==0:
            test="False"
        test="Test"+test+";"
        shipping_address_requested="Shipping_Address_Requested:"+shipping_address_requested+";"
        title="Title:\""+self.data.readString()+"\";"
        description="Description:\""+self.data.readString()+"\";"
        photo=""
        receipt_msg_id=""
        if (flags&1)!=0:
            photo="Document:"+self.TL_webDocument()+";"
        if (flags&4)!=0:
            receipt_msg_id="Receipt_msg_id:"+str(self.data.readInt32())+";"
        currency="Currency:\""+self.data.readString()+"\";"
        total_amount="Total_Amount:"+str(self.data.readInt64())+";"
        start_param="Start_Param:\""+self.data.readString()+"\";"
        msg+=test
        msg+=shipping_address_requested
        msg+=title
        msg+=description
        msg+=photo
        msg+=receipt_msg_id
        msg+=currency
        msg+=total_amount
        msg+=start_param
        return msg
    
    def TL_document(self):
        msg="TL_document - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        version=self.data.readInt32()
        attr=self.data.readInt32()
        items=0
        inf=""
        if (attr==0x1CB5C415):
            items=self.data.readInt32()
            for i in range(items):
                inf+="Item "+str(i)+":"+self.DocumentAttribute()+" "
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Date: "+date+";"
        msg+="Mime_Type: "+str(mime_type)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Version: "+str(version)+";"
        if (items!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        return msg
        
    def TL_document_layer53(self):
        msg="TL_document_layer53 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        attr=self.data.readInt32()
        items=0
        inf=""
        if (attr==0x1CB5C415):
            items=self.data.readInt32()
            for i in range(items):
                inf+="Item "+str(i)+":"+self.DocumentAttribute()+" "
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Date: "+date+";"
        msg+="Mime_Type: "+str(mime_type)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        if (items!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        return msg

    def TL_document_layer68(self):
        msg="TL_document_layer68 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        version=self.data.readInt32()
        attr=self.data.readInt32()
        items=0
        inf=""
        if (attr==0x1CB5C415):
            items=self.data.readInt32()
            for i in range(items):
                inf+="Item "+str(i)+":"+self.DocumentAttribute()+" "
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Date: "+date+";"
        msg+="Mime_Type: "+str(mime_type)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Version: "+str(version)+";"
        if (items!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        return msg

    def TL_document_old(self):
        msg="TL_document_old - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        stream=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        file_name=self.data.readString()
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Stream: "+str(stream)+";"
        msg+="Date: "+date+";"
        msg+="Filename: "+file_name+";"
        msg+="Mime_Type: "+mime_type+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_Id)+";"
        return msg

    def TL_documentEncrypted_old(self):
        msg="TL_documentEncrypted_old - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        stream=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        file_name=self.data.readString()
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        key=self.data.readByteArray();
        iv=self.data.readByteArray();
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Stream: "+str(stream)+";"
        msg+="Date: "+date+";"
        msg+="Filename: "+file_name+";"
        msg+="Mime_Type: "+mime_type+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Key: "+key+";"
        msg+="IV: "+iv+";"
        return msg

    def TL_documentEncrypted(self):
        msg="TL_documentEncrypted - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        date=self.getDate(self.data.readInt32())
        mime_type=self.data.readString()
        #print("Mime_type:"+mime_type+"\n")
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        items=self.data.readInt32()
        inf=""
        key=""
        iv=""
        count=0
        if (items==0x1CB5C415):
            count=self.data.readInt32()
            for i in range(count):
                inf+="Item "+str(i)+":"+self.DocumentAttribute()+" "
            key="Key: "+self.data.readByteArray()+";"
            iv="IV: "+self.data.readByteArray()+";"
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="Date: "+date+";"
        msg+="Mime_Type: "+mime_type+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        if (count!=0):
            msg+="Itemcount: "+hex(items)
            msg+="["+inf+"]"
        msg+=key
        msg+=iv
        return msg

    def Document(self):
        type=self.data.readInt32()
        if (type==0x87232BC7):
            return self.TL_document()
        elif (type==0xF9A39F4F):
            return self.TL_document_layer53()
        elif (type==0x55555556):
            return self.TL_documentEncrypted_old()
        elif (type==0x55555558):
            return self.TL_documentEncrypted()
        elif (type==0x9EFC6326):
            return self.TL_document_old()
        elif (type==0x36F8C871):
            return "Document: Empty"
        print("Unknown document :"+hx(type))
        return ""

    def Document_old(self):
        type=self.data.readInt32()
        if (type==0xF9A39F4F):
            return self.TL_document()
        elif (type==0x55555556):
            return self.TL_documentEncrypted_old()
        elif (type==0x55555558):
            return self.TL_documentEncrypted()
        elif (type==0x9EFC6326):
            return self.TL_document_old()
        elif (type==0x36F8C871):
            return "Document: Empty"

    def TL_video(self):
        msg="TL_video - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        duration=self.data.readInt32()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_ID: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Width: "+str(w)+";"
        msg+="Height: "+str(w)+";"
        return msg

    def TL_videoEncrypted(self):
        msg="TL_videoEncrypted - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        caption=self.data.readString()
        duration=self.data.readInt32()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        key=self.data.readByteArray();
        iv=self.data.readByteArray();
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_ID: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Caption: "+caption+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Width: "+str(w)+";"
        msg+="Height: "+str(w)+";"
        msg+="Key: "+key+";"
        msg+="IV: "+iv+";"
        return msg

    def TL_video_old2(self):
        msg="TL_video_old2 - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        caption=self.data.readString()
        duration=self.data.readInt32()
        mime_type=self.data.readString()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_ID: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Caption: "+caption+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Mime_Type: "+mime_type+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Width: "+str(w)+";"
        msg+="Height: "+str(w)+";"
        return msg

    def TL_video_old(self):
        msg="TL_video_old - "
        id=self.data.readInt64()
        access_hash=self.data.readInt64()
        user_id=self.data.readInt32()
        date=self.getDate(self.data.readInt32())
        caption=self.data.readString()
        duration=self.data.readInt32()
        size=self.data.readInt32()
        thumb=self.PhotoSize()
        dc_id=self.data.readInt32()
        w=self.data.readInt32()
        h=self.data.readInt32()
        msg+="Id: "+str(id)+";"
        msg+="Access_Hash: "+str(access_hash)+";"
        msg+="User_ID: "+self.gettelegramuser(user_id)+";"
        msg+="Date: "+date+";"
        msg+="Caption: "+caption+";"
        msg+="Duration: "+str(duration)+";"
        msg+="Size: "+str(size)+";"
        msg+="Thumb: "+thumb+";"
        msg+="Dc_Id: "+str(dc_id)+";"
        msg+="Width: "+str(w)+";"
        msg+="Height: "+str(w)+";"
        return msg

    def Video(self):
        type=self.data.readInt32()
        if (type==0xEE9F4A4D):
            return self.TL_video()
        if (type==0x388FA391):
            return self.TL_video_old2()
        if (type==0x55555553):
            return self.TL_videoEncrypted()
        if (type==0x5A04A49F):
            return self.TL_video_old()
        if (type==0xC10658A8):
            return "Video: Empty"
        print("Unknown Video: "+hex(type))
        return ""

    def Geo(self):
        return "TL_messageMediaGeo - "+self.GeoPoint()

    def Venue_layer71(self):
        geo=self.GeoPoint()
        title=self.data.readString()
        address=self.data.readString()
        provider=self.data.readString()
        venue_id=self.data.readString()
        msg+="Geo: "+str(geo)+";"
        msg+="Title: "+str(title)+";"
        msg+="Address: "+str(address)+";"
        msg+="Provider: "+str(provider)+";"
        msg+="Venue_ID: "+str(venue_id)+";"
        return "TL_messageMediaVenue_layer71 - "

    def Venue(self):
        geo=self.GeoPoint()
        title=self.data.readString()
        address=self.data.readString()
        provider=self.data.readString()
        venue_id=self.data.readString()
        venue_type=self.data.readString()
        msg+="Geo: "+str(geo)+";"
        msg+="Title: "+str(title)+";"
        msg+="Address: "+str(address)+";"
        msg+="Provider: "+str(provider)+";"
        msg+="Venue_ID: "+str(venue_id)+";"
        msg+="Venue_Type: "+str(venue_type)+";"
        return "TL_messageMediaVenue - "
        
    def TL_messageMediaDocument_layer74(self):
        flags=self.data.readInt32()
        doc=""
        caption=""
        ttl_seconds=""
        if (flags&1)!=0:
            doc=self.Document()
        else:
            return "Document: Empty"
        if (flags&2)!=0:
            caption="Caption:\""+self.data.readString()+"\";"
        if (flags&4)!=0:
            ttl_seconds="TTL_Seconds:"+str(self.data.readInt32())+";"
        return doc+";"+caption+ttl_seconds

    def TL_messageMediaDocument(self):
        flags=self.data.readInt32()
        doc=""
        caption=""
        ttl_seconds=""
        if (flags&1)!=0:
            doc=self.Document()
        else:
            return "Document: Empty"
        if (flags&2)!=0:
            caption="Caption:\""+self.data.readString()+"\";"
        if (flags&4)!=0:
            ttl_seconds="TTL_Seconds:"+str(self.data.readInt32())+";"
        return doc+";"+caption+ttl_seconds
        
    def TL_messageMediaDocument_layer68(self):
        doc="TL_Document_layer68:"+self.Document()+";"
        caption="Caption:\""+self.data.readString()+"\";"
        return doc+caption
        
    def TL_messageMediaDocument_old(self):
        doc="TL_Document_old:"+self.Document()+";"
        return doc
    
    def TL_messageMediaGeoLive(self):
        geo=self.GeoPoint()
        period=self.data.readInt32()
        msg="Geo: "+str(geo)+";"
        msg+="Period: "+str(period)+";"
        return "TL_messageMediaGeoLive - " + msg

    def telegrammedia(self):
        mediatype=self.data.readInt32()
        type=self.getmedia(mediatype)
        #print("Mediatype: "+type)
        if (type=="TL_messageMediaEmpty"):
            return "Empty"
        elif (type=="TL_messageMediaPhoto_old"):
            return self.TL_messageMediaPhoto_old()
        elif (type=="TL_messageMediaPhoto_layer68"):
            return self.TL_messageMediaPhoto_layer68()
        elif (type=="TL_messageMediaPhoto_layer74"):
            return self.TL_messageMediaPhoto_layer74()
        elif (type=="TL_messageMediaPhoto"):
            return self.TL_messageMediaPhoto()
        elif (type=="TL_messageMediaVideo_layer45") or (type=="TL_messageMediaVideo_old"):
            return self.Video()
        elif (type=="TL_messageMediaGeo"):
            return self.Geo()
        elif (type=="TL_messageMediaContact"):
            return self.TL_messageMediaContact()
        elif (type=="TL_messageMediaInvoice"):
            return self.TL_messageMediaInvoice()
        elif (type=="TL_messageMediaUnsupported_old"):
            return "Unsupported_Old - "+self.data.readByteArray()
        elif (type=="TL_messageMediaDocument_old"):
            return self.TL_messageMediaDocument_old()
        elif (type=="TL_messageMediaDocument_layer74"):
            return self.TL_messageMediaDocument_layer74()
        elif (type=="TL_messageMediaDocument"):
            return self.TL_messageMediaDocument()
        elif (type=="TL_messageMediaDocument_layer68"):
            return self.TL_messageMediaDocument_layer68()
        elif (type=="TL_messageMediaAudio_layer45"):
            return self.Audio()
        elif (type=="TL_messageMediaVenue"):
            return self.Venue()
        elif (type=="TL_messageMediaVenue_layer71"):
            return self.Venue_layer71()
        elif (type=="TL_messageMediaUnsupported"):
            return "Unsupported - "+self.data.readByteArray()
        elif (type=="TL_messageMediaWebPage"):
            return self.WebPage()
        elif (type=="TL_messageMediaGeoLive"):
            return self.TL_messageMediaGeoLive()
        print ("Unknown media : "+type)
        return ""  

    class TelegramDecryptedMessageAction:
        TL_DecryptedMessageAction={
            "TL_decryptedMessageActionDeleteMessages":0x65614304,
            "TL_decryptedMessageActionFlushHistory":0x6719E45C,
            "TL_decryptedMessageActionAcceptKey":0x6FE1735B,
            "TL_decryptedMessageActionScreenshotMessages":0x8AC1F475,
            "TL_decryptedMessageActionSetMessageTTL":0xA1733AEC,
            "TL_decryptedMessageActionNoop":0xA82FDD63,
            "TL_decryptedMessageActionTyping":0xCCB27641,
            "TL_decryptedMessageActionAbortKey":0xDD05EC6B,
            "TL_decryptedMessageActionCommitKey":0xEC2E0B9B,
            "TL_decryptedMessageActionNotifyLayer":0xF3048883,
            "TL_decryptedMessageActionRequestKey":0xF3C9611B,
            "TL_decryptedMessageActionReadMessages":0xC4F40BE,
            "TL_decryptedMessageActionResend":0x511110B0
        }
    
    def getdecryptedaction(self,value):
        for key in self.TelegramDecryptedMessageAction.TL_DecryptedMessageAction.keys():
            if self.TelegramDecryptedMessageAction.TL_DecryptedMessageAction[key]==value:
                return key
        return hex(value)
        
    class TelegramAction:
        TL_action={
            "TL_messageActionGeoChatCheckin":0xC7D53DE,
            "TL_messageActionPaymentSent":0x40699CD0,
            "TL_messageActionScreenshotTaken":0x4792929B,
            "TL_messageActionChatAddUser":0x488A7337,
            "TL_messageActionChatMigrateTo":0x51BDB021,
            "TL_messageActionUserJoined":0x55555550,
            "TL_messageActionUserUpdatedPhoto":0x55555551,
            "TL_messageActionTTLChange":0x55555552,
            "TL_messageActionCreatedBroadcastList":0x55555557,
            "TL_messageActionLoginUnknownLocation":0x555555F5,
            "TL_messageEncryptedAction":0x555555F7,
            "TL_messageActionChatAddUser_old":0x5E3CFC4B,
            "TL_messageActionGeoChatCreate":0x6F038EBC,
            "TL_messageActionChatEditPhoto":0x7FCB13A8,
            "TL_messageActionPhoneCall":0x80E11A7F,
            "TL_messageActionGameScore":0x92A72876,
            "TL_messageActionPinMessage":0x94BD38ED,
            "TL_messageActionChannelCreate":0x95D2AC92,
            "TL_messageActionChatDeletePhoto":0x95E3FBEF,
            "TL_messageActionHistoryClear":0x9FBAB604,
            "TL_messageActionChatCreate":0xA6638B9A,
            "TL_messageActionChannelMigrateFrom":0xB055EAEE,
            "TL_messageActionChatDeleteUser":0xB2AE9B0C,
            "TL_messageActionChatEditTitle":0xB5A1CE5A,
            "TL_messageActionEmpty":0xB6AEF7B0,
            "TL_messageActionGroupCall":0xEBD29CD8,
            "TL_messageActionChatJoinedByLink":0xF89CF5E8,
            # Service_V2 action
            "action_user_info":0x00000100,
            "TL_messageActionChatAddUser_old_v2":0x00000102,
            "TL_messageActionChatCreate_add_user":0x00000103
        }
        
    def getaction(self,value):
        for key in self.TelegramAction.TL_action.keys():
            if self.TelegramAction.TL_action[key]==value:
                return key
        return hex(value)

    def TL_messageActionUserJoined(self):
        try:
            from_id=self.data.readInt32()
            to_id_user=self.Peer()
            to_id_date=self.data.readInt32()
            message="[" + self.gettelegramuser(from_id) + " joined the chat]"
            return {"from_id":from_id, "to_id_user":to_id_user, "to_id_date":to_id_date, "message":message}
        except:
            return {"":""}

    def TL_messageActionChatAddUser_old_v2(self):
        from_id=self.gettelegramuser(self.data.readInt32())
        to_id_user=self.Peer()
        to_id_date=self.data.readInt32()
        tempValue=self.data.readInt32() # Unkown - (0x488A7337 - 1217033015)
        tempValue=self.data.readInt32() # Members - (0x1CB5C415 - following new groupmebers)
        countMembers=self.data.readInt32()

        message="[User: "+from_id+" added following "+ str(countMembers)
        if countMembers == 1:
            message=message+" User:\x0a"
        else:
            message=message+" Users:\x0a"
        for n in range(0, countMembers):
            to_id_member=self.gettelegramuser(self.data.readInt32())
            if n == 0:
                message=message+to_id_member
            else:
                message=message+",\x0a"+to_id_member
        message=message+"]"
        return {"from_id":from_id, "to_id_user":to_id_user, "to_id_date":to_id_date, "message":message}
    
    def TL_messageActionChatCreate_add_user(self):
        from_id=self.gettelegramuser(self.data.readInt32())
        to_id_user=self.Peer()
        to_id_date=self.data.readInt32()
        tempValue=self.data.readInt32() # Groupname - (0xA6638B9A - following new groupname string)
        # stringlength - String
        Groupname=self.data.readString()
        tempValue=self.data.readInt32() # Members - (0x1CB5C415 - following new groupmebers)
        countMembers=self.data.readInt32()
        message="[User: "+from_id+" create Group '"+ str(Groupname)+ "'\x0a"
        message=message+" and added following "+ str(countMembers)
        if countMembers == 1:
            message=message+" User:\x0a"
        else:
            message=message+" Users:\x0a"
        for n in range(0, countMembers):
            to_id_member=self.gettelegramuser(self.data.readInt32())
            if n == 0:
                message=message+to_id_member
            else:
                message=message+",\x0a"+to_id_member
        message=message+"]"
        return {"from_id":from_id, "to_id_user":to_id_user, "to_id_date":to_id_date, "message":message}
        
    def TL_messageActionPaymentSent(self):
        currency = "Currency:\""+self.data.readString()+"\";"
        total_amount = "Total_Amount:"+self.data.readInt64()+";"
        return {"message":"[TL_messageActionPaymentSent]","media":currency+total_amount}
    
    def TL_messageActionChatCreate(self):
        title="Title:\""+self.data.readString()+"\";"
        users = "Users:\""
        flag = self.data.readInt32()
        if (flag==0x1CB5C415):
            count = self.data.readInt32()
            for x in range(0,count):
                users = users+str(self.data.readInt32())+","
        users=users+"\";"
        return {"message":"[TL_messageActionChatCreate]","media":title+users}
        
    def TL_messageActionChatAddUser(self):
        users = "Users:\""
        flag = self.data.readInt32()
        if (flag==0x1CB5C415):
            count = self.data.readInt32()
            for x in range(0,count):
                users = users+str(self.data.readInt32())+","
        users=users+"\";"
        return {"message":"[TL_messageActionChatAddUser]","media":users}
    
    def TL_messageActionChatMigrateTo(self):
        channel_id = "Channel_ID:\""+str(self.data.readInt32())+"\";"
        return {"message":"[TL_messageActionChatMigrateTo]","media":channel_id}
    
    def TL_messageActionChannelMigrateTo(self):
        title="Title:\""+self.data.readString()+"\";"
        chat_id = "Chat_ID:\""+str(self.data.readInt32())+"\";"
        return {"message":"[TL_messageActionChatMigrateTo]","media":title+chat_id}
        
    def TL_userProfilePhoto(self):
        photo_id="Photo_ID:"+str(self.data.readInt64())+";"
        photo_small="Photo_Small:"+self.FileLocation()+";"
        photo_big="Photo_Big:"+self.FileLocation()+";"
        return {"message":"[TL_userProfilePhoto]","media":photo_id+photo_small+photo_big}
    
    def TL_userProfilePhoto_old(self):
        photo_small="Photo_Small:"+self.FileLocation()+";"
        photo_big="Photo_Big:"+self.FileLocation()+";"
        return {"message":"[TL_userProfilePhoto]","media":photo_small+photo_big}
        
    def TL_messageActionUserUpdatedPhoto(self):
        id = self.data.readInt32()
        if (id==0xD559D8C8):
            return self.TL_userProfilePhoto()
        elif (id==0x4F11BAE1):
            return {"message":"[TL_userProfilePhotoEmpty]"}
        elif (id==0x990D1493):
            return self.TL_userProfilePhoto_old()
        else:
            return {"message":"[TL_messageActionUserUpdatedPhoto, Unknown action: "+hex(id)+"]"}
    
    def TL_messageActionTTLChange(self):
        ttl = "TTL:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionTTLChange]","media":ttl}
    
    def TL_messageActionLoginUnknownLocation(self):
        title = "Title:"+self.data.readString()+";"
        address = "Address:"+self.data.readString()+";"
        return {"message":"[TL_messageActionLoginUnknownLocation]","media":title+address}
    
    def TL_messageActionChatAddUser_old(self):
        user_id = "User_ID:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionChatAddUser_old]","media":user_id}
    
    def TL_messageActionChatDeleteUser(self):
        user_id = "User_ID:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionChatDeleteUser]","media":user_id}
        
    def TL_messageActionGeoChatCreate(self):
        title = "Title:"+self.data.readString()+";"
        address = "Address:"+self.data.readString()+";"
        return {"message":"[TL_messageActionGeoChatCreate]","media":title+address}
        
    def TL_messageActionChatEditPhoto(self):
        photo=self.Photo()
        return {"message":"[TL_messageActionChatEditPhoto]","media":photo}
    
    def PhoneCallDiscardReason(self):
        subtype=self.data.readInt32()
        if (subtype==0x85E42301):
            return "TL_phoneCallDiscardReasonMissed"
        elif (subtype==0xE095C1A0):
            return "TL_phoneCallDiscardReasonDisconnect"
        elif (subtype==0xFAF7E8C9):
            return "TL_phoneCallDiscardReasonBusy"
        elif (subtype==0x57ADC690):
            return "TL_phoneCallDiscardReasonHangup"
        else:
            return "Unknown reason"
            
    def TL_messageActionPhoneCall(self):
        flags=self.data.readInt32()
        call_id="Call_ID:\""+str(self.data.readInt64())+"\";"
        reason=""
        duration=""
        if (flags&1)!=0:
            reason="Reason:"+self.PhoneCallDiscardReason()+";"
        if (flags&2)!=0:
            duration="Duration:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionPhoneCall]","media":call_id+reason+duration}
    
    def TL_messageActionGameScore(self):
        game_id="Game_Id:"+str(self.data.readInt64())+";"
        score="Score:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionGameScore]","media":game_id+score}
    
    def TL_messageActionChannelCreate(self):
        title="Title:\""+self.data.readString()+"\";"
        return {"message":"[TL_messageActionChannelCreate]","media":title}
    
    def TL_messageActionChatEditTitle(self):
        title="Title:\""+self.data.readString()+"\";"
        return {"message":"[TL_messageActionChatEditTitle]","media":title}
    
    def TL_messageActionChatJoinedByLink(self):
        inviter_id="Inviter_Id:"+str(self.data.readInt32())+";"
        return {"message":"[TL_messageActionChatJoinedByLink]","media":inviter_id}
    
    def TL_inputGroupCall(self):
        id="Id:"+str(self.data.readInt64())+";"
        access_hash="Access_Hash:"+str(self.data.readInt64())+";"
        return {"message":"[TL_inputGroupCall]","media":id+access_hash}
        
    def TL_messageActionGroupCall(self):
        id=self.data.readInt32()
        if (id==0xD8AA840F):
            return self.TL_messageEncryptedAction()
        else:
            return {"message":"[TL_messageActionGroupCall: Unknown id:"+hex(id)+"]"}
    
    def TL_decryptedMessageActionScreenshotMessages(self):
        flag = self.data.readInt32()
        random_ids="Random_Ids:"
        if (flag==0x1CB5C415):
            count = self.data.readInt32()
            for x in range(0,count):
                random_ids = random_ids+str(self.data.readInt64())+","
        random_ids=random_ids+"\";"
        return {"message":"[TL_decryptedMessageActionScreenshotMessages]","media":random_ids}

    def TL_decryptedMessageActionDeleteMessages(self):
        flag = self.data.readInt32()
        random_ids="Random_Ids:"
        if (flag==0x1CB5C415):
            count = self.data.readInt32()
            for x in range(0,count):
                random_ids = random_ids+str(self.data.readInt64())+","
        random_ids=random_ids+"\";"
        return {"message":"[TL_decryptedMessageActionDeleteMessages]","media":random_ids}
        
    def TL_decryptedMessageActionReadMessages(self):
        flag = self.data.readInt32()
        random_ids="Random_Ids:"
        if (flag==0x1CB5C415):
            count = self.data.readInt32()
            for x in range(0,count):
                random_ids = random_ids+str(self.data.readInt64())+","
        random_ids=random_ids+"\";"
        return {"message":"[TL_decryptedMessageActionReadMessages]","media":random_ids}
        
    def TL_decryptedMessageActionAcceptKey(self):
        exchange_id="Exchange_Id:"+str(self.data.readInt64())+";"
        g_b = self.data.readByteArray()
        g_b_v="G_B:\""
        for i in range(0,len(g_b)):
            g_b_v+=hex(int(g_b[i]))
        g_b_v+="\";"
        key_fingerprint = "Key_Fingerprint:"+str(self.data.readInt64())+";"
        return {"message":"[TL_decryptedMessageActionAcceptKey]","media":exchange_id+g_b_v+key_fingerprint}
        
    def TL_decryptedMessageActionSetMessageTTL(self):
        ttl_seconds = "TTL_Seconds:"+str(self.data.readInt32())+";"
        return {"message":"[TL_decryptedMessageActionSetMessageTTL]","media":ttl_seconds}
    
    def TL_decryptedMessageActionAbortKey(self):
        exchange_id = "Exchange_Id:"+str(self.data.readInt64())+";"
        return {"message":"[TL_decryptedMessageActionAbortKey]","media":exchange_id}
    
    def TL_decryptedMessageActionCommitKey(self):
        exchange_id = "Exchange_Id:"+str(self.data.readInt64())+";"
        key_fingerprint = "Key_Fingerprint:"+str(self.data.readInt64())+";"
        return {"message":"[TL_decryptedMessageActionCommitKey]","media":exchange_id+key_fingerprint}
    
    def TL_decryptedMessageActionNotifyLayer(self):
        layer = "Notify_Layer:"+str(self.data.readInt32())+";"
        return {"message":"[TL_decryptedMessageActionNotifyLayer]","media":layer}
        
    def TL_decryptedMessageActionRequestKey(self):
        exchange_id="Exchange_Id:"+str(self.data.readInt64())+";"
        g_a = self.data.readByteArray()
        g_a_v="G_A:\""
        for i in range(0,len(g_a)):
            g_a_v+=hex(int(g_a[i]))
        g_a_v+="\";"
        return {"message":"[TL_decryptedMessageActionRequestKey]","media":exchange_id+g_a_v}
    
    def TL_decryptedMessageActionResend(self):
        start_seq_no="Start_seq_no:"+str(self.data.readInt32())+";"
        end_seq_no="End_seq_no:"+str(self.data.readInt32())+";"
        return {"message":"[TL_decryptedMessageActionResend]","media":start_seq_no+end_seq_no}
        
    def TL_sendMessageUploadDocumentAction(self):
        progress="Progress:"+str(self.data.readInt32())+";"
        return {"message":"[TL_sendMessageUploadDocumentAction]","media":progress}

    def TL_sendMessageUploadPhotoAction(self):
        progress="Progress:"+str(self.data.readInt32())+";"
        return {"message":"[TL_sendMessageUploadPhotoAction]","media":progress}
    
    def TL_sendMessageUploadVideoAction(self):
        progress="Progress:"+str(self.data.readInt32())+";"
        return {"message":"[TL_sendMessageUploadVideoAction]","media":progress}

    def TL_sendMessageUploadAudioAction(self):
        progress="Progress:"+str(self.data.readInt32())+";"
        return {"message":"[TL_sendMessageUploadAudioAction]","media":progress}

    def TL_sendMessageUploadRoundAction(self):
        progress="Progress:"+str(self.data.readInt32())+";"
        return {"message":"[TL_sendMessageUploadRoundAction]","media":progress}
        
    def TL_decryptedMessageActionTyping(self):
        id=self.data.readInt32()
        type=self.getsendmessage(id)
        if (type=="TL_sendMessageGeoLocationAction"):
            return {"message":"[TL_sendMessageGeoLocationAction]"}
        elif (type=="TL_sendMessageChooseContactAction"):
            return {"message":"[TL_sendMessageChooseContactAction]"}
        elif (type=="TL_sendMessageRecordRoundAction"):
            return {"message":"[TL_sendMessageRecordRoundAction]"}
        elif (type=="TL_sendMessageUploadDocumentAction_old"):
            return {"message":"[TL_sendMessageUploadDocumentAction_old]"}
        elif (type=="TL_sendMessageUploadVideoAction_old"):
            return {"message":"[TL_sendMessageUploadVideoAction_old]"}
        elif (type=="TL_sendMessageUploadPhotoAction_old"):
            return {"message":"[TL_sendMessageUploadPhotoAction_old]"}
        elif (type=="TL_sendMessageRecordVideoAction"):
            return {"message":"[TL_sendMessageRecordVideoAction]"}
        elif (type=="TL_sendMessageUploadDocumentAction"):
            return self.TL_sendMessageUploadDocumentAction()
        elif (type=="TL_sendMessageUploadPhotoAction"):
            return self.TL_sendMessageUploadPhotoAction()
        elif (type=="TL_sendMessageRecordAudioAction"):
             return {"message":"[TL_sendMessageRecordVideoAction]"}
        elif (type=="TL_sendMessageGamePlayAction"):
            return {"message":"[TL_sendMessageGamePlayAction]"}
        elif (type=="TL_sendMessageUploadAudioAction_old"):
            return {"message":"[TL_sendMessageUploadAudioAction_old]"}
        elif (type=="TL_sendMessageUploadVideoAction"):
            return self.TL_sendMessageUploadVideoAction()
        elif (type=="TL_sendMessageUploadAudioAction"):
            return self.TL_sendMessageUploadAudioAction()
        elif (type=="TL_sendMessageCancelAction"):
            return {"message":"[TL_sendMessageCancelAction]"}
        elif (type=="TL_sendMessageTypingAction"):
            return {"message":"[TL_sendMessageTypingAction]"}
        elif (type=="TL_sendMessageUploadRoundAction"):
            return self.TL_sendMessageUploadRoundAction()
        else:
            return {"message":"[SendMessageAction: Unknown id:"+hex(id)+"]"}
            
    def TL_messageEncryptedAction(self):
        actionflag=self.data.readInt32()
        action=self.getdecryptedaction(actionflag)
        if (action=="TL_decryptedMessageActionDeleteMessages"):
            return self.TL_decryptedMessageActionDeleteMessages()
        elif (action=="TL_decryptedMessageActionFlushHistory"):
            return {"message":"[TL_decryptedMessageActionFlushHistory]"}
        elif (action=="TL_decryptedMessageActionAcceptKey"):
            return self.TL_decryptedMessageActionAcceptKey()
        elif (action=="TL_decryptedMessageActionScreenshotMessages"):
            return self.TL_decryptedMessageActionScreenshotMessages()
        elif (action=="TL_decryptedMessageActionSetMessageTTL"):
            return self.TL_decryptedMessageActionSetMessageTTL()
        elif (action=="TL_decryptedMessageActionNoop"):
            return {"message":"[TL_decryptedMessageActionNoop]"}
        elif (action=="TL_decryptedMessageActionTyping"):
            return self.TL_decryptedMessageActionTyping()
        elif (action=="TL_decryptedMessageActionAbortKey"):
            return self.TL_decryptedMessageActionAbortKey()
        elif (action=="TL_decryptedMessageActionCommitKey"):
            return self.TL_decryptedMessageActionCommitKey()
        elif (action=="TL_decryptedMessageActionNotifyLayer"):
            return self.TL_decryptedMessageActionNotifyLayer()
        elif (action=="TL_decryptedMessageActionRequestKey"):
            return self.TL_decryptedMessageActionRequestKey()
        elif (action=="TL_decryptedMessageActionReadMessages"):
            return self.TL_decryptedMessageActionReadMessages()
        elif (action=="TL_decryptedMessageActionResend"):
            return self.TL_decryptedMessageActionResend()
        else:
            return {"message":"[TL_messageEncryptedAction: Unknown id:"+hex(id)+"]"}
            
    def telegramaction(self):
        actionflag=self.data.readInt32()
        action=self.getaction(actionflag)

        if (action=="TL_messageActionGeoChatCheckin"):
            return {"message":"[TL_messageActionGeoChatCheckin]"}
        elif (action=="TL_messageActionPaymentSent"):
            return self.TL_messageActionPaymentSent()
        elif (action=="TL_messageActionScreenshotTaken"):
            return {"message":"[TL_messageActionScreenshotTaken]"}
        elif (action=="TL_messageActionChatAddUser"):
            return self.TL_messageActionChatAddUser()
        elif (action=="TL_messageActionChatMigrateTo"):
            return self.TL_messageActionChatMigrateTo()
        elif (action=="TL_messageActionUserJoined"):
            return self.TL_messageActionUserJoined()
        elif (action=="TL_messageActionUserUpdatedPhoto"):
            return self.TL_messageActionUserUpdatedPhoto()
        elif (action=="TL_messageActionTTLChange"):
            return self.TL_messageActionTTLChange()
        elif (action=="TL_messageActionCreatedBroadcastList"):
            return {"message":"[TL_messageActionCreatedBroadcastList]"}
        elif (action=="TL_messageActionLoginUnknownLocation"):
            return self.TL_messageActionLoginUnknownLocation()
        elif (action=="TL_messageEncryptedAction"):
            return self.TL_messageEncryptedAction()
        elif (action=="TL_messageActionChatAddUser_old"):
            return self.TL_messageActionChatAddUser_old()
        elif (action=="TL_messageActionGeoChatCreate"):
            return self.TL_messageActionGeoChatCreate()
        elif (action=="TL_messageActionChatEditPhoto"):
            return self.TL_messageActionChatEditPhoto()
        elif (action=="TL_messageActionPhoneCall"):
            return self.TL_messageActionPhoneCall()
        elif (action=="TL_messageActionGameScore"):
            return self.TL_messageActionGameScore()
        elif (action=="TL_messageActionPinMessage"):
            return {"message":"[TL_messageActionPinMessage]"}
        elif (action=="TL_messageActionChannelCreate"):
            return self.TL_messageActionChannelCreate()
        elif (action=="TL_messageActionChatDeletePhoto"):
            return {"message":"[TL_messageActionChatDeletePhoto]"}
        elif (action=="TL_messageActionHistoryClear"):
            return {"message":"[TL_messageActionHistoryClear]"}
        elif (action=="TL_messageActionChatCreate"):
            return self.TL_messageActionChatCreate()
        elif (action=="TL_messageActionChannelMigrateFrom"):
            return self.TL_messageActionChannelMigrateTo()
        elif (action=="TL_messageActionChatDeleteUser"):
            return self.TL_messageActionChatDeleteUser()
        elif (action=="TL_messageActionChatEditTitle"):
            return self.TL_messageActionChatEditTitle()
        elif (action=="TL_messageActionEmpty"):
            return {"message":"[TL_messageActionEmpty]"}
        elif (action=="TL_messageActionGroupCall"):
            return self.TL_messageActionGroupCall()
        elif (action=="TL_messageActionChatJoinedByLink"):
            return self.TL_messageActionChatJoinedByLink()
        elif (action=="TL_messageActionChatAddUser_old_v2"):
            return self.TL_messageActionChatAddUser_old_v2()
        elif (action=="TL_messageActionChatCreate_add_user"):
            return self.TL_messageActionChatCreate_add_user()
        elif (action=="action_user_info"):
            from_id=self.data.readInt32()
            to_id_user=self.Peer()
            to_id_date=self.data.readInt32()
            id_message=self.data.readInt32()
            return {"from_id":from_id, "to_id_user":to_id_user, "to_id_date":to_id_date, "message":message}
        else:
            return {"message":"[Unknown Action : "+hex(actionflag)+"]"}

    def gettelegramuser(self,userid):
        if userid not in self.usertable:
            if (userid) in self.chattable:
                    return self.chattable[userid]
            return str(userid)
        return self.usertable[userid]

    def gettelegramchat(self,chatid):
        if chatid not in self.chattable:
            return str(chatid)
        return "Group: "+self.chattable[chatid]

    def TL_peerUser(self):
        user_id=self.data.readInt32()
        return self.gettelegramuser(user_id)

    def TL_peerChat(self):
        chat_id=self.data.readInt32()
        return self.gettelegramchat(chat_id)
    
    def TL_peerChannel(self):
        channel_id=self.data.readInt32()
        return "Channel_ID: "+str(channel_id);
    
    def TL_messageFwdHeader(self):
        type=self.data.readInt32()
        if (type==0xC786DDCB):
            flags=self.data.readInt32()
            from_id=0
            if ((flags&1)!=0):
                from_id=self.data.readInt32()
            date=self.data.readInt32()
            channel_id=0
            if ((flags&2)!=0):
                channel_id=self.data.readInt32()
            channel_post=0
            if ((flags&4)!=0):
                channel_post=self.data.readInt32()
        else:
            from_id=type
            date=0
            channel_id=0
            channel_post=0
        return [from_id,date,channel_id,channel_post]

    def Peer(self):
        type=self.data.readInt32()
        if (type==0x9DB1BC6D):
            return self.TL_peerUser()
        elif (type==0xBAD0E5BB):
            return self.TL_peerChat()
        elif (type==0xBDDDE532):
            return self.TL_peerChannel()
        else:
            assert("Peer error")

    def TL_keyboardButton(self):
        type=self.data.readInt32()
        if (type==0xA2FA4880):
            return self.data.readString()
        return "Error on TL_keyboardButton"

    def TL_keyboardButtonRow(self):
        type=self.data.readInt32()
        str=""
        if (type==0x1CB5C415):
            count=self.data.readInt32()
            for i in range(count):
                str+=self.TL_keyboardButton()+";"
        return str

    def ReplyMarkup(self):
        type=self.data.readInt32()
        if (type==0xA03E5B85):
            if (((self.data.readInt32())&4)!=0):
                return "TL_replyKeyboardHide:true"
            else:
                return "TL_replyKeyboardHide:false"     
        elif (type==0xF4108AA0):
            if (((self.data.readInt32())&4)!=0):
                return "TL_replyKeyboardForceReply:true"
            else:
                return "TL_replyKeyboardForceReply:false"
        elif (type==0x3502758C):
            resize=self.data.readInt32()
            str=""
            if ((resize&1)!=0):
                str+="resize;"
            if ((resize&2)!=0):
                str+="single-use;"
            if ((resize&4)!=0):
                str+="selective;"
            #count=self.data.readInt32()
            #for i in range(count):
            #    str+=self.TL_keyboardButtonRow()+"|"
            return str
        return ""

    def MessageEntity(self):
        type=self.data.readInt32()
        return self.getmessageentity(type)+"[Offset:"+hex(self.data.readInt32())+";Length:"+hex(self.data.readInt32())+"]"

    def TL_message_handler(self):
        flags=0
        type=""
        message=""
        id=0
        from_id=0
        to_id_user=""
        fwd_from_id=0
        fwd_date=0
        reply_to_msg_id=0
        fwd_msg_id=0
        to_id_date=0
        date=""
        type=self.getmessage(self.data.readInt32())
        media=""
        tts=""
        if (type == "TL_message_old2"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
        elif (type == "TL_message_old3"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd_from_id = self.data.readInt32()
                fwd_date = self.data.readInt32()
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
            if (((flags & 4) != 0) and (id < 0)):
                fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message_old4"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd_from_id = self.data.readInt32()
                fwd_date = self.data.readInt32()
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
            if (((flags & 4) != 0) and (id < 0)):
                fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message_layer72"):
            flags = self.data.readInt32()
            media = ""
            from_id = 0
            if ((flags & 2) != 0):
                media = "Out;"
            if ((flags & 0x10) != 0):
                media = "Mentioned;"
            if ((flags & 0x20) != 0):
                media = "Media_Unread;"
            if ((flags & 0x2000) != 0):
                media = "Silent;"
            if ((flags & 0x4000) != 0):
                media = "Post;"
            id = self.data.readInt32()
            if ((flags & 0x100) != 0):
                from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if (from_id == 0):
                if "Channel_ID: " in to_id_user:
                    from_id = int(to_id_user[12:])
            if ((flags & 4) != 0):
                media += "Fwd["
                id = self.data.readInt32()
                if (id != 0xC786DDCB):
                    assert ("Unknown TL_messageFwdHeader")
                mflag = self.data.readInt32()
                if ((mflag & 1) != 0):
                    fwd_from_id = self.data.readInt32()
                    media += "From:" + str(fwd_from_id) + ";"
                fwd_date = self.data.readInt32()
                media += "Date:" + self.getDate(fwd_date) + ";"
                if ((mflag & 2) != 0):
                    fwd_channel_id = self.data.readInt32()
                    media += "ChannelID:" + str(fwd_channel_id) + ";"
                if ((mflag & 4) != 0):
                    fwd_channel_post = self.data.readInt32()
                    media += "ChannelPost:" + str(fwd_channel_post) + ";"
                media += "]"
            if ((flags & 0x800) != 0):
                via_bot_id = self.data.readInt32()
                media += "ViaBotId[" + hex(via_bot_id) + "]"
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            if ((flags & 0x200) != 0):  # Fix me
                media = self.telegrammedia()
            if ((flags & 0x40) != 0):
                reply = self.ReplyMarkup()
            if ((flags & 0x80 != 0)):
                hash = self.data.readInt32()
                if (hash == 0x1CB5C415):
                    counter = self.data.readInt32()
                    for i in range(counter):
                        media += ";MessageEntity: " + self.MessageEntity()
            else:
                if ((flags & 0x4000) != 0):  # Fix me
                    views = self.data.readInt32()
                if ((flags & 0x8000) != 0):
                    edit_date = self.data.readInt32()
                if ((flags & 0x10000) != 0):
                    post_author = self.data.readInt32()
                if ((id < 0) and (media != "Empty") and (message != "")):
                    attachPath = self.data.readString()
                    media += "AttachPath: " + attachPath
                if (((flags & 4) != 0) or (id < 0)):
                    fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message"):
            flags = self.data.readInt32()
            media = ""
            from_id = 0
            if ((flags & 2) != 0):
                media = "Out;"
            if ((flags & 0x10) != 0):
                media = "Mentioned;"
            if ((flags & 0x20) != 0):
                media = "Media_Unread;"
            if ((flags & 0x2000) != 0):
                media = "Silent;"
            if ((flags & 0x4000) != 0):
                media = "Post;"
            id = self.data.readInt32()
            if ((flags & 0x100) != 0):
                from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if (from_id == 0):
                if "Channel_ID: " in to_id_user:
                    from_id = int(to_id_user[12:])
            if ((flags & 4) != 0):
                media += "Fwd["
                id = self.data.readInt32()
                if (id != 0xC786DDCB):
                    assert ("Unknown TL_messageFwdHeader")
                mflag = self.data.readInt32()
                if ((mflag & 1) != 0):
                    fwd_from_id = self.data.readInt32()
                    media += "From:" + str(fwd_from_id) + ";"
                fwd_date = self.data.readInt32()
                media += "Date:" + self.getDate(fwd_date) + ";"
                if ((mflag & 2) != 0):
                    fwd_channel_id = self.data.readInt32()
                    media += "ChannelID:" + str(fwd_channel_id) + ";"
                if ((mflag & 4) != 0):
                    fwd_channel_post = self.data.readInt32()
                    media += "ChannelPost:" + str(fwd_channel_post) + ";"
                media += "]"
            if ((flags & 0x800) != 0):
                via_bot_id = self.data.readInt32()
                media += "ViaBotId[" + hex(via_bot_id) + "]"
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            if ((flags & 0x200) != 0):  # Fix me
                media = self.telegrammedia()
            if ((flags & 0x40) != 0):
                reply = self.ReplyMarkup()
            if ((flags & 0x80 != 0)):
                hash = self.data.readInt32()
                if (hash == 0x1CB5C415):
                    counter = self.data.readInt32()
                    for i in range(counter):
                        media += ";MessageEntity: " + self.MessageEntity()
            else:
                if ((flags & 0x4000) != 0):  # Fix me
                    views = self.data.readInt32()
                if ((flags & 0x8000) != 0):
                    edit_date = self.data.readInt32()
                if ((flags & 0x10000) != 0):
                    post_author = self.data.readInt32()
                if ((flags & 0x20000) != 0):
                    grouped_id = self.data.readInt64()
        elif (type == "TL_message_layer68"):
            flags = self.data.readInt32()
            media = ""
            from_id = 0
            if ((flags & 1) != 0):
                media = "Unread;"
            if ((flags & 2) != 0):
                media = "Out;"
            if ((flags & 16) != 0):
                media = "Mentioned;"
            if ((flags & 32) != 0):
                media = "Media_Unread;"
            if ((flags & 0x2000) != 0):
                media = "Silent;"
            if ((flags & 0x4000) != 0):
                media = "Post;"
            id = self.data.readInt32()
            if ((flags & 0x100) != 0):
                from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if (from_id == 0):
                if "Channel_ID: " in to_id_user:
                    from_id = int(to_id_user[12:])
            if ((flags & 4) != 0):
                media += "Fwd["
                id = self.data.readInt32()
                if (id != 0xC786DDCB):
                    assert ("Unknown TL_messageFwdHeader")
                mflag = self.data.readInt32()
                if ((mflag & 1) != 0):
                    fwd_from_id = self.data.readInt32()
                    media += "From:" + str(fwd_from_id) + ";"
                fwd_date = self.data.readInt32()
                media += "Date:" + self.getDate(fwd_date) + ";"
                if ((mflag & 2) != 0):
                    fwd_channel_id = self.data.readInt32()
                    media += "ChannelID:" + str(fwd_channel_id) + ";"
                if ((mflag & 4) != 0):
                    fwd_channel_post = self.data.readInt32()
                    media += "ChannelPost:" + str(fwd_channel_post) + ";"
                media += "]"
            if ((flags & 0x800) != 0):
                via_bot_id = self.data.readInt32()
                media += "ViaBotId[" + hex(via_bot_id) + "]"
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            if ((flags & 0x200) != 0):  # Fix me
                media = self.telegrammedia()
            # if ((flags&0x40)!=0):
            #    reply=self.ReplyMarkup()
            # if((flags&0x80!=0)):
            #    hash=self.data.readInt32()
            #    if (hash==0x1CB5C415):
            #        counter=self.data.readInt32()
            #        for i in range(counter):
            #            media+=";MessageEntity: "+self.MessageEntity()
            # else:
            # if ((flags&0x4000)!=0): #Fix me
            #    views=self.data.readInt32()
            # if ((flags&0x8000)!=0):
            #    edit_date=self.data.readInt32()
            # if ((id<0) and (media!="Empty") and (message!="")):
            #    attachPath=self.data.readString()
            #    media+="AttachPath: "+attachPath
            # if (((flags & 4)!=0) and (id <0)):
            #    fwd_msg_id=self.data.readInt32()
        elif (type == "TL_message_layer47"):
            flags = self.data.readInt32()
            media = ""
            if ((flags & 1) != 0):
                media = "Unread;"
            if ((flags & 2) != 0):
                media = "Out;"
            if ((flags & 0x10) != 0):
                media = "Mentioned;"
            if ((flags & 0x20) != 0):
                media = "Media_Unread;"
            id = self.data.readInt32()
            if ((flags & 0x100) != 0):
                from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd = self.TL_messageFwdHeader()
                fwd_from = fwd[0]
                fwd_date = fwd[1]
                fwd_channel_id = fwd[2]
                if fwd_channel_id != 0:
                    media += "Channel_ID[" + str(fwd_channel_id) + "]"
                fwd_channel_post = fwd[3]
                if fwd_channel_post != 0:
                    media += "Channel_Post[" + str(fwd_channel_post) + "]"
                fwd_from_id = self.Peer()
                fwd_date = self.data.readInt32()
            if ((flags & 0x800) != 0):
                via_bot_id = self.data.readInt32()
                media += "ViaBotId[" + hex(via_bot_id) + "]"
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            if ((flags & 64) != 0):
                reply = self.ReplyMarkup()
            if ((flags & 512) != 0):
                media += self.telegrammedia()
            else:
                v = self.data.readInt32()
                media += "Empty"
            if ((flags & 128 != 0)):
                hash = self.data.readInt32()
                if (hash == 0x1CB5C415):
                    counter = self.data.readInt32()
                    for i in range(counter):
                        media += ";MessageEntity: " + self.MessageEntity()
            else:
                if ((flags & 1024) != 0):
                    views = self.data.readInt32()
                if ((id < 0) and (media != "Empty") and (message != "")):
                    attachPath = self.data.readString()
                    media += "AttachPath: " + attachPath
                if (((flags & 4) != 0) and (id < 0)):
                    fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message_old6"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd_from_id = self.data.readInt32()
                fwd_date = self.data.readInt32()
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            if ((flags & 64) != 0):
                reply = self.ReplyMarkup()
            if ((flags & 512) != 0):
                media = self.telegrammedia()
            else:
                v = self.data.readInt32()
                media = "Media: Empty"
            if ((flags & 128 != 0)):
                hash = self.data.readInt32()
                if (hash == 0x1CB5C415):
                    counter = self.data.readInt32()
                    for i in range(counter):
                        media += ";MessageEntity: " + self.MessageEntity()
            else:
                if ((id < 0) and (media != "Empty") and (message != "")):
                    attachPath = self.data.readString()
                    media += "AttachPath: " + attachPath
                if (((flags & 4) != 0) and (id < 0)):
                    fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message_old7"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            if ((flags & 0x100) != 0):
                from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd = self.TL_messageFwdHeader()
                fwd_from = fwd[0]
                fwd_date = fwd[1]
                fwd_channel_id = fwd[2]
                if fwd_channel_id != 0:
                    media += "Channel_ID[" + str(fwd_channel_id) + "]"
                fwd_channel_post = fwd[3]
                if fwd_channel_post != 0:
                    media += "Channel_Post[" + str(fwd_channel_post) + "]"
                fwd_from_id = self.Peer()
                fwd_date = self.data.readInt32()
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            # print("Debug: id date: "+hex(to_id_date))
            message = self.data.readString()
            if ((flags & 0x200) != 0):
                media = self.telegrammedia()
            else:
                media = "Media: Empty"
            if ((flags & 64) != 0):
                reply = self.ReplyMarkup()
            if ((flags & 128 != 0)):
                hash = self.data.readInt32()
                if (hash == 0x1CB5C415):
                    counter = self.data.readInt32()
                    for i in range(counter):
                        media += ";MessageEntity: " + self.MessageEntity()
            else:
                if ((id < 0) and (media != "Empty") and (message != "")):
                    attachPath = self.data.readString()
                    media += "AttachPath: " + attachPath
                if (((flags & 4) != 0) and (id < 0)):
                    fwd_msg_id = self.data.readInt32()
        elif (type == "TL_message_old"):
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            flags = 0
            if (self.data.readBool()):
                flags = flags | 2
            if (self.data.readBool()):
                flags = flags | 1
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
        elif (type == "TL_message_secret_old"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            tts = str(self.data.readInt32())
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
        elif (type == "TL_message_secret_layer72"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            ttl = self.data.readInt32()
            tts = ""
            if (ttl > 0): str(self.data.readInt32())
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            oldmessage = message
            if message[0:2] == "-1":
                message = "[Media File]"
            if (self.data.readInt32() == 0x1CB5C415):
                counter = self.data.readInt32()
                for i in range(counter):
                    media += ";MessageEntity: " + self.MessageEntity()
                if ((flags & 0x800) != 0):
                    message = "[Via Bot:" + self.data.readString() + "] " + message
                if ((flags & 8) != 0):
                    message = "[Reply to random id: " + hex(self.data.readInt64()) + "] " + message
                if (id >= 0):
                    if oldmessage[0:2] == "-1":
                        message = "[AttachPath: " + self.data.readString() + "]"
        elif (type == "TL_message_secret"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            ttl = self.data.readInt32()
            tts = ""
            if (ttl > 0): str(self.data.readInt32())
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            media = self.telegrammedia()
            oldmessage = message
            if message[0:2] == "-1":
                message = "[Media File]"
            if (self.data.readInt32() == 0x1CB5C415):
                counter = self.data.readInt32()
                for i in range(counter):
                    media += ";MessageEntity: " + self.MessageEntity()
                if ((flags & 0x800) != 0):
                    message = "[Via Bot:" + self.data.readString() + "] " + message
                if ((flags & 8) != 0):
                    message = "[Reply to random id: " + hex(self.data.readInt64()) + "] " + message
                if ((flags & 0x20000) != 0):
                    grouped_id=self.data.readInt32()
        elif (type == "TL_messageService_old2"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            to_id_date = self.data.readInt32()
            action = self.telegramaction()
            if "message" in action:
                message = action["message"]
            if "media" in action:
                media = action["media"]
        elif (type == "TL_messageService_old"):
            id = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            flags = 0
            if (self.data.readBool()):
                flags = flags | 2
            if (self.data.readBool()):
                flags = flags | 1
            to_id_date = self.data.readInt32()
            action = self.telegramaction()
            if "message" in action:
                message = action["message"]
            if "media" in action:
                media = action["media"]
        elif (type == "TL_messageService_layer48"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            ddata = {}
            if ((flags & 0x100) != 0):
                ddata["from_id"] = self.data.readInt32()
                ddata["to_id_user"] = self.Peer()
                ddata["to_id_date"] = self.data.readInt32()
                action = self.telegramaction()
                if "message" in action:
                    ddata["message"] = action["message"]
                if "media" in action:
                    ddata["media"] = action["media"]
                # from_id=self.data.readInt32()
            if "from_id" in ddata:
                from_id = ddata["from_id"]
            else:
                from_id = 0
                # to_id_user=self.Peer()
            if "to_id_user" in ddata:
                to_id_user = ddata["to_id_user"]
            else:
                to_id_user = ""
                # to_id_date=self.data.readInt32()
            if "to_id_date" in ddata:
                to_id_date = ddata["to_id_date"]
                # message=self.telegramaction()
            if "message" in ddata:
                message = ddata["message"]
            else:
                message = ""
        elif (type == "TL_messageService"):
            flags = self.data.readInt32()
            id = self.data.readInt32()
            ddata = {}
            if ((flags & 0x100) != 0):
                ddata["from_id"] = self.data.readInt32()
            ddata["to_id_user"] = self.Peer()
            if ((flags & 8)!=0):
                from_id = self.data.readInt32()
            ddata["to_id_date"] = self.data.readInt32()
            
            action = self.telegramaction()
            #print(action)
            if "message" in action:
                message = action["message"]
            if "media" in action:
                media = action["media"]
            if "from_id" in ddata:
                from_id = ddata["from_id"]
            else:
                from_id = 0
                # to_id_user=self.Peer()
            if "to_id_user" in ddata:
                to_id_user = ddata["to_id_user"]
            else:
                to_id_user = ""
                # to_id_date=self.data.readInt32()
            if "to_id_date" in ddata:
                to_id_date = ddata["to_id_date"]
                # message=self.telegramaction()
            if "message" in ddata:
                message = ddata["message"]
            else:
                message = ""
            
        elif (type == "TL_messageForwarded_old"):
            id = self.data.readInt32()
            fwd_from_id = self.data.readInt32()
            fwd_date = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            flags = 0
            if (self.data.readBool()):
                flags = flags | 2
            if (self.data.readBool()):
                flags = flags | 1
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            flags |= 4
            media = self.telegrammedia()
            if (id < 0):
                fwd_msg_id = self.data.readInt32()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
        elif (type == "TL_messageForwarded_old2"):
            type = "TL_messageForwarded_old2"
            flags = self.data.readInt32()
            id = self.data.readInt32()
            fwd_from_id = self.data.readInt32()
            fwd_date = self.data.readInt32()
            from_id = self.data.readInt32()
            to_id_user = self.Peer()
            if ((flags & 4) != 0):
                fwd_from_id = self.data.readInt32()
                fwd_date = self.data.readInt32()
            if ((flags & 8) != 0):
                reply_to_msg_id = self.data.readInt32()
            to_id_date = self.data.readInt32()
            message = self.data.readString()
            flags |= 4
            media = self.telegrammedia()
            if (id < 0):
                fwd_msg_id = self.data.readInt32()
            if ((id < 0) and (media != "Empty") and (message != "")):
                attachPath = self.data.readString()
                media += "AttachPath: " + attachPath
            # if ((id<0) and (len(message)>6) and ("Video" in media)):
            #    media+=VideoEditedInfo()
            else:
                message = "[Unknown type: " + type + "]"
        return flags, from_id, fwd_date, fwd_from_id, fwd_msg_id, id, media, message, reply_to_msg_id, to_id_date, to_id_user, tts, type

    def run(self):
        result={}
        if len(self.textdata)>4:
            self.data = JavaFunc(self.textdata)
            flags, from_id, fwd_date, fwd_from_id, fwd_msg_id, id, media, message, reply_to_msg_id, to_id_date, to_id_user, tts, type = self.TL_message_handler()
            result["type"]=type #TL_TYPE
            result["id"]=str(id) #TL_ID
            result["from_id"]=self.gettelegramuser(from_id)    #TL_FROM_ID
            result["to_id_user"]=self.gettelegramuser(to_id_user) #TL_TO_USER_ID
            result["flags"]=self.telegramflag(flags) #TL_FLAG
            result["to_id_date"]=to_id_date #TL_DATE
            result["message"]=message #TL_DATA
            result["media"]=media #TL_MEDIA
            result["tts"]=tts #TL_TTS
            result["fwd_from_id"]=self.gettelegramuser(fwd_from_id) #FWD_FROM_ID
            result["fwd_date"]=fwd_date #FWD_DATE
            result["reply_to_msg_id"]=str(reply_to_msg_id) #REPLY_TO_MSG_ID
            result["fwd_msg_id"]=str(fwd_msg_id) #fwd_msg_id
            result["media_filename"]=""
        if len(self.mediadata)>4:
            self.data = JavaFunc(self.mediadata)
            flags2, from_id2, fwd_date2, fwd_from_id2, fwd_msg_id2, id2, media2, message2, reply_to_msg_id2, to_id_date2, to_id_user2, tts2, type2 = self.TL_message_handler()
            #print("a-%s|b-%s|c-%s|d-%s|e-%s|f-%s|g-%s|h-%s|i-%s|j-%s|k-%s|l-%s|m-%s" % (flags2, from_id2, fwd_date2, fwd_from_id2, fwd_msg_id2, id2, media2, message2, reply_to_msg_id2, to_id_date2, to_id_user2, tts2, type2))
            fname=self.data.readString()
            fname=fname.replace("/storage/emulated/","/media/")
            result["media_filename"]=fname
            #/storage/emulated/0/Android/data/org.telegram.messenger/cache/-2147483648_-210156.jpg
        return result

