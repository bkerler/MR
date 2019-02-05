#Pluginname="Facebook Events (Android)"
#Filename="events_db"
#Type=App

import struct
import zlib
from Library import flatbuffer

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select rowid, facebook_id, start_time_millis, common_fragment from events;")
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
        facebook_id=ctx.sqlite_get_data(conn,i,1)
        timestamp=ctx.sqlite_get_data(conn,i,2)
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
                type = ft.getshort(roottbl[0])
                if (type==0x101):
                    contact=""
                    contact_alias=""
                    message=""
                    desc=""
                    if (len(roottbl)>0):
                        desc="Description:\""+ft.sstring(roottbl[24])+"\","
                        desc+="\""+ft.sstring(roottbl[27])+"\","
                        desc+="\""+ft.sstring(roottbl[28])+"\";"
                        desc+="Url:\""+ft.sstring(roottbl[30])+"\";"
                        if (len(roottbl)>66):
                            sv66=ft.svector_offsets(roottbl[66])
                            st65=ft.stable_offsets(roottbl[65])
                            st64=ft.stable_offsets(roottbl[64])
                            if (len(st64)>0):
                                message=ft.sstring(st64[0])
                            if (len(st65)>1):
                                info=ft.sstring(st65[1])
                            if (len(sv66)>0):
                                sv66_t0=ft.table_offsets(sv66[0])
                                if len(sv66_t0)>5:
                                    contact=ft.sstring(sv66_t0[2])
                                    contact_alias=ft.sstring(sv66_t0[3])
                                    desc+="Friendstatus:\""+ft.sstring(sv66_t0[5])+"\";"

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
    ctx.gui_setMainLabel("Facebook Event: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."