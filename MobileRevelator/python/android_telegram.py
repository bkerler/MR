#Pluginname="Telegram Messages (Android)"
#Filename="cache4.db"
#Type=App

import struct
from Library.telegram import Telegram
from PythonQt import QtCore
from Library import thumbnail

def getusers(db):
  conn=ctx.sqlite_run_cmd(db,"SELECT name,uid FROM users;")
  usertable={}
  for i in range(ctx.sqlite_get_data_size(conn)[0]):
    name=ctx.sqlite_get_data(conn,i,0)
    id=ctx.sqlite_get_data(conn,i,1)
    if name is None:
      continue
    if name[-3:]==";;;":
     name=name[:-3]
    if ";;;" in name:
     name=name.replace(";;;"," (")
     name=name+")"
    aUser=name.split(" ")
    for n in range(0, len(aUser)):
     aUser[n]=aUser[n].capitalize()
    name=" ".join(aUser)
    usertable[id]=name
  ctx.sqlite_cmd_close(conn)
  return usertable

def getchat(db):
  conn=ctx.sqlite_run_cmd(db,"SELECT name,uid FROM chats;")
  userchat={}
  for i in range(ctx.sqlite_get_data_size(conn)[0]):
    name=ctx.sqlite_get_data(conn,i,0)
    id=ctx.sqlite_get_data(conn,i,1)
    userchat[id]=name
  ctx.sqlite_cmd_close(conn)
  return userchat
 
def convertdata(table,dataidx,db):
    colidx=ctx.sqlite_get_headers(table).index("TL_TYPE (QString)")
    conn=ctx.sqlite_run_cmd(db,"SELECT messages.rowid, messages.data as messagedata, media_v2.data as mediadata, messages.mid from messages LEFT OUTER JOIN media_v2 ON messages.mid=media_v2.mid;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    if (rows==0):
        return
    ctx.gui_setMainProgressBar(0)
    oldpos=0
    usertable=getusers(db)
    userchat=getchat(db)
    for i in range(0,rows):
        newpos=int(i/rows*100);
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        if (ctx.sqlite_get_data(conn,i,1) is None):
            continue
        rowid=ctx.sqlite_get_data(conn,i,0)
        #print("Debug Idx: "+str(rowid))
        value=ctx.sqlite_get_data(conn,i,1).data()
        mediavalue=QtCore.QByteArray(ctx.sqlite_get_data(conn,i,2)).data()
        telgram = Telegram(value,mediavalue,usertable,userchat)
        result=telgram.run()
        ctx.sqlite_set_data(table,i,colidx,result["type"])    #TL_TYPE
        ctx.sqlite_set_data(table,i,colidx+1,str(result["id"])) #TL_ID
        ctx.sqlite_set_data(table,i,colidx+2,result["from_id"])    #TL_FROM_ID
        ctx.sqlite_set_data(table,i,colidx+3,result["to_id_user"]) #TL_TO_USER_ID
        ctx.sqlite_set_data(table,i,colidx+4,result["flags"]) #TL_FLAG
        if (result["to_id_date"]>0):
            ctx.sqlite_set_data(table,i,colidx+5,ctx.gui_getDate(result["to_id_date"])) #TL_DATE
        else:
            ctx.sqlite_set_data(table,i,colidx+5,str(result["to_id_date"])) #TL_DATE
        
        ctx.sqlite_set_data(table,i,dataidx,result["message"]) #TL_DATA
        ctx.sqlite_set_data(table,i,colidx+6,result["media"]) #TL_MEDIA
        ctx.sqlite_set_data(table,i,colidx+7,result["tts"]) #TL_TTS
        ctx.sqlite_set_data(table,i,colidx+8,result["fwd_from_id"]) #FWD_FROM_ID
        if (result["fwd_date"]>0):
            ctx.sqlite_set_data(table,i,colidx+9,ctx.gui_getDate(result["fwd_date"])) #FWD_DATE
        else:
            ctx.sqlite_set_data(table,i,colidx+9,str(result["fwd_date"])) #FWD_DATE
        ctx.sqlite_set_data(table,i,colidx+10,result["reply_to_msg_id"]) #REPLY_TO_MSG_ID
        ctx.sqlite_set_data(table,i,colidx+11,result["fwd_msg_id"]) #fwd_msg_id
        medianame=result["media_filename"]
        medianame=medianame.replace("/storage/emulated/","/media/")
        if medianame!="" and medianame is not None:
            ret=thumbnail.generate(ctx,medianame)
            ctx.sqlite_set_data(table,i,colidx+12,medianame)
            if (ret!=-1):
                ctx.sqlite_set_data(table,i,colidx+13,QtCore.QByteArray(bytes(ret[1])))
        else:
            ctx.sqlite_set_data(table,i,colidx+12,"")
            ctx.sqlite_set_data(table,i,colidx+13,"")
    ctx.gui_setMainProgressBar(100)
    ctx.sqlite_cmd_close(conn)


def converttimecolumn(table,dateidx,db):
    for i in range(0,ctx.sqlite_get_data_size(table)[0]):
        val=ctx.sqlite_get_data(table,i,dateidx)
        if ((val!=None) and (val>0)):
            conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
            ctx.sqlite_set_data(table,i,dateidx,ctx.sqlite_get_data(conn,0,0))
            ctx.sqlite_cmd_close(conn)

def searchandreplace(table,idx,search,replace):
    for i in range(0,ctx.sqlite_get_data_size(table)[0]):
        if (search==ctx.sqlite_get_data(table,i,idx)):
            ctx.sqlite_set_data(table,i,idx,replace)

def main():
    ctx.gui_setMainLabel("Telegram: Seeking messages")
    db=ctx.sqlite_open("gui",True)
    table=ctx.sqlite_run_cmd(db,"SELECT * from messages;")
    if table==-1:
        error="Error on query: SELECT * from messages;"
        return error
    rows=ctx.sqlite_get_data_size(table)[0]
    print(rows)
    if (rows==0):
        ctx.gui_update(table)
        ctx.gui_setMainLabel("Status: Idle.")
        return "Finished running plugin."
    ctx.gui_setMainLabel("Telegram Plugin: Converting Date Field");
    dateidx=ctx.sqlite_get_headers(table).index("date (int)")
    converttimecolumn(table,dateidx,db)

    ctx.gui_setMainLabel("Telegram Plugin: Replacing values");
    searchandreplace(table,ctx.sqlite_get_headers(table).index("read_state (int)"),1,"yes")
    searchandreplace(table,ctx.sqlite_get_headers(table).index("read_state (int)"),0,"no")
    searchandreplace(table,ctx.sqlite_get_headers(table).index("out (int)"),1,"sent")
    searchandreplace(table,ctx.sqlite_get_headers(table).index("out (int)"),0,"received")

    ctx.gui_setMainLabel("Telegram Plugin: Converting Data");
    dataidx=ctx.sqlite_get_headers(table).index("data (QByteArray)")
    ctx.sqlite_add_column(table,"TL_TYPE (QString)")
    ctx.sqlite_add_column(table,"TL_ID (int)")
    ctx.sqlite_add_column(table,"TL_FROM_ID (QString)")
    ctx.sqlite_add_column(table,"TL_TO_USER_ID (int)")
    ctx.sqlite_add_column(table,"TL_FLAG (QString)")
    ctx.sqlite_add_column(table,"TL_DATE (QString)")
    ctx.sqlite_add_column(table,"TL_MEDIA (QString)")
    ctx.sqlite_add_column(table,"TL_TTS (int)")
    ctx.sqlite_add_column(table,"FWD_FROM_ID (int)")
    ctx.sqlite_add_column(table,"FWD_DATE (int)")
    ctx.sqlite_add_column(table,"REPLY_TO_MSG_ID (int)")
    ctx.sqlite_add_column(table,"FWD_MSG_ID (int)")
    ctx.sqlite_add_column(table,"MEDIA_FILENAME (int)")
    ctx.sqlite_add_column(table,"MEDIA_THUMBNAIL (QByteArray)")
    convertdata(table,dataidx,db)
    ctx.gui_update(table)
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.sqlite_close(db)
    return "Finished running plugin."