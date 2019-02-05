#Pluginname="MD5 Run Whitelist"
#Category="Whitelist"
#Type=FS

import struct
import os
import tempfile
import hashlib

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def readwhitelistdatabase(whitelistdb):
	#Read whitelisted md5 into database
	hashdb={}
	if (os.path.isfile(whitelistdb)):
		with open(whitelistdb, "r") as rdb:
			for line in iter(rdb):
				item=line.split(";")
				hash=item[1][:-1]
				filename=item[0]
				hashdb[hash]=filename
	return hashdb

def whitelist(whitelistdb,hashdb):
	#Create hash if files are selected
	tmpfile=tempfile.gettempdir()+"/md5tmp"
	allfiles=ctx.fs_getselected()
	if len(allfiles)==0:
		allfiles=ctx.fs_filelist()
	filecount=len(allfiles)
	if (filecount==0):
		return "No files found for whitelisting. Aborting."
		
	if (filecount>0):
		i=0
		for file in allfiles:
			if (ctx.fs_isDir(file)):
				continue
			elif(ctx.fs_isFile(file)):
				ctx.gui_setMainProgressBar(abs(i/filecount*100))
				ctx.gui_setMainLabel("Whitelisting "+file)
				ctx.fs_file_extract(file,tmpfile)
				hash=md5(tmpfile)
				os.remove(tmpfile)
				i=i+1
				if (hash in hashdb):
					ctx.fs_hide(file)
	return ""

def main():
	ctx.gui_setMainProgressBar(0);
	ctx.gui_setMainLabel("Starting MD5 whilelisting")
	whitelistpath=ctx.gui_getpythonscriptpath()+"/whitelist"
	whitelistdb=whitelistpath+"/whitelist.txt"
	
	ctx.gui_setMainLabel("Creating whitelist directory")
	if not os.path.exists(whitelistpath):
		os.makedirs(whitelistpath)
	
	ctx.gui_setMainLabel("Reading database")
	hashdb=readwhitelistdatabase(whitelistdb)

	ctx.gui_setMainLabel("Running whitelist")
	str=whitelist(whitelistdb,hashdb)
	
	ctx.gui_setMainLabel("Status: Idle.")
	ctx.gui_setMainProgressBar(0);
	if (str==""):
		return "Finished Running Whitelist."
	return str;