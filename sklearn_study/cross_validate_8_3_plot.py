# -*- coding=utf8 -*-
from sklearn.datasets import load_iris
#from sklearn.model_selection.train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import  KNeighborsClassifier
iris = load_iris()
X = iris.data
y = iris.target

from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt
k_range = range(1, 31)
k_scores = []
k_loss = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')#for classifictaiton
    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')#for regression
    k_scores.append(scores.mean())
    k_loss.append(loss.mean())
    #print(scores)

#plt.plot(k_range, k_scores)
plt.plot(k_range, k_loss)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()