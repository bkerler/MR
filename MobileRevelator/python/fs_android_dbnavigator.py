#Pluginname="DB Navigator (Android,FS)"
#Category="Reports"
#Type=FS

import struct
import os
import tempfile

def finddbnavigator():
	#Lets see where the db navigator files are
	ctx.gui_setMainLabel("Seeking for DBNavigator files")
	result={}
	for datadir in ["/data/de.hafas.android.db/databases/hafas_android.db","/data/de.hafas.android.vbn/databases/hafas_android.db","de.hafas.android.db/db/hafas_android.db"]:
		if (ctx.fs_isFile(datadir)==True):
			result["Data"]=datadir
	return result
	
def converttimecolumn(db,conn):
	rows=ctx.sqlite_get_data_size(conn)[0]
	for i in range(0,rows):
		dat=ctx.sqlite_get_data(conn,i,3)
		if dat!=None:
			val=int(dat)/1000
			if (val>0):
				conn2=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
				ctx.sqlite_set_data(conn,i,3,ctx.sqlite_get_data(conn2,0,0))
				ctx.sqlite_cmd_close(conn2)

def convertdata(db,conn):
	headers=["_id (int)","startLocationName (QString)","targetLocationName (QString)","requestTime (int)"]
	ctx.sqlite_set_headers(conn,headers)
	rows=ctx.sqlite_get_data_size(conn)[0]

	oldpos=0
	for i in range(0,rows):
		newpos=int(i/rows*100)
		if (oldpos<newpos):
			oldpos=newpos
			ctx.gui_setMainProgressBar(oldpos)
		id=ctx.sqlite_get_data(conn,i,0)
		dataitems=ctx.sqlite_get_data(conn,i,1).data()
		datastr=dataitems.splitlines()
		try:
			startLocationName=datastr[0].decode('utf-8')
			targetLocationName=datastr[1].decode('utf-8')
		except:
			startLocationName=datastr[0].decode('latin1')
			targetLocationName=datastr[1].decode('latin1')
		for x in range(len(datastr)):
			if "requestTime" in str(datastr[x]):
				requestTime=str(datastr[x]).split("=")[1][:-1]
				break

		ctx.sqlite_set_data(conn,i,0,id)
		ctx.sqlite_set_data(conn,i,1,startLocationName)
		ctx.sqlite_set_data(conn,i,2,targetLocationName)
		ctx.sqlite_set_data(conn,i,3,requestTime)
		

def main():
	error=""
	files=finddbnavigator()
	if (len(files)==0):
		error="Error: Couldn't find DB Navigator"
		return error
	i=-1
	for subfiles in files["Data"].split(";"):
		i=i+1
		print(subfiles+"\n")
		db=ctx.sqlite_open(subfiles,False)
		if db==-1:
			error="Couldn't open Database "+subfiles
			continue;
		ctx.gui_setMainLabel("DB Navigator: Parsing Strings");
		ctx.gui_setMainProgressBar(0)
		query="SELECT _id, data from favoritenlist_reqp;"
		conn=ctx.sqlite_run_cmd(db,query)
		if conn==-1:
			error="Error on query: "+query
			ctx.sqlite_close(db)
			continue;
		convertdata(db,conn)
		ctx.gui_setMainLabel("DB Navigator: Converting timestamp")
		converttimecolumn(db,conn)
		if (reportdir is ""):
			xlsxfile=ctx.gui_askSaveDir("Please select directory to store the report")
			if (xlsxfile==""):
				error="Can't generate report without directory"
				ctx.gui_setMainLabel("Status: Idle.")
		else:
				if not os.path.exists(reportdir+"/dbnavigator"):
					os.makedirs(reportdir+"/dbnavigator")
				xlsxfile=reportdir+"/dbnavigator"

		xlsxfile=xlsxfile+"/dbnavigator"+str(i)+".xlsx"
		if (not ctx.sqlite_save_as_xlsx(conn,xlsxfile, "hafas_android")):
			return "Error on writing "+xlsxfile
		ctx.sqlite_cmd_close(conn)
		ctx.sqlite_close(db)
	ctx.gui_setMainLabel("Status: Idle.")
	ctx.gui_setMainProgressBar(0)
	return "Finished running plugin."