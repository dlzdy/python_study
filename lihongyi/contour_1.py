# -*- coding=utf8 -*-
'''
无论contour还是contourf，都是绘制三维图，其中前两个参数x和y为两个等长一维数组，第三个参数z为二维数组（表示平面点xi,yi映射的函数值）。
正是由于contourf可以填充等高线之间的空隙颜色，呈现出区域的分划状，所以很多分类机器学习模型的可视化常会借助其展现。
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
x = np.array([1, 2])
y = np.array([1, 2])
z = np.array([[1, 2], [2, 3]])
plt.xlim(1, 2)
plt.ylim(1, 2)
colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
cmap = ListedColormap(colors[:len(np.unique(z))])
plt.contourf(x, y, z, cmap=cmap) ###
plt.show()
