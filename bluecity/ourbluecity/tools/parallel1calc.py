
def parallel1_calc(fac, row, col):
    prec = fac["prec"][:, row, col]
    pres = fac["pres"][:, row, col]
    wind = fac["wind"][:, row, col]
    temp = fac["temp"][:, row, col]
    SHum = fac["sHum"][:, row, col]
    Irad = fac["Irad"][:, row, col]
    SRad = fac["SRad"][:, row, col]
    aqi_fin = fac["aqi_fin"][:, row, col]
    n = aqi_fin.shape[0]
    lst = []
    for i in range(n):
        lst.append([prec[i], pres[i], wind[i], temp[i], SHum[i], Irad[i], SRad[i], aqi_fin[i]])
    return {"dataBJ":lst}
