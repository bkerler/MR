#Pluginname="Gallery3D (Android)"
#Filename="imgcache*.0"
# - added by B.Kerler (12.09.2017)
#Type=App

import os
import tempfile
from Library.java import JavaFunc
from binascii import hexlify, unhexlify
from os import walk
import struct
import io
from PIL import Image
from PythonQt import QtCore

globalval=0
size = 128*2, 128*2

def extractimgcachemicro(micro):
    global globalval
    results=[]
    with open(micro,"rb") as rb:
        pos=4
        rb.seek(pos)
        while (1):
            if (rb.tell()==os.stat(micro).st_size):
                break
            result=[]
            header=rb.read(16)
            if len(header)!=16:
                break
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
                    result.append(timestamp)
                    flag=0
            else:
                    timestamp = struct.unpack("<Q", rb.read(8))[0]
                    timestamp=timestamp/1000  
                    result.append(timestamp)
                    flag=8
                    hpos=rb.tell()
                    dd=rb.read(2)
                    rb.seek(hpos)
                    if dd==b"\xFF\xD8" or dd==b"\xFF\xE0":
                        ext=".jpg"
                    
            imgname=filename[filename.rfind("/")+1:]
            newfilename=imgname[:imgname.rfind("+")]
            if len(imgname)<2:
                newfilename=str(globalval)
                globalval+=1
            if imgname.rfind(".")==-1:
                if ext==".jpg":
                    newfilename+=ext
            data=bytearray(rb.read(imglen-subpos-3-flag))
            result.append(data)
            result.append(newfilename)
            pos+=imglen
            rb.seek(pos)
            results.append(result)
            if (pos==os.stat(micro).st_size):
                break
    return results

def main():
    error=""
    filenames=ctx.pluginfilenames();
    headers=["timestamp (int)","thumbnail (QByteArray)","fsfilename (QString)","realfilename (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainProgressBar(0)
    ctx.gui_setMainLabel("Status: Converting gallery3d image to thumbnail")

    i=0
    for fsname in filenames:
        timestamp=ctx.fs_gettime(fsname)[1]
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
        if ctx.fs_file_extract(fsname,filename):
            results=extractimgcachemicro(filename)
            for x in results:
                jpg=x[1]
                timestamp=x[0]
                orgfilename=x[2]
                ctx.gui_set_data(i,0,int(timestamp))
                ctx.gui_set_data(i,1,QtCore.QByteArray(bytes(jpg)))
                ctx.gui_set_data(i,2,fsname)
                ctx.gui_set_data(i,3,orgfilename)
                i=i+1
            os.remove(filename)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    
    return "Finished running plugin."
    #return "Error: None"