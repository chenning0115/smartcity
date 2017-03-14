import numpy as np
import pandas as pd
import ourbluecity.tools.datamanager as dm
from sklearn import  linear_model

colnames_x = ['prec', 'pres', 'wind', 'temp',
       'SHum', 'Irad', 'SRad', 'poi', 'road', 'lucc']
colname_y = 'aqi_fin'

maxfactorpath = r'/Users/chenning/Desktop/data/maxfactor.csv'
df_maxfactor = pd.read_csv(maxfactorpath,dtype='a')

# y为参考列
def grecorr(x,y):
    p = 0.5
    print(x.shape,y.shape)
    y_std = y/y.iloc[0]
    x_std = pd.DataFrame()
    list_xnames = x.columns
    for i in range(len(list_xnames)):
        tempname = list_xnames[i]
        x_std[tempname] = x[tempname]/x[tempname].iloc[0]
    x_matrix = pd.DataFrame()
    minval = 999999999999999
    maxval = -99999999999999
    for i in range(len(list_xnames)):
        tempname = list_xnames[i]
        x_matrix[tempname] = abs(x_std[tempname]-y_std)
        tempmin = x_matrix[tempname].min()
        tempmax = x_matrix[tempname].max()
        if tempmin < minval: minval = tempmin
        if tempmax > maxval: maxval = tempmax

    x_matrix = (minval + p*maxval)/(x_matrix+p*maxval)

    resultdict = {}
    for i in range(len(list_xnames)):
        resultdict[list_xnames[i]] = x_matrix[list_xnames[i]].mean()
    return resultdict

def getgrecorrbyrow_col(row,col):
    gridnumber = (col - 1) * 35 + row
    df_filter = dm.df[dm.df['location'] == gridnumber]
    df_filter = df_filter[(df_filter.prec != None) & (df_filter.pres != None) & (df_filter.temp != None) & (df_filter.wind != None) & (df_filter.SHum != None) & (df_filter.Irad != None) & (df_filter.SRad != None) ]
    return grecorr(df_filter[colnames_x],df_filter[colname_y])

def saveallparcorr(path):
    file = open(path,'w')
    tempstr = ''
    for i in range(len(colnames_x)):
        tempstr = tempstr+colnames_x[i]+','
    file.write(tempstr+'\r\n')
    for col in range(dm.grid_colnum):
        for row in range(dm.grid_rownum):
            print(row,col)
            corrdict = getgrecorrbyrow_col(row + 1, col + 1)
            tempstr = ''
            for key in corrdict:
                tempstr=tempstr+str(corrdict[key])+','
            tempstr+='\r\n'
            file.write(tempstr)
    file.flush()
    file.close()

def getallparcorr():
    resultlist = []
    maxindex = 0
    maxval = str(0)
    for i in range(df_maxfactor.index.size):
        for j in range(df_maxfactor.columns.size-2):
            val = str(df_maxfactor.iloc[i,j])
            if val > maxval:
                maxval = val
                maxindex = j
        resultlist.append(colnames_x[maxindex])
    print(resultlist)
    return np.array(resultlist).reshape((dm.grid_rownum,dm.grid_colnum))

def getradardata(row,col):
    index = (col - 1) * 35 + row - 1
    l1 = df_maxfactor.iloc[index,:]
    l1.astype('float64')
    



