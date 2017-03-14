def duidietu1_calc(data):
    xaxis = ['2014.1','2014.2','2014.3','2014.4','2014.5','2014.6','2014.7','2014.8','2014.9','2014.10','2014.11','2014.12',
             '2015.1','2015.2','2015.3','2015.4','2015.5','2015.6','2015.7','2015.8','2015.9','2015.10','2015.11','2015.12']
    m_days = [0,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(2,len(m_days)):
        m_days[i] = m_days[i] + m_days[i-1]
    aqi = [[0 for j in range(24)] for i in range(7)]
    for i in range(len(m_days)-1):
        for j in data[m_days[i]:m_days[i+1]]:
            aqi[int(j)][i] += 1
    r = {"xaxis":xaxis,"aqi1":aqi[1],"aqi2":aqi[2],"aqi3":aqi[3],"aqi4":aqi[4],"aqi5":aqi[5],"aqi6":aqi[6]}
    return r
