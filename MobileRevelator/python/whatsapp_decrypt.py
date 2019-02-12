#Filename="msgstore*db.crypt"
#Type=Prerun

import os
import hashlib
import struct
import array
import binascii
import tempfile
import shutil
from Crypto.Cipher import AES
try:
    AES.MODE_GCM
except:
    from Cryptodome.Cipher import AES
    try:
        AES.MODE_GCM
    except:
        print('Please install Crypto or Cryptodome with MODE_GCM support.')
import gzip
import zlib

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def GetBase(input):
    try:
        if (input.rindex('/')>0):
            return input[input.rindex('/') + 1:]
    except:
        return input[input.rindex('\\') + 1:]

def GetPath(input):
    try:
        if (input.rindex('/')>0):
            return input[0:input.rindex('/')]
    except:
            return input[0:input.rindex('\\')]


def PKCS5PaddingLength(data):
  length = data[len(data)-1]
  if ((length > 0) and (length < 16)):
    for i in range (0,length):
      if length != data[len(data)-i-1]:
        return 0
  else:
    return 0
  return length

def decryptwhatsapp(infile,outfile,keypath):
    try:
        print("Trying to decrypt Whatsapp Crypt database :"+infile)
        filename, file_extension = os.path.splitext(infile)
        decryptedfile = outfile
        if "_" in file_extension:
            file_extension=file_extension[:file_extension.rfind("_")]
        #print (file_extension)
        version=int(file_extension[6:])
        decrypted=b''
        if (version==0):
            key = "346a23652a46392b4d73257c67317e352e3372482177652c"
            key = bytes.fromhex(key)
            cipher = AES.new(key,AES.MODE_ECB)
            decrypted = cipher.decrypt(open(infile,"rb").read())
        elif (version>=6) and (version<9):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_CBC, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        compressed=compressed[0:len(compressed)-padlen]
                        try:
                            decrypted=gzip.decompress(compressed)
                        except:
                            return ""
            else:
                print("Error: Couldn't find key in path: "+keypath)
                return
        elif (version>=9) and (version<12):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_GCM, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        compressed=compressed[0:len(compressed)-padlen]
                        try:
                            decrypted=gzip.decompress(compressed)
                        except:
                            return ""
            else:
                print("Error: Couldn't find key in path: "+keypath)
                return
        elif (version==12):
            if os.path.isfile(keypath):
                with (open(keypath,'rb')) as keyf:
                    keycontent = keyf.read()
                    key = keycontent[126:126+32]
                    with (open(infile,"rb")) as inputf:
                        inputf.seek(51)
                        iv=inputf.read(16)
                        cipher = AES.new(key, AES.MODE_GCM, iv)
                        compressed = cipher.decrypt(open(infile,"rb").read()[51+16:])
                        padlen=PKCS5PaddingLength(compressed)
                        decrypted=compressed[0:len(compressed)-padlen]
                        try:
                            decrypted=zlib.decompress(compressed,32)
                        except:
                            return ""
            else:
                print("Error: Couldn't find key in path: "+keypath)
                return ""
        else:
                print("Unknown crypt version")
                return ""
        with open(decryptedfile, "wb") as output:
            output.write(decrypted)
            return decryptedfile
    except:
        print("Error on decryption")
        raise
    return ""
        
def main():
    ctx.gui_setMainLabel("WhatsApp: Extracting key");
    tmpdir = tempfile.mkdtemp()
    outkey = os.path.join(tmpdir, "key")
    error=""
    keyfiles=[]
    for kf in ["/data/com.whatsapp/files/key","/data/user/150/com.whatsapp/files/key"]:
        keyfiles.append(kf)
    
    for keyfile in keyfiles:
        print(keyfile)
        if ctx.fs_file_extract(keyfile, outkey):
            ctx.gui_add_report_relevant_file("/data/com.whatsapp/files/key")
            ret=decryptwhatsapp(filename,filename+".dec",outkey)
            if (ret!=""):
                shutil.rmtree(tmpdir)
                return "WhatsApp: Decryption of whatsapp database successful."
    shutil.rmtree(tmpdir)
    return "Error: Couldn't decrypt whatsapp database."