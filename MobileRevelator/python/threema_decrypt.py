#Filename="threema.db"
#Type=Prerun

import os
import hashlib
import struct
import array
import binascii
import tempfile
import shutil

def main():
    ctx.gui_setMainLabel("Threema: Extracting key");
    tmpdir = tempfile.mkdtemp()
    outkey = os.path.join(tmpdir, "key.dat")
    error=""
    if not ctx.fs_file_extract("/data/ch.threema.app/files/key.dat", outkey):
        shutil.rmtree(tmpdir)
        return "Error: Couldn't find key.dat for decryption."
    
    ctx.gui_add_report_relevant_file("/data/ch.threema.app/files/key.dat")
    with open(outkey,"rb") as rb:
            ciphertable = array.array("b",[-107, 13, 38, 122, -120, -22, 119, 16, -100, 80, -25, 63, 71, -32, 105, 114, -38, -60, 57, 124, -103, -22, 126, 103, -81, -3, -35, 50, -38, 53, -9, 12])
            ciphertable = bytearray(ciphertable)

            keydata=rb.read()
            stkey=struct.unpack('B 32s 8s 4s', keydata)
            flag=stkey[0]
            key=bytearray(stkey[1])
            salt=stkey[2]
            hash=stkey[3]
            z = len(key)
            for i in range(0,32):
                key[i]=key[i]^ciphertable[i]

            deckey=hashlib.sha1(key).digest()
            if deckey[0:4]==hash:
                print("Threema key correctly decrypted:")
                dbkey="x\""+binascii.hexlify(key).decode()+"\""
                print(dbkey)
                ctx.gui_setMainLabel("Threema: Key extracted: " + dbkey)
                if not (ctx.fs_sqlcipher_decrypt(filename, filename + ".dec", dbkey)):
                    error="Error: Wrong key for decryption."
            else:
                print("Database is locked by password")
                checkpin=ctx.gui_askText("Please enter password:")
                if (checkpin!=""):
                    dk = hashlib.pbkdf2_hmac('sha1', bytearray(checkpin), salt, 10000, 0x100)
                    for i in range(0,32):
                        key[i]=key[i]^dk[i]

                    deckey=hashlib.sha1(key).digest()
                    if deckey[0:4]==hash:
                        print("Threema key correctly decrypted:")
                        dbkey="x\""+binascii.hexlify(key).decode()+"\""
                        print(dbkey)
                        ctx.gui_setMainLabel("Threema: Key extracted: " + dbkey)
                        if not (ctx.fs_sqlcipher_decrypt(filename, filename + ".dec", dbkey)):
                            error="Error: Wrong key for decryption."
                else:
                    error="Error: Wrong key for decryption."
                
    os.remove(outkey)
    if (error==""):
        return "Threema: Decryption of database successful."
    else:
        return error
