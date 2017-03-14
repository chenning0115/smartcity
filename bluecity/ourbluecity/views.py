from django.shortcuts import render

# Create your views here.

import datetime
from django.http import HttpResponse
from ourbluecity.tools.createGrid import *
from django.http import HttpResponse
import ourbluecity.tools.datamanager as dm
from ourbluecity.tools.datamanager import fac_dict
import ourbluecity.tools.TimeseriseSerivce as ts
import json
from ourbluecity.tools.stateTranMat import getTranProbStr
from urllib import  request as urlreq

def gethome(request):
    return render(request,'homepage.html')

def quaryaqi(request):
    row = int(request.GET["row"])
    col = int(request.GET["col"])
    return render(request, 'QuaryAQI.html', {'rownum': row, 'colnum': col})


def getFactorGrid(request):
    day = int(request.GET["day"])
    fac = request.GET["factor"]
    return HttpResponse(getGridStr(array=fac_dict[fac][day-1,:,:]))



def getBlockFactor(request):
    '''
    获得第date天第row行第col列格子的aqi
    :param request:
    :return:
    '''
    day = int(request.GET["date"])
    row = int(request.GET["row"])
    col = int(request.GET["col"])
    fac = request.GET["factor"]
    return HttpResponse(fac_dict[fac][day-1, row, col])

def getTranProData(request):
    index_row = int(request.GET['row'])
    index_col = int(request.GET['col'])
    d = fac_dict["aqi_fin"][:, index_row, index_col]
    s = getTranProbStr(d)
    return HttpResponse(s)






# #########################################
#chenning 新增
def analyse_time(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    return render(request, 'analyse_time.html', {'rownum': row, 'colnum': col})
def analyse_factor(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    return render(request, 'analyse_factor.html', {'rownum': row, 'colnum': col})
def decisionsupport(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    return render(request, 'decisionsupport.html', {'rownum': row, 'colnum': col})

def yearline(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    content = ts.yearlinedata(row,col)
    return HttpResponse(content)
def bestpath(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    return render(request, 'bestpath.html', {'rownum': row, 'colnum': col})

def yearpie(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    content = ts.yearpiedata(row,col)
    return HttpResponse(content)
# #########################################

def analysis_temporaldensity(request):
    return render(request, "analysis_temporaldensity.html")

def temporaldensity(request):
    row = request.GET['row']
    col = request.GET['col']
    hm = ts.TimeHeatmap()
    data = hm.getheatmapdata(int(row),int(col))
    dict = {'rowstr':hm.rowstr,'colstr':hm.colstr,'data':data}
    content = json.dumps(dict)
    return HttpResponse(content)

def analysis_aqihistory(request):
    return render(request, "analysis_aqihistory.html")

def aqihistory(request):
    row = request.GET['row']
    col = request.GET['col']
    data = dm.getaqidata(int(row),int(col))
    content = json.dumps({'year':dm.startyear, 'month':dm.startmonth, 'day':dm.startdate, 'len':len(data),'data':data})
    return HttpResponse(content)


def analysis_dashboard(request):
    return render(request, "analysis_dashboard.html")

def dashboard(request):
    row = request.GET['row']
    col = request.GET['col']
    d = fac_dict["aqi_fin"][:, row, col]
    dicsum = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(d.shape[0]):
        dicsum[int(d[i])] += 1
    r = int((dicsum[1]+dicsum[2]+dicsum[3])/d.shape[0]*100)
    return HttpResponse(r)


def analysis_duidietu1(request):
    return render(request, "analysis_duidietu1.html")

from ourbluecity.tools.duidietu1calc import duidietu1_calc
def duidietu1(request):
    row = request.GET['row']
    col = request.GET['col']
    d = fac_dict["aqi_fin"][:, row, col]
    r = json.dumps(duidietu1_calc(d))
    return HttpResponse(r)

def realtimefineprediction(request):
    row = int(request.GET["row"])
    col = int(request.GET["col"])
    return render(request,'realtimefineprediction.html', {'rownum': row, 'colnum': col})

def analysis_parallel1(request):
    return render(request, "analysis_parallel1.html")

from ourbluecity.tools.parallel1calc import parallel1_calc
def parallel1(request):
    row = request.GET['row']
    col = request.GET['col']
    d = parallel1_calc(fac_dict, row, col)
    r = json.dumps(d)
    return HttpResponse(r)

def analysis_greycorr(request):
    return render(request, "analysis_greycorr.html")

from ourbluecity.tools.causeService import getgrecorrbyrow_col
def greycorr(request):
    row = int(request.GET['row'])
    col = int(request.GET['col'])
    d = getgrecorrbyrow_col(row, col)
    vals = list(d.values())
    return HttpResponse(json.dumps({"vals":vals}))

