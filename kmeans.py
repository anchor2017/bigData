#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:38:46 2019

@author: anchor
"""

#文本编辑距离
import Levenshtein
a= Levenshtein.distance('abhg','bgj')
print(a)

from sklearn.cluster import KMeans  
  
X = [[0.262, 4],  
     [0.192, 4],  
     [4.052, 1.98],  
     [1, 19.59],  
     [2, 3.5],  
     [0.78, 10.6],  
     [2, 10.5],  
     [2.038, 7.38],  
     [0.574, 11.6],  
     [5, 1.06],  
     [4.43, 4.78],  
     [0.514, 43],  
     [0.592, 31],  
     [1, 16.2],  
     [1, 7.39],  
     [1, 95.9],  
     [1, 23.29],  
     [1, 12.8],  
     [1.338, 2.6],  
     [0.46, 19]     
    ]  
 
# Kmeans聚类
clf = KMeans(n_clusters=4)  
y_pred = clf.fit_predict(X)  
print(clf)   
print(y_pred)  
 
import matplotlib.pyplot as plt  
  

x = [n[0] for n in X]  
y = [n[1] for n in X]  

# 可视化操作
plt.scatter(x, y, c=y_pred, marker='x')   
plt.title("Kmeans-sales Data")   
plt.xlabel("object")  
plt.ylabel("prices")  
plt.legend(["Rank"])   
plt.show()  
