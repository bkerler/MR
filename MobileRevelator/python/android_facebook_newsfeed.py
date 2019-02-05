#Pluginname="Facebook Newsfeed (Android)"
#Filename=""
#Type=App

import struct
import os
import sys
import tempfile
from Library import flatbuffer

def convertdata(filenames):
    row=0
    oldpos=0
    kk=0
    zfields=[]
    for fsname in filenames:
        filename=tempfile.gettempdir()+"/"+fsname[fsname.rfind("/")+1:].replace(":","")
        offsets=[]
        
        newpos=int(kk/len(filenames)*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        kk=kk+1
        
        if ctx.fs_file_extract(fsname,filename):
            print("Running Facebook Newsfeed conversion: "+filename[filename.rfind("/")+1:])
            with open(filename,"rb") as tt:
                data=tt.read()
            os.remove(filename)
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

                try:
                    rootoffset = ft.getint(0)
                    roottbl = ft.table_offsets(rootoffset)
                    type = ft.getshort(roottbl[0])
                except:
                    continue
                #print ("Type: "+str(type))
                #print(ft.flattoxml())

                if (type==60) and (arguments["user"]==True):
                    # People you may know
                    posttbl = ft.stable_offsets(roottbl[1])
                    t2 = ft.svector_offsets(ft.stable_offsets(posttbl[1])[0])
                    for h in range(0, len(t2)):
                        t3 = ft.table_offsets(t2[h])
                        t4 = ft.stable_offsets(t3[0])
                        zfield = {}
                        zfield["type"] = "60 - People you may know"
                        zfield["filename"]=fsname
                        zfield["message"]=""
                        zfield["desc"]=""
                        zfield["package"]=""
                        zfield["contact"] = ft.sstring(t4[39])
                        zfield["contact_alias"] = ft.sstring(t4[69])
                        zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                        if (len(t4) > 87):
                            tz=ft.stable_offsets(t4[87])
                            if (len(tz)>3):
                                zfield["desc"] = "Url: "+ft.sstring(tz[3])
                        zfields.append(zfield)
                elif (type==25) and (arguments["user"]==False):
                    #posts
                    zfield={}
                    posttbl = ft.stable_offsets(roottbl[1])

                    v3 = ft.svector_offsets(posttbl[3])  # userinfo
                    usertbl=ft.table_offsets(v3[0])
                    usertype=ft.sstring(usertbl[0])
                    zfield["type"] = "25 - Timeline"
                    zfield["filename"] = fsname
                    zfield["contact"]=ft.sstring(usertbl[32])
                    zfield["contact_alias"]=ft.sstring(usertbl[48])
                    zfield["package"]=""
                    zfield["desc"]=""
                    zfield["desc"]+=usertype+":"
                    zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                    zfield["message"]=""
                    
                    if (len(posttbl)>20):
                        zfield["timestamp"]=str(ft.getint64(posttbl[20])*1000)
                    if (len(posttbl)>22):
                        t22 = ft.stable_offsets(posttbl[22])
                        if (len(t22)>4):
                            zfield["desc"] += ft.sstring(t22[4])+";"  #Vorgeschlagen

                    t53 = ft.stable_offsets(posttbl[53])  # url
                    if (len(t53)>10):
                        zfield["desc"] += ft.sstring(t53[0])+":"+ft.sstring(t53[10])+";" #External Url

                    t40 = ft.stable_offsets(posttbl[40])  # description
                    if (len(t40)>3):
                        t1_40_3=ft.svector_offsets(t40[3])
                        if (len(t1_40_3)>0):
                            t1_40_3_0=ft.table_offsets(t1_40_3[0])
                            if (len(t1_40_3_0)>0):
                                tm=ft.stable_offsets(t1_40_3_0[0])
                                if (len(tm)>26):
                                    zfield["desc"] += ft.sstring(tm[0])+":["+ft.sstring(tm[10])+":\""+ft.sstring(tm[13])+"\"];" #hashtag
                    if (len(posttbl)>92):
                        t3 = ft.stable_offsets(posttbl[92])
                        if (len(t3) > 4):
                            zfield["desc"]+=ft.sstring(t3[4])+";"
                    if (posttbl[39]!=0):
                        zfield["desc"]+="Id_fbid:"+ft.sstring(posttbl[39])+";" #id_fbid

                    if (len(t40) > 4):
                            zfield["message"] = "Post: \"" + ft.sstring(t40[4]) + "\"" #Post

                    v10 = ft.svector_offsets(posttbl[10])
                    if (len(v10)>0):
                        v10_t0 = ft.table_offsets(v10[0])
                        if (len(v10_t0)>12):
                            v10_t0_t3 = ft.stable_offsets(v10_t0[3])
                            if (len(v10_t0_t3)>4):
                                zfield["desc"] = "Post: \"" + ft.sstring(v10_t0_t3[4])+"\";"
                            v10_t0_t8 = ft.stable_offsets(v10_t0[8])
                            if (len(v10_t0_t8)>73):
                                if (v10_t0_t8[73]!=0):
                                    zfield["desc"] += "Video url: " + ft.sstring(v10_t0_t8[73]) + ";"
                            tm=ft.stable_offsets(v10_t0[12])
                            if (len(tm)>4):
                                zfield["desc"] += "Attached Link: " + ft.sstring(tm[4])+";"

                    t1_9 = ft.stable_offsets(posttbl[9])  # comment
                    if (len(t1_9)>40):
                        t1_9_40=ft.stable_offsets(t1_9[40])
                        if (len(t1_9_40)>4):
                            zfield["message"] = "Comment: \"" + ft.sstring(t1_9_40[4]) + "\""
                    if (len(t1_9)>53):
                        t1_9_53=ft.stable_offsets(t1_9[53])
                        if (len(t1_9_53)>10):
                            zfield["desc"] += ft.sstring(t1_9_53[0]) + ":" + ft.sstring(t1_9_53[10])+";" #Photo
                        if (len(t1_9)>76):
                            zfield["desc"] += "Url: \""+ft.sstring(t1_9[76])+"\";" #Photo Url

                    t69 = ft.stable_offsets(posttbl[69])  # group
                    if (len(t69)>46):
                        zfield["package"] +=ft.sstring(t69[0])+"[\""+ft.sstring(t69[46])+"\"], Id:"+ft.sstring(t69[37]) #Group id

                    t66 = ft.stable_offsets(posttbl[66])  # comment description
                    if (len(t66)>4):
                        zfield["desc"] += ft.sstring(t66[4]) + ";"  # Description who commented

                    t45 = ft.stable_offsets(posttbl[45])  # forwhom
                    if (len(t45)>9):
                        zfield["desc"] += "For:" + ft.sstring(t45[5]) + "["+ft.sstring(t45[9])+"];" #rights

                    #if (len(t2)>4):
                    #    postad = ft.sstring(t2[4])
                    zfields.append(zfield)
                elif (type==27) and (arguments["user"]==False):
                    #posts
                    zfield={}
                    zfield["timestamp"]=ctx.fs_gettime(fsname)[1]

                    posttbl = ft.stable_offsets(roottbl[1])
                    
                    t2 = ft.stable_offsets(posttbl[40])
                    t3 = ft.stable_offsets(posttbl[92])
                    
                    if (len(posttbl)>87):
                        zfield["timestamp"]=str(ft.getint64(posttbl[87])*1000)
                    
                    if (len(posttbl)>3):
                        t0 = ft.svector_offsets(posttbl[3])
                        if (len(t0)>0):
                            usertbl=ft.table_offsets(t0[0])
                            if (len(usertbl)>48):
                                usertype=ft.sstring(usertbl[0])
                                zfield["contact"]=ft.sstring(usertbl[29])
                                zfield["contact_alias"]=ft.sstring(usertbl[48])
                    
                    zfield["type"] = "27 - Timeline"
                    zfield["filename"] = fsname
                    zfield["message"]=""
                    zfield["desc"]=""
                    zfield["package"]=""
                    
                    if (len(t3) > 4):
                        zfield["desc"]+=ft.sstring(t3[4])+";"
                    if ((len(posttbl)>39) and posttbl[39]!=0):
                        zfield["desc"]+="Id_fbid:"+ft.sstring(posttbl[39])+";"
                    
                    if (len(posttbl)>47):
                        t5 = ft.stable_offsets(posttbl[47])
                        if (len(t5)>10):
                            zfield["desc"] += "For:" + ft.sstring(t5[10]) + "["+ft.sstring(t5[10])+"];"
                    
                    if (len(posttbl)>27):
                        t4 = ft.stable_offsets(posttbl[27])
                        if (len(t4) > 5):
                            t45 = ft.svector_offsets(t4[5])
                            if (len(t45)>0):
                                t450 = ft.table_offsets(t45[0])
                                t4504 = ft.stable_offsets(t450[4])
                                if (len(t4504) > 4):
                                    zfield["message"]="Comment: \"" + ft.sstring(t4504[4]) +"\""
                    
                    if (len(posttbl)>9):
                        t1 = ft.stable_offsets(posttbl[9])
                        if (len(t1) > 54):
                            t19 = ft.stable_offsets(t1[54])
                            try:
                                zfield["desc"] += "Mediatype: " + ft.sstring(t19[0]) +";"
                            except:
                                mediatype = ""
                            if (len(t19)>10):
                                zfield["desc"] += "Mediaid: " + ft.sstring(t19[10]) + ";"
                            if (len(t1)>76):
                                try:
                                    zfield["desc"] += "Mediaurl: " + ft.sstring(t1[76]) + ";"
                                except:
                                    t1=t1
                        if (len(t1) > 40):
                            t19=ft.stable_offsets(t1[40])
                            if (len(t19) > 4):
                                zfield["message"] = "Post: \"" + ft.sstring(t19[4]) + "\""
                    #if (len(t2)>4):
                    #    postad = ft.sstring(t2[4])
                    zfields.append(zfield)
                elif (type==34) and (arguments["user"]==True):
                    #People you may know
                    posttbl = ft.stable_offsets(roottbl[1])
                    t40 = ft.svector_offsets(ft.stable_offsets(posttbl[0])[0])
                    for h in range(0,len(t40)):
                        t3 = ft.table_offsets(t40[h])
                        t4 = ft.stable_offsets(t3[0])
                        zfield={}
                        zfield["type"]  =  "34 - People you may know"
                        zfield["filename"] = fsname
                        zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                        zfield["contact"] = ft.sstring(t4[36])
                        zfield["contact_alias"] = ft.sstring(t4[61])
                        zfield["message"]=""
                        zfield["desc"]=""
                        zfield["package"]=""
                        if (len(t3)>1):
                            jj=ft.stable_offsets(t3[1])
                            if (len(jj)>4):
                                zfield["desc"] = ft.sstring(jj[4])
                        zfields.append(zfield)
                elif (type==37) and (arguments["user"]==True):
                    #People you may know
                    posttbl = ft.stable_offsets(roottbl[1])
                    t2 = ft.svector_offsets(ft.stable_offsets(posttbl[0])[0])
                    for h in range(0,len(t2)):
                        t3 = ft.table_offsets(t2[h])
                        t4 = ft.stable_offsets(t3[0])
                        zfield={}
                        zfield["type"]  =  "37 - People you may know"
                        zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                        zfield["filename"] = fsname
                        zfield["contact"] = ft.sstring(t4[35])
                        zfield["contact_alias"] = ft.sstring(t4[63])
                        zfield["message"]=""
                        zfield["desc"]=""
                        zfield["package"]=""
                        if (len(t3)>1):
                            jj=ft.stable_offsets(t3[1])
                            if (len(jj)>4):
                                zfield["desc"] = ft.sstring(jj[4])
                        zfields.append(zfield)
                elif (type==108) and (arguments["user"]==False):
                    #Group message
                    posttbl = ft.stable_offsets(roottbl[1])
                    t5=ft.svector_offsets(posttbl[5])
                    zfield = {}
                    zfield["type"] = "108 - Group info"
                    zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                    zfield["filename"] = fsname
                    zfield["contact"] = ""
                    zfield["contact_alias"] = ""
                    zfield["message"]=""
                    zfield["desc"]=""
                    zfield["package"]=""
                    for x in t5:
                        tbl=ft.table_offsets(x) #Group entries
                        if (len(tbl)>1):
                            st0 = ft.stable_offsets(tbl[0])
                            if (len(st0)>4):
                                zfield["desc"] = ft.sstring(st0[4]) + ";"
                            st1 = ft.stable_offsets(tbl[1])
                            if (len(st1)>77):
                                zfield["desc"] += "Group: "+ft.sstring(st1[23])+";"
                                if (st1[31]>0):
                                    zfield["desc"] += "Group Alias: " + ft.sstring(st1[31]) + ";"
                                st77=ft.stable_offsets(st1[77])
                                if (len(st77)>4):
                                    zfield["desc"] += ft.sstring(st77[4]) + ";"
                            zfield["desc"] += "["
                            if (st0[3]>0):
                                st03=ft.svector_offsets(st0[3])
                                for x in st03:
                                    user = ft.table_offsets(x)
                                    if (user[0]>0):
                                        tt=ft.stable_offsets(user[0])
                                        if (len(tt)>10):
                                            zfield["desc"] += ft.sstring(tt[0]) + ":"
                                            zfield["desc"] += ft.sstring(tt[10]) + ","
                                        if (len(tt) > 13):
                                            zfield["desc"] += "\""+ft.sstring(tt[13]) + "\","
                                        if (len(tt) > 26):
                                            zfield["desc"] += "Url: \""+ft.sstring(tt[26]) + "\";"
                            if (st0[0]>0):
                                st03 = ft.svector_offsets(st0[0])
                                for x in st03:
                                    user = ft.table_offsets(x)
                                    if (user[3] > 0):
                                        tt=ft.svector_offsets(user[3])
                                        for xx in tt:
                                            hh=ft.table_offsets(xx)
                                            if (len(hh)>10):
                                                zfield["desc"] += ft.sstring(hh[0]) + ":"
                                                zfield["desc"] += ft.sstring(hh[10]) + ","
                                            if (len(hh) > 13):
                                                zfield["desc"] += "\""+ft.sstring(hh[13]) + "\","
                                            if (len(hh) > 26):
                                                zfield["desc"] += "Url: \""+ft.sstring(hh[26]) + "\";"

                            zfield["desc"] += "]"
                        zfields.append(zfield)
                elif (type==7) and (arguments["user"]==False):
                    posttbl=ft.stable_offsets(roottbl[1])
                    rr=ft.svector_offsets(posttbl[1])
                    zfield={}
                    zfield["desc"]=""
                    if (len(rr)>0):
                        tbl1 = ft.table_offsets(rr[0])
                        if (len(tbl1)>0):
                            zfield["desc"]="Action: "+ft.sstring(tbl1[0])+";"
                        if (len(tbl1)>95) and tbl1[95]!=0:
                            zfield["desc"]+="Actiontype: "+ft.sstring(tbl1[95])+";"
                    zfield["type"] = "7 - Timeline"
                    zfield["filename"] = fsname
                    zfield["timestamp"]=ctx.fs_gettime(fsname)[1]
                    zfield["message"]=""
                    zfield["package"]=""
                    zfield["contact"]=""
                    zfield["contact_alias"]=""
                    if (len(posttbl)>3):
                        tbl3 = ft.table_offsets(ft.svector_offsets(posttbl[3])[0])
                        poster = ft.sstring(tbl3[0])
                        id=""
                        user=""
                        #if (poster=='User'):
                        zfield["contact"] = ft.sstring(tbl3[24])
                        zfield["contact_alias"] = ft.sstring(tbl3[44])
                        if (len(tbl3)>52):
                            tbl3_52 = ft.stable_offsets(tbl3[52])
                            if (len(tbl3_52)>3):
                                zfield["desc"] += "Profileurl: "+ft.sstring(tbl3_52[3])+";"
                                #t3_52_6 = ft.sstring(tbl3_52[6])
                                #prpfile_fb = ft.sstring(tbl3[68])

                    if (len(posttbl)>12):
                        t12 = ft.sstring(posttbl[12])
                        if (len(posttbl)>21):
                            zfield["timestamp"] = str(ft.getint64(posttbl[21])*1000)
                        if (len(posttbl) > 71):
                            zfield["timestamp"] = str(ft.getint64(posttbl[71])*1000)

                    '''
                    tbl27 = ft.stable_offsets(posttbl[27])
                    t27_13 = ft.sstring(tbl27[13])
                    t27_20 = ft.sstring(tbl27[20])
                    fbid = ft.sstring(tbl27[25])
                    tbl27_41 = ft.stable_offsets(tbl27[41])
                    post_user = ft.sstring(tbl27_41[69])
                    tbl27_56 = ft.svector_offsets(tbl27[56])
                    t27_56_0 = ft.string(tbl27_56[0])

                    t34 = ft.sstring(posttbl[34])
                    t37 = ft.sstring(posttbl[37])
                    '''
                    if (len(posttbl)>42):
                        zfield["desc"] += "Id_fbid: "+ft.sstring(posttbl[42])
                    if (len(posttbl)>50):
                        tbl50 = ft.stable_offsets(posttbl[50])
                        if (len(tbl50)>5):
                            zfield["message"] = "Post: \""+ft.sstring(tbl50[5])+"\""
                    if (len(posttbl)>80):
                        tbl80 = ft.stable_offsets(posttbl[80])
                        if (len(tbl80)>5):
                            zfield["message"] += "Shared: \""+ft.sstring(tbl80[5])+"\""
                    '''
                    tbl65 = ft.stable_offsets(posttbl[65])
                    subtype = ft.sstring(tbl65[0])
                    t65_12 = ft.sstring(tbl65[12])

                    t67 = ft.sstring(posttbl[67])
                    t83 = ft.sstring(posttbl[83])
                    '''

                    if (len(posttbl)>84):
                        tbl84 = ft.stable_offsets(posttbl[84])
                        if (len(tbl84)>1):
                            #langcode0 = ft.sstring(tbl84[0])
                            zfield["desc"]+="Language: "+ft.sstring(tbl84[1])+";"
                            #langcode1 = ft.sstring(tbl84[2])
                            #language1 = ft.sstring(tbl84[3])

                    if (len(posttbl)>86):
                        zfield["desc"]+="Storyurl: "+ft.sstring(posttbl[86])+";"
                    zfields.append(zfield)
                
    for zfield in zfields:
        ctx.gui_set_data(row,0,str(row))
        ctx.gui_set_data(row,1,zfield["filename"])
        ctx.gui_set_data(row,2,zfield["type"])
        ctx.gui_set_data(row,3,zfield["package"])
        ctx.gui_set_data(row,4,zfield["contact"])
        ctx.gui_set_data(row,5,zfield["contact_alias"])
        ctx.gui_set_data(row,6,zfield["message"])
        ctx.gui_set_data(row,7,zfield["timestamp"])
        ctx.gui_set_data(row,8,zfield["desc"])
        row+=1
                
def main():
    ctx.gui_setMainLabel("Facebook Newsfeed: Parsing Strings");
    ctx.gui_setMainProgressBar(0)
    filenames=ctx.pluginfilenames()
    headers=["rowid (int)","filename (QString)","type (QString)","package (QString)", "contact (QString)","contact_alias (QString)","message (QString)","timestamp (int)", "desc (QString)"]
    ctx.gui_set_headers(headers)
    convertdata(filenames)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."