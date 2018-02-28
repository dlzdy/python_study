# -*- coding=utf8 -*-

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
plt.contour(x, y, z,  cmap=cmap)   ###
plt.show()
