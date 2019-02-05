#Pluginname="Telegram (Android,FS)"
#Category="Reports"
#Type=FS

import struct
import os
import tempfile
from Library.java import JavaFunc
from Library.telegram import Telegram

def findtelegram():
    #Lets see where the db navigator files are
    ctx.gui_setMainLabel("Seeking for Telegram database")
    result={}
    
    for datadir in ["/data/org.telegram.messenger/files/cache4.db","org.telegram.messenger/files/cache4.db"]:
        if (ctx.fs_isFile(datadir)==True):
            result["Data"]=datadir;
    return result

def getusers(db):
    conn=ctx.sqlite_run_cmd(db,"SELECT name,uid FROM users;")
    usertable={}
    for i in range(ctx.sqlite_get_data_size(conn)[0]):
        name=ctx.sqlite_get_data(conn,i,0)
        if name!=None:        
            id=ctx.sqlite_get_data(conn,i,1)
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
 
def convertdata(db,table,dataidx):
    colidx=ctx.sqlite_get_headers(table).index("TL_TYPE (QString)")
    conn=ctx.sqlite_run_cmd(db,"SELECT data from messages;")
    rows=ctx.sqlite_get_data_size(conn)[0]
    if rows>0:    
        ctx.gui_setMainProgressBar(0)
        oldpos=0
        usertable=getusers(db)
        userchat=getchat(db)
        for i in range(0,rows):
            newpos=int(i/rows*100);
            if (oldpos<newpos):
                oldpos=newpos
                ctx.gui_setMainProgressBar(oldpos)
            value=ctx.sqlite_get_data(conn,i,0)
            if value!=None:
                value=value.data()
                data = JavaFunc(value)
                telgram = Telegram(data,usertable,userchat)
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
    ctx.gui_setMainProgressBar(100)
    ctx.sqlite_cmd_close(conn)

def converttimecolumn(db,table,dateidx):
	for i in range(0,ctx.sqlite_get_data_size(table)[0]):
		val=ctx.sqlite_get_data(table,i,dateidx)
		if (val!=None and val>0):
			conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
			ctx.sqlite_set_data(table,i,dateidx,ctx.sqlite_get_data(conn,0,0))
			ctx.sqlite_cmd_close(conn)

def searchandreplace(table,idx,search,replace):
	for i in range(0,ctx.sqlite_get_data_size(table)[0]):
		if (search==ctx.sqlite_get_data(table,i,idx)):
			ctx.sqlite_set_data(table,i,idx,replace)

def main():
    error=""
    files=findtelegram()
    ctx.gui_setMainProgressBar(0)
    if (len(files)==0):
        error="Error: Couldn't find Telegram"
        return error
    db=ctx.sqlite_open(files["Data"],False)
    if db==-1:
        error="Error: Couldn't open Database "+files["Data"];
        return error
    ctx.gui_setMainLabel("Telegram: Seeking messages");
    table=ctx.sqlite_run_cmd(db,"SELECT * from messages;")
    if table==-1:
        error="Error on query: SELECT * from messages;"
        ctx.sqlite_close(db)
        return error

    ctx.gui_setMainLabel("Telegram Plugin: Converting Date Field");
    dateidx=ctx.sqlite_get_headers(table).index("date (int)")
    converttimecolumn(db,table,dateidx)

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
    convertdata(db,table,dataidx)

    if (reportdir is ""):
        xlsxfile=ctx.gui_askSaveDir("Please select directory to store the report")
        if (xlsxfile==""):
            error="Can't generate report without directory"
            ctx.gui_setMainLabel("Status: Idle.")
    else:
            if not os.path.exists(reportdir+"/telegram"):
                os.makedirs(reportdir+"/telegram")
            xlsxfile=reportdir+"/telegram"

    ctx.gui_setMainLabel("Status: Writing telegram report to xlsx.")
    xlsxfile=xlsxfile+"/telegram.xlsx"
    if (not ctx.sqlite_save_as_xlsx(table,xlsxfile, "cache4.db")):
        return "Error on writing "+xlsxfile
    ctx.sqlite_cmd_close(table)
    ctx.sqlite_close(db)
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."