# -*- coding=utf8 -*-
from sklearn.datasets import load_iris
#from sklearn.model_selection.train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import  KNeighborsClassifier
iris = load_iris()
X = iris.data
y = iris.target

from sklearn.cross_validation import cross_val_score
knn = KNeighborsClassifier(n_neighbors=2)
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print(scores)
