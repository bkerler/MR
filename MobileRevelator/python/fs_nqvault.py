#Pluginname="NQ Vault (Android,FS)"
#Category="Extraction"
#Type=FS

import struct
import os
import tempfile
from Library.java import JavaFunc
from binascii import hexlify, unhexlify

def findnqvault():
	#Lets see where the nq vault files are
	ctx.gui_setMainLabel("Seeking for NQ Vault database")
	result={}
	
	for datadir in ["/data/com.netqin.ps/databases/contactsDB","com.netqin.ps/db/contactsDB"]:
		if (ctx.fs_isFile(datadir)==True):
			result["Data"]=datadir;
	
	return result

def findfiles():
	files={}
	allfiles=ctx.fs_getselected()
	m=0
	if len(allfiles)==0:
		allfiles=ctx.fs_filelist()
	filecount=len(allfiles)
	for file in allfiles:
		if (".image/" in file or ".audio/" in file or ".video/" in file):
			if	".bin" in file:
				item=file[file.rfind("/")+1:file.rfind(".bin")]
				files[item]=file
		if ("322w465ay423xy11" in file):
			st=file[file.rfind("/")+1:]
			if len("322w465ay423xy11")==len(st):
				files[st+str(m)]=file
				m+=1
	return files


def hashcode(passcode):
	h = 0
	for i in range(0, len(passcode)):
		h = 31 * h + ord(passcode[i:i + 1])
		h = h & 0xffffffff
	return h;

def bruteforcepin(password):
	#Lets bruteforce the pin
	i=0
	pwd=str(password)
	for i in range(0,99999999):
		curcode=hashcode(str(i))
		if ((i%10000)==0):
			ctx.gui_setMainLabel("NQVault: Trying pin "+str(i))
		if str(curcode)==pwd:
			return str(i)
	return ""

def getpin(db):
	conn=ctx.sqlite_run_cmd(db,"SELECT password FROM private_password;")
	usertable={}
	pins={}
	for i in range(ctx.sqlite_get_data_size(conn)[0]):
		encodedpassword=ctx.sqlite_get_data(conn,i,0)
		pin=bruteforcepin(encodedpassword)
		if (pin!=""):
			pins[i]=pin
	ctx.sqlite_cmd_close(conn)
	return pins

def verifypin(db,pin):
	conn=ctx.sqlite_run_cmd(db,"SELECT password FROM private_password;")
	usertable={}
	pins={}
	for i in range(ctx.sqlite_get_data_size(conn)[0]):
		encodedpassword=ctx.sqlite_get_data(conn,i,0)
		if (str(encodedpassword)==str(hashcode(pin))):
			pins[0]=pin
	ctx.sqlite_cmd_close(conn)
	return pins

def decryptfile(key,infilename):
	with open(infilename,'r+b') as f:
		dec=f.read(0x80)
		f.seek(0)
		for i in range(0,0x80):
			chr=bytes([dec[i]^key])
			f.write(chr)

def getfilenamesfromdb(databasename):
	filenames={}
	db=ctx.sqlite_open(databasename,False)
	if db==-1:
		return filenames
	conn=ctx.sqlite_run_cmd(db,"SELECT file_name_from, file_path_new FROM hideimagevideo;")
	if (conn is not None):
		for i in range(ctx.sqlite_get_data_size(conn)[0]):
			tname=ctx.sqlite_get_data(conn,i,1)
			if (tname is not None):
				tname=tname[tname.rfind("/")+1:tname.rfind(".")]
				filenames[tname]=ctx.sqlite_get_data(conn,i,0)
		ctx.sqlite_cmd_close(conn)
	ctx.sqlite_close(db)
	return filenames

def main():
	nametable={}
	encfiles=findfiles()
	for t in encfiles:
		if "322w465ay423xy11" in t:
			nt=getfilenamesfromdb(encfiles[t])
			for h in nt:
				nametable[h]=nt[h]
	error=""
	files=findnqvault()
	ctx.gui_setMainProgressBar(0)
	if (len(files)==0 and len(encfiles)==0):
		error="Couldn't find NQ Vault"
		return error
	db=-1
	pins={}
	keys=[]
	if (len(files)!=0):
		db=ctx.sqlite_open(files["Data"],False)
	if db!=-1:
		checkpin=ctx.gui_askText("Please enter pin:")
		if (checkpin!=""):
			pins=verifypin(db,checkpin)
			if (len(pins)==0):
				ctx.gui_setMainMessage(1,"NQVault: PIN "+checkpin+" is wrong, trying to bruteforce.","Info");
			else:
				keys.append(hashcode(checkpin)&0xFF)
		if (len(pins)==0):
			if(ctx.gui_askYesNo("Shall we bruteforce the pin ?")):
				ctx.gui_setMainLabel("NQVault: Please wait, recovering pins..");
				pins=getpin(db)
				pincodes=""
				for x in range(0,len(pins)):
					pincodes+=pins[x]+";"
					keys.append(hashcode(pins[x])&0xFF)
				ctx.gui_setMainMessage(0,"NQVault: PINs recovered="+pincodes,"Info");
			else:
				conn=ctx.sqlite_run_cmd(db,"SELECT password FROM private_password;")
				for i in range(ctx.sqlite_get_data_size(conn)[0]):
					encodedpassword=ctx.sqlite_get_data(conn,i,0)
					keys.append(int(encodedpassword)&0xFF)
					break
		if len(keys)==0:
			error="NQVault: Couldn't recover pins"
			ctx.sqlite_close(db)
			return error

	extracttodir=ctx.gui_askSaveDir("Please select directory to decrypt the files to")
	if (extracttodir==""):
		error="Can't generate report without directory"
		ctx.setMainLabel("Status: Idle.")
		return error

	ctx.gui_setMainLabel("Status: Extracting files to: "+extracttodir)
	for f in encfiles:
		if (len(keys)==0) and (".image" in encfiles[f]):
			outfile=encfiles[f]
			outfile=outfile[outfile.rfind("/")+1:]
			ctx.fs_file_extract(encfiles[f],extracttodir+"/"+outfile)
			with open(extracttodir+"/"+outfile,'rb') as t:
				chr=ord(t.read(1))
				keys.append((chr^0xFF))

	if nametable!=None:
		for f in encfiles:
			if f in nametable: 
				infile=encfiles[f]
				outfile=nametable[f]
				ctx.fs_file_extract(infile,extracttodir+"/"+outfile)
				decryptfile(keys[0],extracttodir+"/"+outfile)
			elif "322w465ay423xy11" not in f:
				infile=encfiles[f]
				outfile=encfiles[f]
				outfile=outfile[outfile.rfind("/")+1:]
				ctx.fs_file_extract(infile,extracttodir+"/"+outfile)
				decryptfile(keys[0],extracttodir+"/"+outfile)

	ctx.gui_setMainLabel("Status: Idle.")
	ctx.gui_setMainProgressBar(0)
	return "Finished running plugin."