# -*- coding=utf8 -*-
import numpy as np
import pylab as pl
from sklearn import svm

# we create 40 separable points
np.random.seed(0) # 下次也不变
# numpy.r_是将一系列的序列合并到一个数组中，调用是要用中括号[],而不是()。
'''
np.r_[[1,2,3],[4,5,6]]
Out[21]: array([1, 2, 3, 4, 5, 6])
'''
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]  # []
# X = [np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20

# fit the mddel
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

# get the separating hyperplane
w = clf.coef_[0] # Coefficient ,系数
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
bias = clf.intercept_[0]
yy = a * xx - bias / w[1] # intercept_截距

# plot the parallels to the separating hyperplane that pass through the support vectors
# 第一个向量
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])

# 最后一个向量
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

print('w: ', w)
print('a: ', a)
print('support_vectors_: ', clf.support_vectors_)
print('clf.coef_ ', clf.coef_)

pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--')
pl.plot(xx, yy_up, 'k--')
# 标记一下，加个圈
pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80, facecolors='none')
# 画所有的点
pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

pl.axis('tight')
pl.show()
