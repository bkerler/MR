#Pluginname="Whatsapp (Android,FS)"
#Category="Reports"
#Type=FS

import struct
import os
import tempfile
import subprocess
import sys
import shutil
 
def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

# Run command with logging to trace window
def run(cmd):
    if sys.platform == 'win32':
      startupinfo = subprocess.STARTUPINFO()
      startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    else:
      startupinfo = None
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
    #logtext.insert(END, "Cmd>")
    #for s in cmd:
    #    logtext.insert(END, " " + s)
    #logtext.insert(END, "\r\n")
    stdout = ''
    while True:
        line = str(p.stdout.readline(), encoding='UTF-8')
        stdout += line
        #logtext.insert(END, line)
        #logtext.yview(END)
        curstat = p.poll()
        if ((line == '') and (curstat != None)):
            break
    return stdout

def GetPythonPath(program):
	def is_exe(fpath):
		return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
	
	fpath,fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			path=path.strip('"')
			exe_file = os.path.join(path,program)
			if is_exe(exe_file):
				return exe_file
	
	return None

def findwhatsapp():
	#Lets see where the whatsapp files are
	ctx.gui_setMainLabel("Seeking for Whatsapp files")
	result={}
	
	for datadir in ["/data/com.whatsapp","com.whatsapp"]:
		if (ctx.fs_isDir(datadir)==True):
			result["Data"]=datadir;
	
	for mediadir in ["/media/WhatsApp","/media/0/WhatsApp","/media/1/WhatsApp","/media/2/WhatsApp","/media/3/WhatsApp","/media/4/WhatsApp","/media/150/WhatsApp"]:
		if (ctx.fs_isDir(mediadir)==True):
			result["Media"]=mediadir;
	
	return result
	
def main():
    error=""
    script=ctx.gui_getpythonscriptpath()+"/whatsapp.py"
    ctx.gui_setMainLabel("Getting Python Path")
    python=GetPythonPath("python.exe") #Windows
    if (python is None):
        python=GetPythonPath("python") #Linux/Mac
        if (python is None):
            python=ctx.gui_getpythonpath()+"/python.exe"
            #return "You need to install Python first"

    files=findwhatsapp()
    extracttodir=""
    if ("Data" not in files):
        error="Couldn't find WhatsApp"
    elif ("Media" not in files):
        error="Couldn't find Media Directory"
    if ("reportdir" not in locals()):
        extracttodir=ctx.gui_askSaveDir("Please select directory to store the report")
        if (extracttodir==""):
            error="Error: Can't generate report without directory"
            ctx.gui_setMainLabel("Status: Idle.")
            return error
    else:
        if not os.path.exists(reportdir+"/WhatsApp"):
            os.makedirs(reportdir+"/WhatsApp")
        extracttodir=reportdir+"/WhatsApp"
    print("Status: copying data files to: "+extracttodir+"/data")
    if not os.path.exists(extracttodir+"/data"):
            ctx.gui_setMainLabel("Status: copying data files to: "+extracttodir+"/data")
            copyDirectory(ctx.gui_getpythonscriptpath()+"/WhatsApp/data",extracttodir+"/data")
    ctx.gui_setMainLabel("Status: Extracting files to: "+extracttodir)
    ctx.fs_dir_extract(files["Data"],extracttodir)
    if ("Media" in files):
        ctx.fs_dir_extract(files["Media"],extracttodir)
    ctx.gui_setMainLabel("Status: Running WhatsApp report")
    print("Status: Extraction done. Running plugin.")
    print(python+" "+script+" "+extracttodir+"/com.whatsapp/databases/msgstore.db"+" -o "+extracttodir+"/report")
    run([python,script,extracttodir+"/com.whatsapp/databases/msgstore.db","-o",extracttodir+"/report"])
    ctx.gui_setMainLabel("Status: Idle.")
    return "Finished Running WhatsApp Report."
