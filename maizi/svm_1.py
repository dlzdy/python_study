# -*- coding=utf8 -*-
from sklearn import svm
X = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1] #X对应的分类
clf = svm.SVC(kernel='linear')
clf.fit(X, y)

print(clf)

# get support vectors
print(clf.support_vectors_) #[[ 1.  1.] [ 2.  3.]]

# get indices support vectors
print(clf.support_) #[1 2]

# get number of support vectors for each class
print(clf.n_support_) #[1 1]

print(clf.predict([[2, 0]]))
