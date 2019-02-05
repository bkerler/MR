import binascii
import struct

class flatbuffer:
    def __init__(self, buffer):
        self.data=buffer

    def getint(self,offset):
        return struct.unpack("<i",self.data[offset:offset+4])[0]

    def getuint(self,offset):
        return struct.unpack("<I",self.data[offset:offset+4])[0]

    def getint64(self,offset):
        return struct.unpack("<q",self.data[offset:offset+8])[0]

    def getuint64(self,offset):
        return struct.unpack("<Q",self.data[offset:offset+8])[0]

    def getshort(self,offset):
        return struct.unpack("<H",self.data[offset:offset+2])[0]

    def soffset (self,offset):
        offs=self.getint(offset)
        return offset+offs

    def sstring (self,offset):
        try:
            return self.string(self.soffset(offset))
        except:
            return ""

    def string (self,offset):
        strlen=self.getint(offset)
        if (strlen>len(self.data)):
            return ""
        try:
            st=self.data[offset+4:offset+4+strlen].decode()
        except:
            st="Error on decoding"
        return str(st)

    def vector (self,offset):
        if (offset==0):
            return []
        count=self.getint(offset)
        dataoffsets=[]
        arraystart=offset+4
        for i in range(0,count):
            offs=self.getuint(arraystart+(i*4))
            dataoffsets.append(offs)
        return dataoffsets

    def vector_offsets (self,offset):
        if (offset==0):
            return []
        count=self.getint(offset)
        dataoffsets=[]
        arraystart=offset+4
        for i in range(0,count):
            offs=self.getuint(arraystart+(i*4))
            if (offs>len(self.data)):
                return []
            if (offs>0):
                offs=offs+offset+((i+1)*4)
            dataoffsets.append(offs)
        return dataoffsets

    def svector_offsets (self,offset):
        if (offset==0):
            return []
        return self.vector_offsets(self.soffset(offset))

    def table (self,offset):
        if (offset==0):
            return []
        tableoffset=self.getint(offset)
        arrayoffset=offset-tableoffset
        tablelen=self.getshort(arrayoffset)-4
        tablesz=self.getshort(arrayoffset+2)
        dataoffsets=[]
        arraystart=arrayoffset+4
        for i in range(0,int(tablelen/2)):
            offs=self.getshort(arraystart+(i*2))
            dataoffsets.append(offs)
        return dataoffsets

    def stable_offsets (self,offset):
        if (offset==0):
            return []
        return self.table_offsets(self.soffset(offset))

    def table_offsets (self,offset):
        if (offset==0):
            return []
        tableoffset=self.getint(offset)
        arrayoffset=offset-tableoffset
        dataoffsets = []
        if ((arrayoffset+2)>len(self.data)):
            return dataoffsets
        tablelen=self.getshort(arrayoffset)-4
        tablesz=self.getshort(arrayoffset+2)
        arraystart=arrayoffset+4
        if ((arraystart+tablelen)>len(self.data)):
            return dataoffsets
        for i in range(0,int(tablelen/2)):
            offs=self.getshort(arraystart+(i*2))
            if offs>0:
                offs=offs+offset
                dataoffsets.append(offs)
            else:
                dataoffsets.append(offs)
        return dataoffsets

    def autodetect (self,offset):
        try:
            tableoffset = self.getint(offset)
        except:
            return "error"
        if (offset<0):
            return "integer"
        if (tableoffset<0):
            tbl = self.table_offsets(offset)
            if (len(tbl) > 0):
                return "table"
        v=offset-tableoffset
        tablelen=0
        if (v < len(self.data)) and (v>0):
            tablelen = self.getshort(v)
        if ((offset-tableoffset) > 0):
            if (tableoffset==tablelen):
                tbl=self.table_offsets(offset)
                if (len(tbl)>0):
                    return "table"
        length=tableoffset
        if (length>len(self.data)):
            return "integer"
        if (length>1):
            ischar=True
            for z in range(0,length):
                if (((self.data[offset+4+z])<0x0A) or ((self.data[offset+4+z])>0xEF)):
                    ischar=False
                    break
            if (ischar):
                return "string"
        vec=self.vector_offsets(offset)
        if (len(vec)>0):
            return "vector"
        return "integer"

    def autodecode(self, posttbl, name, lasttype, level):
        tabs="\t"*level
        xml=tabs+"{\n"

        for x in range(0, len(posttbl)):
            info = ""
            if posttbl[x] == 0:
                continue
            if (lasttype == "v"):
                offset = posttbl[x]
            else:
                if ((posttbl[x])>len(self.data)):
                    h=hex(posttbl[x])
                    xml += tabs + "\t" + "<" + name + "_" + str(x) + "=" + h + "/>}\n"
                    return xml
                else:
                    offset = self.soffset(posttbl[x])
                    info="s"
            type = self.autodetect(offset)
            if (type == "string"):
                xml+=tabs+"\t"+"<"+name + "_"+str(x)+"=\"" + self.string(offset) + "\"/>\n"
            elif (type == "error"):
                try:
                    z=self.string(posttbl[x])
                    if z=="":
                        xml += tabs + "\t" + "<" + name + "_" + str(x) + "=" + hex(posttbl[x]) + " "+info+"Offset_Value=" + str(offset)+ "/>\n"
                    else:
                        xml+=tabs+"\t"+"<"+name + "_"+str(x)+"=\"" + z + "\"/>\n"
                except:
                        xml += tabs + "\t" + "<" + name + "_" + str(x) + " "+info+"Offset_Value=" + str(offset) + "/>\n"
            elif (type == "table"):
                tbl = self.table_offsets(offset)
                if (len(tbl)>200):
                    return xml
                xml+=self.autodecode(tbl, name + "_"+info+"t" + str(x)+"["+str(posttbl[x])+"]", "t",level+1)
            elif (type == "vector"):
                tbl = self.vector_offsets(offset)
                xml+=self.autodecode(tbl, name + "_"+info+"v" + str(x)+"["+str(posttbl[x])+"]", "v",level+1)
            elif (type == "integer"):
                if ((posttbl[x])>len(self.data)):
                    h = hex(posttbl[x])
                    ho = str(offset)
                    xml += tabs + "\t" + "<" + name + "_" + str(x) + "=" + h + " "+info+"Offset_Value="+ho+"/>\n"
                else:
                    m = hex(self.getint(posttbl[x]))
                    xml+=tabs+"\t"+"<"+name + "_" + str(x) + "=" + m+"/>\n"
            else:
                xml+=tabs+"\t"+"<"+name + "_" + str(x) + "="+type+"/>\n"
        xml+=tabs+"}\n"
        return xml

    def flattoxml(self):
        rootoffset = self.getint(0)
        roottbl = self.table_offsets(rootoffset)
        return self.autodecode(roottbl, "s", "t",0)

'''
def main():
    with open("../monsterdata.bin","rb") as fr:
        data=bytes(fr.read())

    ft=flatbuffer(data)
    rootoffset=ft.getint(0)
    roottbl=ft.table_offsets(rootoffset)

    mana=ft.getshort(roottbl[2])
    name=ft.string(ft.soffset(roottbl[3]))

    vec=ft.vector_offsets(ft.soffset(roottbl[7]))
    tbl7=ft.table_offsets(vec[0])

    tbl9=ft.table_offsets(ft.soffset(roottbl[9]))
    name9=ft.string(ft.soffset(tbl9[0]))

    name9=name9
main()
'''