# -*- coding=utf8 -*-
#from sklearn.learning_curve import learning_curve
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn import svm
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

clf = svm.SVC #
iris = datasets.load_iris()
X,y = iris.data, iris.target
clf.fit(X, y)

#method 1:pickle
import pickle
with open('save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)

# restore
with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
    print(clf2.predict(X[0:1]))


#joblib

