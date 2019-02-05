import os
from enum import Enum
from binascii import hexlify, unhexlify
import struct

class protodata:
    tag=0
    value=b""

class wiretype(Enum):
    varint=0
    fixed64=1
    length_delimited=2
    start_group=3
    end_group=4
    fixed32=5

class protobuf:

    def __init__(self, buffer):
        self.buf=buffer
        self.pos=0
        self.tag=0
        self.type=0
        self.error=0
        
    def readRawVarint64SlowPath(self):
        result=0
        shift=0
        while (shift<64):
            b = int.from_bytes(self.buf[self.pos:self.pos+1],byteorder='little')
            self.pos+=1
            result |= (b & 0x7F) << shift
            if (b & 0x80)==0:
                return result
            shift+=7
        return result

    def rshift(self,val, n):
        s = val & 0x80000000
        for i in range(0,n):
            val >>= 1
            val |= s
        return val

    def getTagWireType(self):
        return self.data & (1 << 3) -1

    def getTagFieldNumber(self):
        return self.rshift(self.data,3)

    def readTag(self):
        self.data=self.readRawVarint64SlowPath()
        tag=self.getTagFieldNumber()
        if (tag==0):
            return -1
        type=self.getTagWireType()
        self.tag=tag
        self.type=type
        return tag

    def readValue(self):
        if self.type==wiretype.varint.value:
            self.value = self.readRawVarint64SlowPath()
        elif self.type==wiretype.fixed64.value:
            self.value = struct.unpack('<Q', self.buf[self.pos:self.pos+8])[0]
            self.pos+=8
        elif self.type == wiretype.length_delimited.value:
            len = int(self.readRawVarint64SlowPath())
            self.value = self.buf[self.pos:self.pos+len]
            self.pos+=len
        elif self.type == wiretype.fixed32.value:
            self.value = struct.unpack('<I', self.buf[self.pos:self.pos+4])[0]
            self.pos+=4
        elif self.type == wiretype.start_group.value:
            self.value=b"[start_group]"
        elif self.type == wiretype.end_group.value:
            self.value=b"[end_group]"
        else:
            self.value=b""
        return self.value

    def readField(self, data):
        tag = self.readTag()
        if (tag==-1):
            return -1
        data.tag=tag
        try:
            data.value = self.readValue()
        except:
            return -2
        return tag

    def readAllFields(self, debug=False):
        result={}
        data=protodata()
        self.error=0
        while (True):
            tag=self.readField(data)
            if (tag==-1):
                break
            if (tag==-2):
                print("Data issue after Pos:%08X" % self.pos)
                self.error=1
                break
            if (data.value==b"[end_group]"):
                break
            if not data.tag in result:
                result[data.tag]=[]
            result[data.tag].append(data.value)
            if (debug):
                print("Tag:" + str(data.tag) + ";Value:" + str(data.value))
        return result
     
    def lasterror(self):
        return self.error
        
    def getpos(self):
        return self.pos
        
    def datalen(self):
        return len(self.buf)


def recurseproto(data, level):
    info = ""
    pos = 0
    datalen = len(data)
    fdb = []
    errorflag = 0
    tmp = 0
    while (pos < datalen):
        try:
            phandler = protobuf(data[pos:])
        except:
            break
        ft = phandler.readAllFields(False)
        # print(ft)
        fdb.append(ft)
        if phandler.lasterror() != 0:
            #print("LastError: %d" % phandler.lasterror())
            #print(ft)
            errorflag = 1
            break
        tmp = phandler.getpos()
        pos += tmp

    for arry in fdb:
        i = 0
        fill = " " * level
        info += fill + "<item=\"%d\">\n" % i
        for ft in arry:
            i += 1
            for field in arry[ft]:
                if isinstance(field, bytearray) or isinstance(field,bytes):
                    if len(field) == 0:
                        continue
                    if int(field[0]) < 0x30:
                        tmp = recurseproto(field, level + 1)
                        info += tmp
                    else:
                        info += fill + " <key:" + str(ft) + "><value:\"" + field.decode('utf-8') + "\">" + "\n"
                else:
                    info += fill + " <key:" + str(ft) + "><value:" + str(field) + ">" + "\n"

        info += fill + "<\item>\n"
    return info

def pseudoxml(dat):
    return recurseproto(dat, 0)