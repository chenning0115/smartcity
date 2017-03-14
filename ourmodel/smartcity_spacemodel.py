import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.decomposition import PCA

# 从原始数据中抽取出时间相关特征以及空气质量级别的可训练数据列
def getTimeTrainedDatabyTime(df):
	# df_train_time = df[(df.time==time) & (df.aqi>0)]
	df_train = df[(df.aqi>0) & (df.prec) & (df.pres) & (df.temp) & (df.wind) & (df.SHum) & (df.Irad) & (df.SRad)]
	# df_train.to_csv('~/data/smartcity/smc_std_traindata_jicha.csv')
	df_x_train = df_train[['prec', 'pres', 'wind', 'temp', 'SHum', 'Irad','SRad']]
	df_y_train = df_train['aqi'].astype('int32')
	return (df_x_train.values,df_y_train.values)


# 使用PCA
def getTimeDataUsingPCA(df):
	pca = PCA(n_components=2)
	df = df[['prec', 'pres', 'wind', 'temp', 'SHum', 'Irad','SRad','aqi']]
	df_train= df[(df.aqi>0) & (df.prec) & (df.pres) & (df.temp) & (df.wind) & (df.SHum) & (df.Irad) & (df.SRad)]
	# df_train.to_csv('~/data/smartcity/smc_std_traindata_jicha.csv')
	df_x_train = df_train[['prec', 'pres', 'wind', 'temp', 'SHum', 'Irad','SRad']]
	df_y_train = df_train['aqi'].astype('int32')
	pca = pca.fit(df_x_train)
	print(pca)
	df_x_train_pca = pca.transform(df_x_train)
	return (df_x_train_pca,df_y_train.values)
# 训练模型同时对给定值进行插值
def TimePredict(df):
	# traindata = getTimeTrainedDatabyTime(df)
	traindata = getTimeDataUsingPCA(df)
	print(traindata)
	x = traindata[0]
	y = traindata[1]
	# gnb = GaussianNB()
	# timemodel = svm.SVC(gamma=10)
	timemodel = RandomForestClassifier(n_estimators=100)
	# timemodel = ExtraTreesClassifier(n_estimators=300, max_depth=None,min_samples_split=1, random_state=1)
	# y_pre = timemodel.fit(x,y).predict(x)
	# count = (y_pre!=y).sum()
	# # for i in range(len(y_pre)):
	# # 	print(y_pre[i],y[test][i])
	# print(y_pre.size,count,1-(count/y_pre.size))
	# # print(traindata[0].size,traindata[1].size)
	# gnb_pre = gnb.fit(traindata[0],traindata[1])
	# y_pre = gnb_pre.predict(traindata[0])
	# print(y_pre.size,',',(y_pre!=traindata[1]).sum())
	from sklearn import cross_validation
	kfold = cross_validation.KFold(len(x), n_folds=10)
	for train,test in kfold:
		y_pre = timemodel.fit(x[train],y[train]).predict(x[test])
		count = (y_pre!=y[test]).sum()
		# for i in range(len(y_pre)):
		# 	print(y_pre[i],y[test][i])
		print(y_pre.size,count,1-(count/y_pre.size))
		# print(timemodel.fit(x[train], y[train]).score(x[test], y[test]))

df = pd.read_csv('~/data/smartcity/smc_data_1.csv')
# print(df)
# for i in range(50):
# 	spacePredict(df,i+1)
TimePredict(df)