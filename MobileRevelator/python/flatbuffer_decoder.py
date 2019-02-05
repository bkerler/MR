#Pluginname="Flatbuffer Decoder"
#Type=Generic

import struct
import os
from Library import flatbuffer

def main():
    ctx.gui_setMainLabel("Google Mail: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    cell=ctx.gui_get_currentcell()
    row=int(cell[0])
    col=int(cell[1])
    dat=bytearray(ctx.gui_get_data(row,col).data())
    ft = flatbuffer.flatbuffer(dat)
    dat=ft.flattoxml()
    ctx.gui_set_data(row,col,dat)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."