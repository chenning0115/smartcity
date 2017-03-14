# 本文件用于对数据进行规整，将各个文件规整到一个文件中，从而可以进行训练 

import numpy as np
import pandas as pd

def AQI2predictedAQI(path):
	df = pd.read_csv(path)
	newaqi = df['aqi'].values.copy()
	pred_aqi = df['aqi_pre']
	for i in range(newaqi.size):
		if not newaqi[i]>0:
			newaqi[i] = pred_aqi[i]
	df['aqi_fin'] = newaqi
	df.to_csv(path)

# 处理AQI数据为级别，按照规定标准 1-6级
def AQI2Grade(src_path,des_path):
	df_AQI = pd.read_excel(src_path)
	colnum = df_AQI.columns.size
	rownum = df_AQI.index.size
	print(rownum,colnum)
	for i in range(rownum):
		for j in range(colnum):
			# print('i=',i,'j=',j)
			tempval = df_AQI.iloc[i,j]
			if not tempval: df_AQI.iloc[i,j]=NaN;continue
			if tempval<= 50:  df_AQI.iloc[i,j]=1;continue
			if tempval<= 100: df_AQI.iloc[i,j]=2;continue
			if tempval<= 150: df_AQI.iloc[i,j]=3;continue
			if tempval<= 200: df_AQI.iloc[i,j]=4;continue
			if tempval<= 300: df_AQI.iloc[i,j]=5;continue
			if tempval > 300: df_AQI.iloc[i,j]=6;continue
	df_AQI.to_csv(des_path)



def create_timelocation_indexs(path):
	num_time = 730
	num_loc = 35*39
	indexrange = range(num_time*num_loc)
	df = pd.DataFrame(index=indexrange,columns=('time','location'))
	timearray = []
	for i in range(num_time):
		timearray+=[i+1 for j in range(num_loc)]
	locarray =[]
	for i in range(num_time):
		locarray+=[j+1 for j in range(num_loc)]
	print(len(timearray),len(locarray),len(indexrange)) 
	df['time'] = timearray
	df['location'] = locarray
	df.to_csv(path)

# 符合规则的没有遗漏天数的文件
def change_timelike_data(name,old_path,df_new):
	print('readdata...')
	df_old = pd.read_excel(old_path)
	print('readdata success ...')
	old_array = df_old.values
	datanum = old_array.size
	old_array_reshape_1 = old_array.reshape((1,datanum))[0]
	
	print('des_length=',df_new.index.size,name,'size=',old_array_reshape_1.size) 
	df_new[name] = old_array_reshape_1
	print('success in ',name)




def setAQI(aqi_path,df_new):
	df_aqi = pd.read_csv(aqi_path)
	index  = df_aqi['time']
	df_aqi_new = df_aqi
	del df_aqi_new['time']
	list_aqi = [-1 for i in range(df_new.index.size)]
	rownum = df_aqi_new.index.size
	colnum = df_aqi_new.columns.size
	coltimes = 35*39
	coldata = df_aqi_new.columns
	for i in range(rownum):
		for j in range(colnum):
			temp = (index[i]-1)*coltimes+int(coldata[j])-1
			list_aqi[temp] = df_aqi_new.iloc[i,j]
		print(i,' is ok')
	df_new['aqi'] = list_aqi



def setpoiandroad(name,path,df_new):
	df1 = pd.read_excel(path)

	array = df1.values[0]
	eacharray = array.copy()
	for i in range(729):
		temparray = eacharray.copy()
		array = np.concatenate((array,temparray))
		print(i)
	print('len = ',array.size)
	df_new[name] = array


def standarlazition(df_new,list_col,despath):
	# num_time = 730
	# num_loc = 35*39
	# indexrange = range(num_time*num_loc)
	# df = pd.DataFrame(index=indexrange,columns=('time','location'))
	# df['time'] = df_new['time']
	# df['location'] = df_new['location']
	# df['aqi'] = df_new['aqi']
	for i in range(len(list_col)):
		temp = df_new[list_col[i]]
		temp_mean = temp.mean()
		temp_std = temp.std()
		df_new[list_col[i]] = (temp-temp_mean)/temp_std
	df_new.to_csv(despath)



def standarlazition_jicha(df_new,list_col,despath):
	# num_time = 730
	# num_loc = 35*39
	# indexrange = range(num_time*num_loc)
	# df = pd.DataFrame(index=indexrange,columns=('time','location'))
	# df['time'] = df_new['time']
	# df['location'] = df_new['location']
	# df['aqi'] = df_new['aqi']
	for i in range(len(list_col)):
		temp = df_new[list_col[i]]
		temp_val = temp.max()-temp.min()
		temp_min = temp.min()
		df_new[list_col[i]] = (temp-temp_min)/temp_val
	df_new.to_csv(despath)

###################################################################


 

#AQI2Grade('~/data/smartcity/AQI_C.xlsx','~/data/smartcity/AQI_G.csv')
# create_timelocation_indexs('~/data/smartcity/sm_data.csv')
# df_new = pd.read_csv('~/data/smartcity/smc_data_1.csv')
# change_timelike_data('prec','~/data/smartcity/prec_bj.xlsx',df_new)
# change_timelike_data('pres','~/data/smartcity/pres_bj.xlsx',df_new)
# change_timelike_data('wind','~/data/smartcity/wind_bj.xlsx',df_new)
# change_timelike_data('temp','~/data/smartcity/temp_bj.xlsx',df_new)
# change_timelike_data('SHum','~/data/smartcity/SHum_bj.xlsx',df_new)
# change_timelike_data('Irad','~/data/smartcity/Irad_new.xlsx',df_new)
# change_timelike_data('SRad','~/data/smartcity/SRad_bj.xlsx',df_new)
# setAQI('~/data/smartcity/AQI_new.csv',df_new)
# setpoiandroad('poi','~/data/smartcity/poi.xlsx',df_new)
# setpoiandroad('road','~/data/smartcity/road.xlsx',df_new)
# setpoiandroad('lucc','~/data/smartcity/LUCC.xlsx',df_new)
# standarlazition_jicha(df_new,['prec', 'pres', 'wind', 'temp', 'SHum', 'Irad','SRad', 'poi', 'road','lucc'],'~/data/smartcity/smc_std_data_jicha.csv')
# df_new.to_csv('~/data/smartcity/smc_data_1.csv')
AQI2predictedAQI('/Users/chenning/Desktop/data/smc_data_1.csv')
print('all is done')
