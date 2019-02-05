import os
import random

def decrypt(ctx,infile,tmpdir):
    keyfile = os.path.join(tmpdir, "confidential.keystore")
    rnd=str(random.randrange(0xFFFFFFF))
    insql = os.path.join(tmpdir, rnd+".sqlite.enc")
    outsql = os.path.join(tmpdir, rnd+"tmp.sqlite")
    if ctx.fs_file_extract("/data/com.tomtom.navkit/files/confidential.keystore",keyfile):
        if ctx.fs_file_extract(infile,insql):
            if ctx.fs_tomtom_decrypt(keyfile,insql,outsql):
                return ctx.sqlite_open(outsql,True)
        else:
            print("Error on extraction of: "+keyfile)
    else:
        print("Error on extraction of: "+keyfile)
    return -1
