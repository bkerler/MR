import math

def frompointtolatlng(x, y):
    lat_deg = (2 * math.atan(math.exp((y - 128) / -(256 / (2 * math.pi)))) - math.pi / 2) / (math.pi / 180)
    lon_deg = (x - 128) / (256 / 360)
    return (lat_deg, lon_deg)


def necoord(xtile, ytile, zoom):
    n = 2.0 ** zoom
    s = 256 / n
    x = (xtile * s) + s
    y = ytile * s
    return frompointtolatlng(x, y)


def swcoord(xtile, ytile, zoom):
    n = 2.0 ** zoom
    s = 256 / n
    x = xtile * s
    y = (ytile * s) + s
    return frompointtolatlng(x, y)

def normalize(ne, sw):
    if (ne[0] < sw[0]):
        lat = ne[0] + ((sw[0] - ne[0]) / 2)
    else:
        lat = sw[0] + ((ne[0] - sw[0]) / 2)
    if (ne[1] < sw[1]):
        lon = ne[1] + ((sw[1] - ne[1]) / 2)
    else:
        lon = sw[1] + ((ne[1] - sw[1]) / 2)
    return (lat, lon)


def getcoord(x,y,z):
    ne = necoord(x, y, z)
    sw = swcoord(x, y, z)
    coord = normalize(ne, sw)
    latstr = ('%.6f' % coord[0])
    lonstr = ('%.6f' % coord[1])
    return [latstr,lonstr]