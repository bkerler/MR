#Pluginname="Protobuf Decoder"
#Type=Generic

import struct
import os
from Library import protobuf
import binascii

def main():
    ctx.gui_setMainLabel("Protobuf: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    cell=ctx.gui_get_currentcell()
    row=int(cell[0])
    col=int(cell[1])

    try:
        dat=bytearray(ctx.gui_get_data(row,col).data())
    except:
        dat=bytes(ctx.gui_get_data(row,col),'utf-8')
    #dat=binascii.unhexlify("0A180A0A089685E22E10E8ACD30B120A08E8E9BE2E10EAD1930C")
    info=protobuf.pseudoxml(dat)
    print(info)
    #print("Pos:%08X" % str(pos))

    ctx.gui_set_data(row,col,info)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."

#main()