# -*- coding=utf8 -*-


import numpy as np
from sklearn.cluster import KMeans


def load_data(filePath):
    fr = open(filePath,'r+', encoding='utf-8')  #r+:读写方式打开一个文本文件
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines: #一行一个数据
        items = line.strip().split("\t")
        retCityName.append(items[0]) #地区名称
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData,retCityName


if __name__ is '__main__':
    data, cityName = load_data('city.txt')
    print(cityName)
    print(data)

    km = KMeans(n_clusters=3)
    label = km.fit_predict(data) #2,0,1,2,2 ... ...
    expenses = np.sum(km.cluster_centers_, axis=1)
    print(expenses)
    CityCluster = [[], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])

    for i in range(len(CityCluster)):
        print("Expense:%.2f" % expenses[i])
        print(CityCluster[i])