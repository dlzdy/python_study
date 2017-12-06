# -*- coding=utf8 -*-
from sklearn.datasets import load_iris
#from sklearn.model_selection.train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import  KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train) #knn训练
#y_pred = knn.predict(X_test)
print(knn.score(X_test, y_test))#预测 测试集的得分，符合度