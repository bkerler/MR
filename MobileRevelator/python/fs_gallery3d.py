#Pluginname="Gallery3D (Android,FS)"
#Category="Extraction"
#Type=FS

import struct
import os
import tempfile
from Library.java import JavaFunc
from binascii import hexlify, unhexlify
globalval=0

def extractimgcachemicro(micro,outdir):
    global globalval
    with open(micro,"rb") as rb:
        pos=4
        rb.seek(pos)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        while (1):
            if (rb.tell()==os.stat(micro).st_size):
                break
            header=rb.read(16)
            info=struct.unpack("16s",header)
            pos+=16
            hash=info[0]
            imglen = struct.unpack("<I", rb.read(4))[0]
            pos += 4
            filename=""
            subpos=0
            while (subpos<imglen):
                wchar=rb.read(2)
                if (wchar[1]!=0) and (wchar[1]!=6):
                    break;
                filename+=wchar.decode("UTF-16")
                subpos+=2
            dataoffset=pos+subpos
            rb.seek(dataoffset)
            
            hpos=rb.tell()
            dd=rb.read(2)
            rb.seek(hpos)
            ext=""
            flag=0
            if dd==b"\xFF\xD8" or dd==b"\xFF\xE0":
                    ext=".jpg"
                    timestamp=os.stat(micro).st_mtime
                    flag=0
            else:
                    timestamp = struct.unpack("<Q", rb.read(8))[0]
                    timestamp=timestamp/1000  
                    flag=8
                    hpos=rb.tell()
                    dd=rb.read(2)
                    rb.seek(hpos)
                    if dd==b"\xFF\xD8" or dd==b"\xFF\xE0":
                        ext=".jpg"
                    
            imgname=filename[filename.rfind("/")+1:]
            newfilename=outdir+"/"+imgname[:imgname.rfind("+")]
            if len(imgname)<2:
                newfilename=outdir+"/tmp"+str(globalval)
                globalval+=1
            if imgname.rfind(".")==-1:
                if ext==".jpg":
                    newfilename+=ext
            with open(newfilename,"wb") as wf:
                data=rb.read(imglen-subpos-3-flag)
                wf.write(data)
            os.utime(newfilename,(timestamp,timestamp))
            pos+=imglen
            rb.seek(pos)
            if (pos==os.stat(micro).st_size):
                break


def findfiles():
    files=[]
    ctx.gui_setMainLabel("Seeking for Gallery3D cache")
    allfiles=ctx.fs_getselected()
    if len(allfiles)==0:
        allfiles=ctx.fs_filelist()
    filecount=len(allfiles)
    for file in allfiles:
        if ("imgcacheMicro.0" in file or "imgcache.0" in file):
            files.append(file)
    return files

def main():
    error=""
    ctx.gui_setMainProgressBar(0)
    micros=findfiles()
    if (len(micros)==0):
        error="Couldn't find Gallery3D cache"
        return error

    extracttodir=ctx.gui_askSaveDir("Please select directory to extract the files to")
    if (extracttodir==""):
        error="Can't extract files without directory"
        ctx.setMainLabel("Status: Idle.")
        return error

    for t in micros:
        ctx.fs_file_extract(t,extracttodir+"/tmp")
        ctx.gui_setMainLabel("Status: Extracting "+t)
        extractimgcachemicro(extracttodir+"/tmp",extracttodir)
        os.remove(extracttodir+"/tmp")
            
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."