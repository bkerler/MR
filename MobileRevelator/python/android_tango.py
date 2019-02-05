#Pluginname="Tango Messenger (Android)"
#Filename="tc.db"
#Type=App

import struct
import base64
import codecs
import sys
from Library import protobuf
from enum import Enum

class tango_direction (Enum):
    Both = 3
    Dir_None = 0
    Received = 2
    Sent = 1

class tango_id(Enum):
    conversation_id = 2
    type=3
    text=4
    url=5
    thumbnail_url=6
    thumbnail_path=7
    size=8
    duration=9
    media_id=10
    is_ecard=11
    vgood_bundle=12
    product=13
    text_if_not_support=14
    path=15
    original_type=16
    web_page_url=17
    width=18
    height=19
    should_video_be_trimmed=20
    peer_field=21
    time_send=22
    message_id=23
    send_status=24
    robot_message=25
    is_from_me=26
    is_for_update=27
    loading_status=28
    time_created=29
    progress=30
    time_peer_read=31
    channel=41
    read=42
    server_share_id=43
    is_offline=44
    sender_msg_id=45
    sender_jid=46
    peer_cap=47
    is_forwarded=48
    video_rotation=49
    recorder_able_playback=50
    video_trimmer_start_timestamp=61
    video_trimmer_end_timestamp=62
    media_source_type=63

    server_text=76

class Tango_ConversationMessageType(Enum):
    PEER_IN_CHAT_GAMING_MESSAGE = 81
    PEER_TYPING_MESSAGE = 60
    PRODUCT_CLIPBOARD_MESSAGE = 56
    PRODUCT_CLIPBOARD_V2_MESSAGE = 66
    PROFILE_MESSAGE = 34
    READ_RECEIPT_MESSAGE = 10
    REMINDER_MESSAGE = 87
    ROOMS_ACTIVE_IN_ROOM_NOTIF = 74
    ROOMS_CHATMESSAGE_LIKE_NOTIF = 71
    ROOMS_HEAT_UP_NOTIF = 75
    ROOMS_INVITE_MESSAGE = 70
    ROOMS_MENTION_NOTIF = 73
    ROOMS_MESSAGE_FLAGGED_NOTIF = 76
    ROOMS_PROMO = 72
    SDK_NOTIFICATION_MSG_TYPE = 23
    SINGLE_PRODUCT_MESSAGE = 55
    SINGLE_PRODUCT_V2_MESSAGE = 65
    SOCIAL_BE_FRIENDS_MESSAGE = 14
    SOCIAL_BIRTHDAY_REMINDER_MESSAGE = 44
    SOCIAL_COMMENT_MESSAGE = 41
    SOCIAL_FRIEND_REQUEST_MESSAGE = 42
    SOCIAL_FRIEND_RESPONSE_MESSAGE = 43
    SOCIAL_LIKE_MESSAGE = 40
    SOCIAL_LIKE_PROFILE_MESSAGE = 45
    SOCIAL_MUTUAL_FAVORITE_MESSAGE = 48
    SOCIAL_POST_MESSAGE = 33
    SOCIAL_POST_WITH_IMAGE_MESSAGE = 37
    SOCIAL_POST_WITH_VIDEO_MESSAGE = 38
    SOCIAL_REPOST_MESSAGE = 47
    SOCIAL_REPOST_MESSAGE_OBSOLETED = 46
    SOCIAL_REQUEST_UPLOAD_FEED_PHOTO_MESSAGE = 16
    SOCIAL_REQUEST_UPLOAD_PROFILE_PHOTO_MESSAGE = 15
    SPOTIFY_MESSAGE = 30
    STATUS_MESSAGE = 53
    STICKER_MESSAGE = 58
    SYSTEM_MESSAGE = 9
    TEXT_MESSAGE = 0
    TIMELINE_MESSAGE = 8
    ALBUM_MESSAGE = 0x39
    AUDIO_MESSAGE = 2
    BIRTHDAY_MESSAGE = 0x33
    EXTERNAL_MESSAGE = 0x14
    EXTERNAL_MESSAGE_WITH_IMAGE = 0x15
    EXTERNAL_MESSAGE_WITH_VIDEO = 0x16
    EXTERNAL_VIDEO_MESSAGE = 0x34
    GIFTED_VGOOD_PACK_MESSAGE = 6
    GROUP_CHAT_JOIN_MESSAGE = 0xB
    GROUP_CHAT_LEAVE_MESSAGE = 0xC
    GROUP_CHAT_NAME_MESSAGE = 0xD
    IMAGE_MESSAGE = 3
    LOCATION_MESSAGE = 4
    MISSED_CALL_MESSAGE = 0x24
    MOOD_MESSAGE = 0x1F
    MUSIC_MESSAGE = 0x20
    NORMAL_CALL_MESSAGE = 0x23
    VGOOD_MESSAGE = 5
    VIDEO_MESSAGE = 1
    WEB_LINK_MESSAGE = 0x32
    YFJ_V2_MESSAGE = 0x27

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select messages.rowid, messages.conv_id, profile.profiletable.itemFirstName, profile.profiletable.itemLastName, messages.type, messages.media_id, messages.share_id, datetime(messages.send_time/1000,'unixepoch','localtime'), messages.direction, messages.status, messages.payload, messages.del_status from messages LEFT JOIN profile.profiletable ON profile.profiletable.itemUserId = messages.conv_id;")
    if conn==-1:
      conn=ctx.sqlite_run_cmd(db,"select rowid, conv_id, NULL, NULL, type, media_id, share_id, datetime(send_time/1000,'unixepoch','localtime'), direction, status, payload, del_status from messages;")
      if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        conv_id=ctx.sqlite_get_data(conn,i,1)
        name=str(ctx.base64todata(ctx.sqlite_get_data(conn,i,2),1))
        if (name!=""): 
            name+=" "
        name+=str(ctx.base64todata(ctx.sqlite_get_data(conn,i,3),1))
        type=ctx.sqlite_get_data(conn,i,4)
        media_id=ctx.sqlite_get_data(conn,i,5)
        share_id=ctx.sqlite_get_data(conn,i,6) 
        send_time=ctx.sqlite_get_data(conn,i,7)
        direction=ctx.sqlite_get_data(conn,i,8)
        status=ctx.sqlite_get_data(conn,i,9)
        payload=ctx.base64todata(ctx.sqlite_get_data(conn,i,10),1)
        del_status=ctx.sqlite_get_data(conn,i,11)
        prbuf=protobuf.protobuf(payload.data())
        tangodata=prbuf.readAllFields()
        message=""
        is_from_me=""
        url=""
        if tango_id.text.value in tangodata:
           message=tangodata[tango_id.text.value].decode('utf8')
        if (message=="") and (tango_id.server_text.value in tangodata):
           message=tangodata[tango_id.server_text.value].decode('utf8')
        if (tango_id.url.value in tangodata):
           url=tangodata[tango_id.url.value].decode('utf8') 
        if tango_id.is_from_me.value in tangodata:
           is_from_me=str(tangodata[tango_id.is_from_me.value])
        try:
            direction=tango_direction(direction).name
            type=Tango_ConversationMessageType(type).name
        except:
            type=type
        
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,conv_id)
        ctx.gui_set_data(i,2,name)
        ctx.gui_set_data(i,3,type)
        ctx.gui_set_data(i,4,media_id)
        ctx.gui_set_data(i,5,share_id)
        ctx.gui_set_data(i,6,send_time)
        ctx.gui_set_data(i,7,direction)
        ctx.gui_set_data(i,8,status)
        ctx.gui_set_data(i,9,message)
        ctx.gui_set_data(i,10,url)
        ctx.gui_set_data(i,11,payload)
        ctx.gui_set_data(i,12,del_status)
    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","conv_id (QByteArray)","name (QString)","type (int)","media_id (QByteArray)","share_id (QByteArray)","send_time (int)","direction (int)", "status (int)", "text (QString)", "url (QString)", "payload (QByteArray)", "del_status (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Tango Messenger: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."