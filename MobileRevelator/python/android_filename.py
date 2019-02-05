#Pluginname="Filenamecreator"
#(c) B.Kerler 2017
#Type=App

from os import walk
import os
import struct
import tempfile

def main():
    filenames=ctx.pluginfilenames();
    headers=["timestamp (int)","filename (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainProgressBar(0)
    ctx.gui_setMainLabel("Status: Converting filenames")

    i=0
    for fsname in filenames:
        timestamp=ctx.fs_gettime(fsname)[1]
        ctx.gui_set_data(i,0,int(timestamp))
        ctx.gui_set_data(i,1,fsname)
        i=i+1
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    
    return "Finished running plugin."
    #return "Error: None"