import datetime
from datetime import timezone

def getdate(date):
    ts=datetime.datetime.utcfromtimestamp(int(date))
    return ts.strftime('%d.%m.%Y %H:%M:%S')
    
def packDate(d,M,y,h,m,s,ms):
    h=datetime.datetime(y,M,d,h,m,s,ms)
    t=h.replace(tzinfo=timezone.utc).timestamp()
    return int(t)