#Filename="EnMicroMsg.db"
#Type=Prerun

import struct
import os
import tempfile
from Library import javaobj
import xml.etree.ElementTree
from hashlib import md5

def main():
    ctx.gui_setMainLabel("WeChat: Extracting uin");
    tmpdir = tempfile.mkdtemp()
    outuin = os.path.join(tmpdir, "uin")
    uin=""
    if ctx.fs_file_extract("/data/com.tencent.mm/shared_prefs/auth_info_key_prefs.xml",outuin):
      ctx.gui_add_report_relevant_file("/data/com.tencent.mm/shared_prefs/auth_info_key_prefs.xml")
      e = xml.etree.ElementTree.parse(outuin).getroot()
      for atype in e.findall("int"):
        if atype.get("name")=="_auth_uin":
           uin=atype.get("value")
           print("UIN: "+uin+"\n")
      os.remove(outuin)
    
    ctx.gui_setMainLabel("WeChat: Extracting imei");
    imei=""
    outimei = os.path.join(tmpdir, "imei")
    if ctx.fs_file_extract("/data/com.tencent.mm/MicroMsg/CompatibleInfo.cfg",outimei):
      ctx.gui_add_report_relevant_file("/data/com.tencent.mm/MicroMsg/CompatibleInfo.cfg")
      with open(outimei,"rb") as f:
        imei=javaobj.loads(f.read())[0].annotations[2]
        print("IMEI: "+imei+"\n")
      os.remove(outimei)
    if (imei=="" or uin==""): 
      return "Error: Couldn't extract imei and uin."

    a = md5(imei.encode("utf-8") + uin.encode("utf-8"))
    dbkey=a.hexdigest()[:7]
    print(dbkey)
    ctx.gui_setMainLabel("WeChat: Key extracted: "+dbkey)

    outimei = os.path.join(tmpdir, "imei")
    ctx.fs_sqlcipher_decrypt(filename,filename+".dec",dbkey)
    
    return "Finished decryption."