import json
import ourbluecity.tools.datamanager as dm
import datetime

class TimeHeatmap:
    def __init__(self):
        self.colstr=[ '周一', '周二', '周三', '周四', '周五', '周六','周日']
        self.rowstr=[str(i)+'月' for i in range(1,13)]+[str(i)+'p' for i in range(1,13)]
    def getheatmapdata(self,loc_row,loc_col):

        data = dm.getaqidata(loc_row,loc_col)
        print(len(data))
        startdate = datetime.date(2004,1,1)
        # deltday = datetime.timedelt(days=1)
        maxtrix = [([0]*12) for i in range(7)]
        maxtrix_count = [([0]*12) for i in range(7)]
        for i in range(len(data)):
            deltday = datetime.timedelta(days=i)
            tempdate = startdate+deltday
            tempmonth = tempdate.month-1
            tempweek = tempdate.weekday()
            maxtrix[tempweek][tempmonth]+=data[i]
            maxtrix_count[tempweek][tempmonth]+=1
        resultlist = []
        for i in range(7):
            for j in range(12):
                val = int(round(maxtrix[i][j]/maxtrix_count[i][j]))
                resultlist.append([i,j,val])
        return resultlist


def yearlinedata(row,col):
    datalist = dm.getaqidata(row,col)
    l1 = datalist[0:364]
    l2 = datalist[365:]
    r = [[0]*2 for i in range(6)]
    for i in range(len(l1)):
        r[int(l1[i])-1][0]+=1
    for i in range(len(l2)):
        r[int(l2[i])-1][1]+=1
    return json.dumps(r)
def yearpiedata(row,col):
    datalist = dm.getaqidata(row, col)
    r = [0]*6
    ll = len(datalist)
    for i in range(ll):
        r[int(datalist[i])-1]+=1
    return json.dumps(r)