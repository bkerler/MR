#Pluginname="Signal/TextSecure (Android)"
#Filename="messages.db"
# - added Signal/Textsecure (01.01.2017) B. Kerler
#Type=App

import hashlib
import binascii
import tempfile
import xml.etree.ElementTree as ET
from pkcs12 import PKCS12
import base64

def converttimecolumn(db,dateidx):
    for i in range(0,ctx.gui_data_size()[0]):
        if (ctx.gui_get_data(i,dateidx))!=None:
            val=int(ctx.gui_get_data(i,dateidx))/1000
        if (val>0):
            conn=ctx.sqlite_run_cmd(db,"SELECT datetime("+str(val)+",'unixepoch','localtime');")
            ctx.gui_set_data(i,dateidx,ctx.sqlite_get_data(conn,0,0))
            ctx.sqlite_cmd_close(conn)

def findsignalprefs():
    #Lets see where the db navigator files are
    ctx.gui_setMainLabel("Seeking for Signal preferences")
    result={}
    for datadir in ["/data/org.thoughtcrime.securesms/shared_prefs/SecureSMS-Preferences.xml","/org.thoughtcrime.securesms/shared_prefs/SecureSMS-Preferences.xml"]:
        if (ctx.fs_isFile(datadir)==True):
            result["Data"]=datadir;
    return result

def convertdata(masteraes,pkcs12,db):
    conn=ctx.sqlite_run_cmd(db,"select _id, thread_id, address, date, date_sent, read, reply_path_present, delivery_receipt_count, subject, body, expires_in, expire_started from sms;")
    if conn==-1:
        print(ctx.sqlite_last_error(db))
    newversion=True
    if conn==-1:
        conn=ctx.sqlite_run_cmd(db,"select _id, thread_id, address, date, date_sent, read, reply_path_present, delivery_receipt_count, subject, body from sms;")
        newversion=False
    rows=ctx.sqlite_get_data_size(conn)[0]
 
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        thread_id=ctx.sqlite_get_data(conn,i,1)
        address=ctx.sqlite_get_data(conn,i,2)
        date=ctx.sqlite_get_data(conn,i,3)
        date_sent=ctx.sqlite_get_data(conn,i,4)
        read=ctx.sqlite_get_data(conn,i,5)
        reply_path_present=ctx.sqlite_get_data(conn,i,6)
        delivery_receipt_count=ctx.sqlite_get_data(conn,i,7)
        subject=base64.b64decode(ctx.sqlite_get_data(conn,i,8))[:-0x14]
        body=base64.b64decode(ctx.sqlite_get_data(conn,i,9))[:-0x14]
        expires_in=ctx.sqlite_get_data(conn,i,10)
        expire_started=ctx.sqlite_get_data(conn,i,11)
        #print(masteraes.decrypt(body))
        if (len(body)>0):
            tt=masteraes.decrypt(body)
            body=pkcs12.REMOVE_PKCS7_PADDING(tt)[0x10:].decode()
        else:
            body=""
        if (len(subject)>0):
            tt=masteraes.decrypt(subject)
            subject=pkcs12.REMOVE_PKCS7_PADDING(tt)[0x10:].decode()
        else:
            subject=""
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,thread_id)
        ctx.gui_set_data(i,2,address)
        ctx.gui_set_data(i,3,date)
        ctx.gui_set_data(i,4,date_sent)
        ctx.gui_set_data(i,5,read)
        ctx.gui_set_data(i,6,reply_path_present)
        ctx.gui_set_data(i,7,delivery_receipt_count)
        ctx.gui_set_data(i,8,subject)
        ctx.gui_set_data(i,9,body)
        if (newversion==True):
            ctx.gui_set_data(i,10,expires_in)
            ctx.gui_set_data(i,11,expire_started)
        else:
            ctx.gui_set_data(i,10,"0")
            ctx.gui_set_data(i,11,"0")
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["_id (int)","thread_id (int)","address (QString)","date (int)","date_sent (int)","read (int)","reply_path_present (int)","delivery_receipt_count (int)","subject (QString)","body (QString)","expires_in (int)","expire_started (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    files=findsignalprefs()
    
    if (len(files)==0):
        error="Error: Couldn't find Signal preferences"
        return error
    tmpfile=tempfile.gettempdir()+"/SecureSMS-Preferences.xml"
    ctx.fs_file_extract(files["Data"],tmpfile)
    ctx.gui_add_report_relevant_file(files["Data"])
    tree = ET.parse(tmpfile)
    root = tree.getroot()
    passwd=b'\x00u\x00n\x00e\x00n\x00c\x00r\x00y\x00p\x00t\x00e\x00d\x00\x00'
    iterations=0
    salt=b""
    encsecret=b""
    for child in root:
        name=child.attrib['name']
        if (name=='encryption_salt'):
            salt=base64.b64decode(child.text)
        if (name == 'master_secret'):
            encsecret=base64.b64decode(child.text)[:-0x14]
        if (name == 'passphrase_iterations'):
            iterations=int(child.attrib['value'])

    pkcs = PKCS12()
    hash=pkcs.PBKDF_PKCS12v1(iterations,passwd,salt,16)
    key=bytes(hash[0])
    iv=bytes(hash[1])
    from Crypto.Cipher import AES
    aes=AES.new(key,AES.MODE_CBC,iv)
    masterkey=aes.decrypt(encsecret[:16])
    print("Masterkey: "+binascii.hexlify(masterkey).decode())
    print("IV: "+binascii.hexlify(iv).decode())
    masteraes = AES.new(masterkey, AES.MODE_CBC, iv)
    ctx.gui_setMainProgressBar(0)
    ctx.gui_setMainLabel("Signal : Decrypting data...")
    convertdata(masteraes,pkcs,db)
    ctx.gui_setMainLabel("Signal : Converting timestamps...")
    converttimecolumn(db,3)
    converttimecolumn(db,4)
    converttimecolumn(db,10)
    converttimecolumn(db,11)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."