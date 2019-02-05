#Pluginname="Thumbnailcreator"
#(c) B.Kerler 2017
#Type=App

from os import walk
import os
import struct
import io
from PythonQt import QtCore
from Library import thumbnail
import tempfile

size = 128*2, 128*2

def main():
    filenames=ctx.pluginfilenames();
    headers=["timestamp (int)","thumbnail (QByteArray)","filename (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainProgressBar(0)
    ctx.gui_setMainLabel("Status: Converting image to thumbnail")

    i=0
    for fsname in filenames:
        ret=thumbnail.generate(ctx,fsname)
        if (ret!=-1):
            ctx.gui_set_data(i,0,ret[0])
            ctx.gui_set_data(i,1,QtCore.QByteArray(bytes(ret[1])))
            ctx.gui_set_data(i,2,ret[2])
            i=i+1
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    
    return "Finished running plugin."
    #return "Error: None"