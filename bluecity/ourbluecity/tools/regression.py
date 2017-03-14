import numpy as np

def calB_range(data, start_time, end_time, block_x_start, block_x_end, block_y_start, block_y_end):
    r_mat = np.zeros([block_x_end - block_x_start + 1, block_y_end - block_y_start + 1])
    for i in range(block_x_end - block_x_start + 1):
        for j in range(block_y_end - block_y_start + 1):
            r_mat[i, j] = calB_time(data, start_time, end_time, block_x_start + i, block_y_start + j)
    return r_mat

def calB_time(data, start_time, end_time, block_x, block_y):
    return calB(np.array(range(start_time, end_time + 1)), data[start_time - 1:end_time, block_x, block_y])

def calB(xs, ys):
    x_ = xs.mean()
    y_ = ys.mean()
    lxx = ((xs - x_) * (xs - x_)).sum()
    lxy = ((xs - x_) * (ys - y_)).sum()
    return lxy / lxx

def classify(nparray):
    array = np.array(range(nparray.shape[0]*nparray.shape[1])).reshape(nparray.shape)
    for i in range(nparray.shape[0]):
        for j in range(nparray.shape[1]):
            if nparray[i, j] <= -1:
                array[i, j] = 1
            elif nparray[i, j] < -0.5:
                array[i, j] = 2
            elif nparray[i, j] <= 0.5:
                array[i, j] = 3
            elif nparray[i, j] < 1:
                array[i, j] = 4
            else:
                array[i, j] = 5
    return array


# import oursmartcity.tools.datamanager as dm
# print("___")
# arr = dm.fac_dict["aqi_fin"]
# max, min = -100, 100
# for i in range(1, 730-10):
#     a = calB_range(arr, i, i+10, 0, 34, 0, 38)
#     t_max, t_min = a.max(), a.min()
#     max, min = t_max if t_max > max else max, t_min if t_min < min else min
#
# print(max,min)