from numpy import *

def getGridStr(startLon = 116.0975,endLon = 116.554,startLat = 39.7128,endLat = 40.123,numLon = 39,numLat = 35,array = None):
    if array == None:
        array = zeros([numLat,numLon])
    s = ''
    increLon = (endLon - startLon) / numLon
    increLat = -(endLat - startLat) / numLat
    lst = []
    for j in range(numLat):
        for i in range(numLon):
            lst.append('POLYGON(('+str(startLon+i*increLon)+" "+str(endLat+j*increLat)+','+str(startLon+(i+1)*increLon)+" "+str(endLat+j*increLat)
                    +','+str(startLon+(i+1)*increLon)+" "+str(endLat+(j+1)*increLat)+','+str(startLon+i*increLon)+" "+str(endLat+(j+1)*increLat)
                    +','+str(startLon+i*increLon)+" "+str(endLat+j*increLat)+'))'+"&"+str(array[j, i]))
    s += ';'.join(lst)
    return s