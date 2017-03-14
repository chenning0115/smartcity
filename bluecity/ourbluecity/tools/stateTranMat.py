import numpy as np
import json


def getTranMat(lst):
    size = lst.shape[0]
    r_mat = np.zeros([6, 6])
    for i in range(size-1):
        x, y = int(lst[i] - 1), int(lst[i+1] - 1)
        r_mat[x, y] += 1
    return r_mat

def getTranProb(lst):
    s_mat = getTranMat(lst)
    b_mat = np.tile(s_mat.sum(1).reshape([6,1]),[1,6])
    return s_mat / b_mat

def getTranProbStr(lst):
    mat = getTranProb(lst).round(2)
    rowstr = [str(i) for i in range(7)]
    colstr = [str(i) for i in range(7)]
    data = [[i, j, mat[i-1, j-1]] for i in range(1, 7) for j in range(1, 7)]
    return json.dumps({"rowstr":rowstr, "colstr":colstr, "data":data})
# import oursmartcity.tools.datamanager as dm
# a = getTranMat(dm.fac_dict["aqi_fin"][:,3,4])
# print(a)
# b = getTranProb(dm.fac_dict["aqi_fin"][:,3,4])
# print(b.round(2))
