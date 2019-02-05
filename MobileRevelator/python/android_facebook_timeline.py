#Pluginname="Facebook Timeline - Katana (Android)"
#Filename="timeline_db"
#Type=App

import struct
import zlib
from Library import flatbuffer

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select rowid, cachekey, timestamp, data from cache;")
    if (conn==-1):
        print ("Error: "+ctx.sqlite_last_error(db))
        return
    rows=ctx.sqlite_get_data_size(conn)[0]
    if rows==0:
        return
    oldpos=0
    t=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        cachekey=ctx.sqlite_get_data(conn,i,1)
        timestamp=ctx.sqlite_get_data(conn,i,2)
        type=cachekey[:cachekey.find(":")]
        data=ctx.sqlite_get_data(conn,i,3)
        try:
            if (data.size()==0):
                continue
        except:
            continue
            
        data=data.data()
        
        offsets=[]
        pos=0
        while (pos!=-1):
            pos=data.find(b"FLAT",pos)
            if (pos!=-1):
                offsets.append(pos-4)
            else:
                break
            pos+=1
        
        for i in range(0,len(offsets)):
                if (i < len(offsets)-1):
                    dat=data[offsets[i]:offsets[i+1]]
                else:
                    dat=data[offsets[i]:]
                ft = flatbuffer.flatbuffer(dat)

                rootoffset = ft.getint(0)
                roottbl = ft.table_offsets(rootoffset)
                
                contact=""
                contact_alias=""
                message=""
                desc=""
                
                if (len(roottbl)>0):
                    t0=ft.stable_offsets(roottbl[0])
                    
                    if (len(t0)>17):
                        type+=":1"+ft.sstring(t0[9])
                        contact=ft.sstring(t0[10])
                        if t0[16]!=0:
                            contact_alias=ft.sstring(t0[16])
                        elif t0[17]!=0:
                            contact_alias=ft.sstring(t0[17])
                    if (len(t0)>18):
                        t0_t18=ft.stable_offsets(t0[18])
                        if (len(t0_t18)>1):
                            t0_t18_t1=ft.stable_offsets(t0_t18[1])
                            if (len(t0_t18_t1)>0):
                                desc="Info:\""+ft.sstring(t0_t18_t1[0])+"\";"
                
                if (len(roottbl)>9) and "Error" not in ft.sstring(roottbl[9]):
                    type+=":"+ft.sstring(roottbl[9])
                    contact=ft.sstring(roottbl[10])
                    if roottbl[16]!=0:
                            contact_alias=ft.sstring(roottbl[16])
                    elif roottbl[17]!=0:
                            contact_alias=ft.sstring(roottbl[17])
                    elif roottbl[21]!=0:
                            contact=ft.sstring(roottbl[13])
                            contact_alias=ft.sstring(roottbl[21])
                            type=ft.sstring(roottbl[11])
                            if roottbl[38]!=0:
                                 desc="Url:\""+ft.sstring(roottbl[38])+"\";"
                    t18=ft.stable_offsets(roottbl[18])
                    #print(t18)
                    if (len(t18)>5):
                        try:
                            t18_t5=ft.stable_offsets(t18[5])
                            if (len(t18_t5)>0):
                                t18_t5_s0=ft.svector_offsets(t18_t5[0])
                                for x in range(0,len(t18_t5_s0)):
                                    ct=ft.table_offsets(t18_t5_s0[x])
                                    if (len(ct)>6):
                                        desc+=ft.sstring(ct[4])
                                        ct_t5=ft.stable_offsets(ct[5])
                                        if (len(ct_t5)>0):
                                            desc+=":\""+ft.sstring(ct_t5[0])+"\""
                                        desc+=","+ft.sstring(ct[6])+";"
                        except:
                            print(t18)
                if (len(roottbl)>27):
                    t27=ft.stable_offsets(roottbl[27])
                    if (len(t27)>0):
                        t27_s0=ft.svector_offsets(t27[0])
                        if (len(t27_s0)>0):
                            t27_s0_t0=ft.table_offsets(t27_s0[0])
                            if (len(t27_s0_t0)>4):
                                subtype=ft.sstring(t27_s0_t0[3])
                                subinfo=ft.sstring(t27_s0_t0[4])
                                if (len(t27_s0_t0)>5):
                                    t27_s0_t0_t5=ft.stable_offsets(t27_s0_t0[5])
                                    if (len(t27_s0_t0_t5)>0):
                                        desc+=subinfo+":"
                                        desc+="\""+ft.sstring(t27_s0_t0_t5[0])+"\";"
                if (len(roottbl)>29):
                    t29=ft.stable_offsets(roottbl[29])
                    if (len(t29)>0):
                       subinfo=ft.sstring(t29[2])
                       if (len(subinfo)>0):
                           desc+="Profile-Picture:\""+subinfo+"\";"
                           
                if (len(roottbl)>45):
                    type+=":"+ft.sstring(roottbl[26])
                    contact=ft.sstring(roottbl[23])
                    if roottbl[24]!=0:
                            contact_alias=ft.sstring(roottbl[24])
                            if roottbl[25]!=0:
                                 desc="Url:\""+ft.sstring(roottbl[25])+"\";"
                    st45=ft.stable_offsets(roottbl[45])
                    if (len(st45)>4):
                        try:
                            st45_t4=ft.stable_offsets(st45[4])
                            if (len(st45_t4)>0):
                                st45_t4_sv0=ft.svector_offsets(st45_t4[0])
                                for x in range(0,len(st45_t4_sv0)):
                                    ct=ft.table_offsets(st45_t4_sv0[x])
                                    if (len(ct)>1):
                                        sct=ft.stable_offsets(ct[1])
                                        if (len(sct)>6):
                                            desc+=ft.sstring(sct[2])
                                            sct_t6=ft.stable_offsets(sct[6])
                                            if (len(sct_t6)>0):
                                                desc+=":\""+ft.sstring(sct_t6[0])+"\""
                        except:
                            print(st45)
                
                if (contact!=""):
                    ctx.gui_set_data(t,0,id)
                    ctx.gui_set_data(t,1,type)
                    ctx.gui_set_data(t,2,contact)
                    ctx.gui_set_data(t,3,contact_alias)
                    ctx.gui_set_data(t,4,message)
                    ctx.gui_set_data(t,5,timestamp)
                    ctx.gui_set_data(t,6,desc)
                    t+=1
        
    ctx.sqlite_cmd_close(conn)


def main():
    headers=["rowid (int)","type (QString)","contact (QString)","contact_alias (QString)","message (QString)","timestamp (int)", "desc (QString)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Facebook Timeline: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."