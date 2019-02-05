#Pluginname="SkyECC Decoder"
#Type=App

import struct
import os
from Crypto.Cipher import AES
import hashlib
import base64
import binascii
import sqlite3
import datetime

passwd=b'ecfx'
enc_secretkey='PtedZpZ9c3aViSySsHlD3fTzK48n5zWyDiYWjlfhcnJeLZqpngux0IkwIbHibMKG'

def unpad(s):
    try:
        dat=s[:-ord(s[len(s)-1:])]
    except:
        dat=s
    return dat

def hu_KDFDerive(type, passwd):
    if (type==6):
        return hashlib.sha512(passwd + b'\x00\x00\x00\x01').digest()
        
def decrypt_secret_key(enc_secretkey,aes):
    secretKey = aes.decrypt(base64.b64decode(enc_secretkey))
    secretKey = unpad(secretKey)
    kdfDeriveS = hu_KDFDerive(6,secretKey)
    return kdfDeriveS
    
def decrypt_session_key(db,kdfDeriveS,aes):
    masterKey=b''
    conn=ctx.sqlite_run_cmd(db,"select k,v from secconfig;")
    if (conn==-1):
        return masterKey
    rows=ctx.sqlite_get_data_size(conn)[0]
    encnames=['RSA_PRIV','HID','PRIVATE_KEY','MASTER_KEY','ECC_PRIV','ENC_TEST_KEY','DURESS_PWD','SERVER_SES_KEY']
    debase=['SERV_PUB_KEY','PUBLIC_KEY','ECC_PUB','ECDH_SERVPUB','AGENT_PIN']
    for i in range(0,rows):
        name=ctx.sqlite_get_data(conn,i,0)
        if (name in encnames):
                IV = b'0' * 16
                aes = AES.new(kdfDeriveS[0:32], AES.MODE_CFB, IV, segment_size=128)
                data = aes.decrypt(base64.b64decode(ctx.sqlite_get_data(conn,i,1)))
                if (name == 'MASTER_KEY'):
                    masterKey=data
        elif (name in debase):
            data=base64.b64decode(ctx.sqlite_get_data(conn,i,1))
    ctx.sqlite_cmd_close(conn)
    return masterKey

def decrypt_raw(datakey, masterKey):
    IV = b'0' * 16
    aes2 = AES.new(masterKey[0:32], AES.MODE_CFB, IV, segment_size=128)
    msg = unpad(aes2.decrypt(base64.b64decode(datakey)))
    return msg

def decrypt_string(datakey, masterKey):
    IV = b'0' * 16
    aes2 = AES.new(masterKey[0:32], AES.MODE_CFB, IV, segment_size=128)
    msg = unpad(aes2.decrypt(base64.b64decode(datakey)))
    msg = msg.decode()
    return msg

def decrypt_data(masterKey,datakey,mdate,db):
    cursor = db.cursor()
    info=datakey.split(':')
    pkey = info[0]
    seqcount = int(info[1])
    md5 = info[2]
    key = hashlib.sha256(bytes(pkey, 'utf8')).digest()

    data=b''
    for seq in range(0,seqcount):
        cursor.execute('select data from note_data where mdate='+str(mdate)+' and seq='+str(seq)+';')
        for row in cursor:
            IV = b'aBfc9ab525fe273e'
            aes3 = AES.new(key, AES.MODE_CBC, IV)
            dec=aes3.decrypt(base64.b64decode(row['data']))
            data+=dec
    return data

def getdate(date):
    ts=datetime.datetime.utcfromtimestamp(int(date)/1000)
    return ts.strftime('%d.%m.%Y %H:%M:%S')

def getdatename(date):
    ts=datetime.datetime.utcfromtimestamp(int(date)/1000)
    return ts.strftime('%d%m%Y-%H%M%S')
    
def main():
    ctx.gui_setMainLabel("SkyECC: Getting MasterKey");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    kdfDerive = hu_KDFDerive(6,passwd)

    IV = b'0' * 16
    pwaes = AES.new(kdfDerive[0:32],AES.MODE_CFB, IV, segment_size=128)
    secretkey=decrypt_secret_key(enc_secretkey,pwaes)
    saes  = AES.new(secretkey[0:32],AES.MODE_CFB, IV, segment_size=128)
    masterKey = decrypt_session_key(db,secretkey,pwaes)
    
    cell=ctx.gui_get_currentcell()
    rows=ctx.gui_data_size()[0]
    #row=int(cell[0])
    col=int(cell[1])
    for row in range(0,rows):
        dat=bytearray(ctx.gui_get_data(row,col),'utf8')
        try:
            dec=decrypt_string(dat,masterKey)
        except:
            dec=decrypt_raw(dat,masterKey)
        ctx.gui_set_data(row,col,dec)

    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."