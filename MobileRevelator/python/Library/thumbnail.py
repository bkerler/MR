from os import walk
import os
import struct
import io
from PIL import Image
import tempfile

size = 128*2, 128*2

def generate(ctx,fsname):
    timestamp=ctx.fs_gettime(fsname)[1]
    filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:]
    if ctx.fs_file_extract(fsname,filename):
        with open(filename,"rb") as rb:
            jpg=bytearray(rb.read())
            dat=[]
            try:
                with io.BytesIO() as output:
                    im = Image.open(io.BytesIO(jpg))
                    im.thumbnail(size)
                    im.save(output, format=im.format)
                    jpg=output.getvalue()
                    dat=[int(timestamp),jpg,fsname]
            except:
                jpg=""
        os.remove(filename)
        if len(dat)>0:
            return dat
    return -1
