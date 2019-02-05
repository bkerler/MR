import struct
from struct import pack,unpack

class JavaFunc(object):
    def __init__(self,data):
        self.__globalpos=0x0
        self.__value=data
        self.__datalen=len(data)

    def seek(self,pos):
        self.__globalpos=pos

    def readInt32(self):
        if (self.__globalpos>self.__datalen):
            return -1
        val=struct.unpack('I',self.__value[self.__globalpos:self.__globalpos+4])[0]
        self.__globalpos+=4
        return val

    def readBool(self):
        if (self.__globalpos>self.__datalen):
            return -1
        val=struct.unpack('I',self.__value[self.__globalpos:self.__globalpos+4])[0]
        self.__globalpos+=4
        return (val&1)

    def readInt64(self):
        if (self.__globalpos>self.__datalen):
            return -1
        val=struct.unpack('Q',self.__value[self.__globalpos:self.__globalpos+8])[0]
        self.__globalpos+=8
        return val

    def getdouble(self):
        if (self.__globalpos>self.__datalen):
            return -1
        val=struct.unpack('d',self.__value[self.__globalpos:self.__globalpos+8])[0]
        self.__globalpos+=8
        return val
        
    def readDouble(self):
        if (self.__globalpos>self.__datalen):
            return -1
        val=struct.unpack('d',self.__value[self.__globalpos:self.__globalpos+8])[0]
        self.__globalpos+=8
        return val

    def readString(self):
        if ((self.__globalpos+4)>self.__datalen):
            #print("Decoding error 1")
            return ""
        len=self.readInt32()
        rpos=0
        if ((len&0xFF)==0xFE):
            len=(len>>8)
        else:
            len=(len&0xFF)
            self.__globalpos-=3
            rpos=1
        str=""
        if ((self.__globalpos+len)>self.__datalen):
            #print("Decoding error 2")
            return ""
        try:
            str=self.__value[self.__globalpos:self.__globalpos+len].decode("utf-8")
        except:
            str="Decoding error: Len: "+hex(len)+" "
            for i in range(self.__globalpos,self.__globalpos+3):
                str+=hex(self.__value[i])+" "
            #print(str)
            return ""
        nval=int((self.__globalpos+len)/4)*4
        if (((self.__globalpos+len)%4)>0):
            nval+=4
        #str=hex(globalpos)+" - "+hex(len)+" - "+hex(nval)+" - "+hex(rpos)
        self.__globalpos=nval
        return str

    def readByteArray(self):
        if ((self.__globalpos+4)>self.__datalen):
            return "Decoding error"
        len=self.readInt32()
        rpos=0
        if ((len&0xFF)==0xFE):
            len=(len>>8)
        else:
            len=(len&0xFF)
            self.__globalpos-=3
            rpos=1
        if ((self.__globalpos+len)>self.__datalen):
            return "Decoding error"
        str=""
        for i in range(self.__globalpos,self.__globalpos+len):
            str+='{:02x}'.format(self.__value[i])
        nval=int((self.__globalpos+len)/4)*4
        if (((self.__globalpos+len)%4)>0):
            nval+=4
        self.__globalpos=nval
        return str

    def hashcode(passcode):
        h = 0
        for i in range(0, len(passcode)):
            h = 31 * h + ord(passcode[i:i + 1])
            h = h & 0xffffffff
        return h;