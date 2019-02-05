#Pluginname="Herrevad Google GMS (Android)"
#Filename="herrevad"
#Type=App

import os
from Library import protobuf
import base64
import binascii

def wcdma(data):
    celltype = "WCDMA"
    #print(data)
    mcc=""
    cid=""
    lac=""
    mnc=""
    if 1 and 2 in data:
        mcc = data[1][0].decode()
        mnc = data[2][0].decode()
    if 3 and 4 in data:
        lac = str(data[3][0])
        cid = str(data[4][0])
    if cid=="18446744073709551615": cid = "-1"
    #res = ("[WCDMA] MCC: " + mcc + " MNC: " + mnc + " LAC: " + lac + " CID: " + cid)
    #print(res)
    return [celltype, mcc, mnc, lac, cid]

def lte(data):
    celltype = "LTE"
    mcc=""
    mnc=""
    tac=""
    ci=""
    if 1 and 2 in data:
        mcc = data[1][0].decode()
        mnc = data[2][0].decode()
    if 3 and 4 in data:
        tac = str(data[3][0])
        ci = str(data[4][0])
    if ci=="18446744073709551615": ci = "-1"
    #res = ("[LTE] MCC: " + mcc + " MNC: " + mnc + " TAC: " + tac + " CI: " + ci)
    #print(res)
    return [celltype, mcc, mnc, tac, ci]

def gsm(data):
    celltype = "GSM"
    mcc=""
    cid=""
    lac=""
    mnc=""
    if 1 and 2 in data:
        mcc = data[1][0].decode()
        mnc = data[2][0].decode()
    if 3 and 4 in data:
        lac = str(data[3][0])
        cid = str(data[4][0])
    if cid=="18446744073709551615": cid = "-1"
    #res = ("[GSM] MCC: " + mcc + " MNC: " + mnc + " LAC: " + lac + " CID: " + cid)
    #print (res)
    return [celltype,mcc,mnc,lac,cid]

def providerinfo(data):
    celltype = "ProviderInfo"
    mcc=""
    mnc=""
    provider=""
    if (len(data)==2):
        mcc = data[1][0].decode()
        mnc = data[2][0].decode()
        return [mcc, mnc]
    if (len(data)>2):
        provider = data[3][0].decode()
        return [mcc, mnc, provider]
    #res = ("[ProviderInfo] MCC: " + mcc + " MNC: " + mnc + " Provider: " + provider)
    #print(res)
    return ["", "", "Error"]
    

def networkinfo(data):
    res=""
    if 1 in data:
        for item in data[1]:
            buf1 = protobuf.protobuf(item).readAllFields()
            if 2 in buf1:
                for item1 in buf1[2]:
                    buf12 = protobuf.protobuf(item1).readAllFields()
                    res+=networkinfo(buf12)
    if 2 in data:  # GSM
        for item in data[2]:
            buf122 = protobuf.protobuf(item).readAllFields()
            location = gsm(buf122)
            res += ("["+location[0]+"] MCC: " + location[1] + " MNC: " + location[2] + " LAC: " + location[3] + " CID: " + location[4]+";\n")
            res += ctx.getlocationcell(location[1],location[2],location[3],location[4])+"\n"
    if 3 in data:  # LTE
        for item in data[3]:
            buf123 = protobuf.protobuf(item).readAllFields()
            location = lte(buf123)
            res += ("["+location[0]+"] MCC: " + location[1] + " MNC: " + location[2] + " TAC: " + location[3] + " CI: " + location[4]+";\n")
            res += ctx.getlocationcell(location[1],location[2],location[3],location[4])+"\n"
    if 4 in data:  # WCDMA
        for item in data[4]:
            buf124 = protobuf.protobuf(item).readAllFields()
            location = wcdma(buf124)
            res += ("["+location[0]+"] MCC: " + location[1] + " MNC: " + location[2] + " LAC: " + location[3] + " CID: " + location[4]+";\n")
            res += ctx.getlocationcell(location[1],location[2],location[3],location[4])+"\n"
    return res

def celldecode(data):
    celldata = protobuf.protobuf(data).readAllFields()
    celltype = "None"
    res = ""
    #print(celldata)
    if (1 in celldata) or (2 in celldata) or (3 in celldata) or (4 in celldata):  # Generic network
        res+=networkinfo(celldata)
    if 8 in celldata:
        for item in celldata[8]:
            if (len(item)>0):
                buf8 = protobuf.protobuf(item).readAllFields()
                provider = providerinfo(buf8)
                if (len(provider))==3:
                    res+=("[ProviderInfo] MCC: " + provider[0] + " MNC: " + provider[1] + " Provider: " + provider[2]+";\n")
                elif (len(provider))==2:
                    res+=("[ProviderInfo] MCC: " + provider[0] + " MNC: " + provider[1]+";\n")
    if 5 in celldata:
        buf5 = celldata[5][0]  # Value 5 ?
    if 10 in celldata:
        buf5 = celldata[10][0]  # Value 5 ?
    if 11 in celldata:
        for item in celldata[11]:
            if (len(item)>0):
                buf11 = protobuf.protobuf(item).readAllFields()
                if (len(buf11)>0):
                    provider = providerinfo(buf11)
            if (len(provider))==3:
                res+=("[ProviderInfo] MCC: " + provider[0] + " MNC: " + provider[1] + " Provider: " + provider[2]+";\n")
            elif (len(provider))==2:
                res+=("[ProviderInfo] MCC: " + provider[0] + " MNC: " + provider[1]+";\n")
    if 12 in celldata:
        for item in celldata[12]:
            if (len(item)>0):
                buf12 = protobuf.protobuf(item).readAllFields()
                if 2 in buf12: #WCDMA
                    for item2 in buf12[2]:
                        if (len(item2)>0):
                            buf12_2 = protobuf.protobuf(item2).readAllFields()
                            location = wcdma(buf12_2)
                            res += ("["+location[0]+"] MCC: " + location[1] + " MNC: " + location[2] + " LAC: " + location[3] + " CID: " + location[4]+";\n")
                            res += ctx.getlocationcell(location[1],location[2],location[3],location[4])+";\n"
    if 13 in celldata:
        for item in celldata[13]:
            if (len(item)>0):
                buf13 = item.decode()  # ProviderMCCMNC and some value as string
                res += buf13+"\n"
    return res
    

def convertdata(db):
    conn=ctx.sqlite_run_cmd(db,"select rowid, package, network_type, ssid, bssid, cellid, timestamp_millis, latency_micros, bytes_uploaded, duration_millis, measurement_type, throughput_bps from local_reports;")
    if (conn==-1):
         print ("Error: "+ctx.sqlite_last_error(db))
         return
    rows=ctx.sqlite_get_data_size(conn)[0]
    print("Running herrevad conversion")
    oldpos=0
    for i in range(0,rows):
        newpos=int(i/rows*100)
        if (oldpos<newpos):
            oldpos=newpos
            ctx.gui_setMainProgressBar(oldpos)
        id=ctx.sqlite_get_data(conn,i,0)
        package=ctx.sqlite_get_data(conn,i,1)
        network_type=ctx.sqlite_get_data(conn,i,2)
        ssid=ctx.sqlite_get_data(conn,i,3)
        bssid=ctx.sqlite_get_data(conn,i,4)
        cellid=ctx.sqlite_get_data(conn,i,5)
        timestamp_millis=ctx.sqlite_get_data(conn,i,6)
        latency_micros=ctx.sqlite_get_data(conn,i,7)
        bytes_uploaded=ctx.sqlite_get_data(conn,i,8)
        duration_millis=ctx.sqlite_get_data(conn,i,9)
        measurement_type=ctx.sqlite_get_data(conn,i,10)
        throughput_bps=ctx.sqlite_get_data(conn,i,11)
        if cellid!="":
            #print(cellid)
            try:
                #print("Cell:"+str(id))
                data=ctx.base64todata(cellid,1).data()
                info=celldecode(data)
            except:
                info="Error on rowid: "+str(id)
        else:
            #print("WiFi:"+str(id))
            info="WiFi - SSID: "+ssid+" BSSID: "+bssid
        ctx.gui_set_data(i,0,id)
        ctx.gui_set_data(i,1,package)
        ctx.gui_set_data(i,2,network_type)
        ctx.gui_set_data(i,3,info)
        ctx.gui_set_data(i,4,timestamp_millis)
        ctx.gui_set_data(i,5,latency_micros)
        ctx.gui_set_data(i,6,bytes_uploaded)
        ctx.gui_set_data(i,7,duration_millis)
        ctx.gui_set_data(i,8,measurement_type)
        ctx.gui_set_data(i,9,throughput_bps)

    ctx.sqlite_cmd_close(conn)

def main():
    headers=["rowid (int)","package (QString)","network_type (int)","info (QString)","timestamp_millis (QString)","latency_micros (int)", "bytes_uploaded (int)", "duration_millis (int)", "measurement_type (int)", "throughput_bps (int)"]
    ctx.gui_set_headers(headers)
    ctx.gui_setMainLabel("Google Herrevad: Parsing Locations");
    ctx.gui_setMainProgressBar(0)
    db=ctx.sqlite_open("gui",True)
    convertdata(db)
    ctx.gui_update()
    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    ctx.sqlite_close(db)
    return "Finished running plugin."