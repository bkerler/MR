#Pluginname="Google Maps Data_Tiles (Android,FS)"
#Category="Extraction"
#(c) B.Kerler 2017
#Type=FS

from os import walk
import os
import struct
import math
import tempfile

def frompointtolatlng(x,y):
    lat_deg = (2 * math.atan(math.exp((y - 128) / -(256 / (2 * math.pi)))) - math.pi / 2) / (math.pi / 180)
    lon_deg = (x - 128) / (256 / 360)
    return (lat_deg, lon_deg)

def necoord(xtile, ytile, zoom):
    n = 2.0 ** zoom
    s = 256 / n
    x = (xtile*s)+s
    y = ytile*s
    return frompointtolatlng(x,y)

def swcoord(xtile, ytile, zoom):
    n = 2.0 ** zoom
    s = 256 / n
    x = xtile*s
    y = (ytile*s)+s
    return frompointtolatlng(x,y)
    
def normalize(ne,sw):
    if (ne[0]<sw[0]):
        lat=ne[0]+((sw[0]-ne[0])/2)
    else:
        lat=sw[0]+((ne[0]-sw[0])/2)
    if (ne[1]<sw[1]):
        lon=ne[1]+((sw[1]-ne[1])/2)
    else:
        lon=sw[1]+((ne[1]-sw[1])/2)
    return (lat,lon)

def findtiles():
    files=[]
    allfiles=ctx.fs_getselected()
    m=0
    if len(allfiles)==0:
        allfiles=ctx.fs_filelist()
    filecount=len(allfiles)
    for file in allfiles:
        if ("DATA_Tiles_" in file):
            files.append(file)
    return files

def main():
    ctx.gui_setMainProgressBar(0)
    tiles=findtiles()
    if (len(tiles)>0):
        extracttodir=ctx.gui_askSaveDir("Please select directory to extract the files to")
        if (extracttodir==""):
            error="Error: Can't extract files without directory"
            ctx.setMainLabel("Status: Idle.")
            return error
        ctx.gui_setMainLabel("Status: Extracting files to: "+extracttodir)
        i=0
        with open(extracttodir+"/coordinates.csv","wb") as cw:
            cw.write(b"Filename;Latitude;Longitude\n")
            for item in tiles:
                ctx.gui_setMainProgressBar(int(i/len(tiles)))
                ctx.fs_file_extract(item,extracttodir+"/tmp")
                i+=1
                with open(extracttodir+"/tmp","rb") as rb:
                    itemcount = struct.unpack("B",rb.read(1))[0]
                    for counter in range(0,itemcount):
                        data=struct.unpack(">B I I B H",rb.read(0xC))
                        version=data[0] #Version should be 2
                        x=data[1]
                        y=data[2]
                        z=data[3]-1 #Zoom level
                        ne=necoord(x,y,z)
                        sw=swcoord(x,y,z)
                        coord=normalize(ne,sw)
                        latstr=('%.6f' % coord[0])
                        lonstr=('%.6f' % coord[1])
                        cw.write(bytearray(item+";"+latstr+";"+lonstr+"\n","utf-8"))
                        lendat=data[4]
                        filename=extracttodir+"/img"+item[item.rfind("/")+1:]+"_"+str(counter)+"_lat_"+latstr+"_lon_"+lonstr+"_.png"
                        with open(filename,"wb") as wb:
                            data=rb.read(lendat)
                            wb.write(data)
                os.remove(extracttodir+"/tmp")

    ctx.gui_setMainLabel("Status: Idle.")
    ctx.gui_setMainProgressBar(0)
    return "Finished running plugin."