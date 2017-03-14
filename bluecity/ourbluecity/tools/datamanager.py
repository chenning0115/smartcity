
import numpy as np
import pandas as pd
import sys
import  json

datapath = r'/Users/chenning/Desktop/data/smc_data_1.csv'

grid_rownum = 35
grid_colnum = 39

startdate = '20140101'
enddate = '20151230'
startyear = 2014
startmonth = 1
startdate = 1
startweek = 3
columnnames = ['time', 'location', 'prec', 'pres', 'wind', 'temp',
       'SHum', 'Irad', 'SRad', 'aqi', 'poi', 'road', 'lucc', 'aqi_pre',
       'aqi_fin']

df = pd.read_csv(datapath)


def getaqidata(row,col):
    '''
    获取预测后给定格子所有时间的aqi级别信息,返回一个List
    :return: list
    '''
    gridnumber = (col-1)*35+row
    df_spe_grid = df[df['location']==gridnumber]
    df_aqi = df_spe_grid['aqi_fin']
    # print(df_aqi)
    return df_aqi.values.tolist()

def get3darray(array):
    timetemp = np.zeros([730 , 35, 39])
    locationtemp = np.zeros([730 , 35, 39])
    prectemp = np.zeros([730 , 35, 39])
    prestemp = np.zeros([730 , 35, 39])
    windtemp = np.zeros([730 , 35, 39])
    temptemp = np.zeros([730 , 35, 39])
    sHumtemp = np.zeros([730 , 35, 39])
    Iradtemp = np.zeros([730 , 35, 39])
    SRadtemp = np.zeros([730 , 35, 39])
    poitemp = np.zeros([730 , 35, 39])
    roadtemp = np.zeros([730 , 35, 39])
    lucctemp = np.zeros([730 , 35, 39])
    aqi_pretemp = np.zeros([730 , 35, 39])
    aqi_fintemp = np.zeros([730 , 35, 39])

    for line in range(array.shape[0]):
        temp = int(array[line, 2]) - 1
        col = temp // 35
        row = temp % 35
        timetemp[int(array[line, 1])-1, row,col ] = array[line, 1]
        locationtemp[int(array[line, 1])-1, row,col ] = array[line, 2]
        prectemp[int(array[line, 1])-1, row,col ] = array[line, 3]
        prestemp[int(array[line, 1])-1, row,col ] = array[line, 4]
        windtemp[int(array[line, 1])-1, row,col ] = array[line, 5]
        temptemp[int(array[line, 1])-1, row,col ] = array[line, 6]
        sHumtemp[int(array[line, 1])-1, row,col ] = array[line, 7]
        Iradtemp[int(array[line, 1])-1, row,col ] = array[line, 8]
        SRadtemp[int(array[line, 1])-1, row,col ] = array[line, 9]
        poitemp[int(array[line, 1])-1, row,col ] = array[line, 11]
        roadtemp[int(array[line, 1])-1, row,col ] = array[line, 12]
        lucctemp[int(array[line, 1])-1, row,col ] = array[line, 13]
        aqi_pretemp[int(array[line, 1])-1, row,col ] = array[line, 14]
        aqi_fintemp[int(array[line, 1])-1, row,col ] = array[line, 15]

    dictfac = {}
    dictfac["time"] = timetemp
    dictfac["location"] = locationtemp
    dictfac["prec"] = prectemp
    dictfac["pres"] = prestemp
    dictfac["wind"] = windtemp
    dictfac["temp"] = temptemp
    dictfac["sHum"] = sHumtemp
    dictfac["Irad"] = Iradtemp
    dictfac["SRad"] = SRadtemp
    dictfac["poi"] = poitemp
    dictfac["road"] = roadtemp
    dictfac["lucc"] = lucctemp
    dictfac["aqi_pre"] = aqi_pretemp
    dictfac["aqi_fin"] = aqi_fintemp
    return dictfac


arraycsv = df.values
fac_dict = get3darray(arraycsv)

