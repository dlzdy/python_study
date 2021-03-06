# -*- coding=utf8 -*-
import numpy as np
import matplotlib.pyplot as plt


x_data = [338., 333., 328., 207., 226., 22., 179., 60., 208., 606.]
y_data = [640., 633., 619., 393., 428., 27., 193., 66., 226., 1591.]
# y_data = b+ w * xdata

bias_x = np.arange(-200, -100, 1) #bias, [-200, -199, -101, -100]. 100 个
weight_y = np.arange(-5, 5, 0.1) #weight,[-5,-4.9,-4.8, 0.  4.8, 4.9 5.0] 100个
Z = np.zeros((len(bias_x), len(weight_y))) # 100*100
# Z[j][i] = 偏差 穷举法，把w，b遍历，算出偏差
for i in range(len(bias_x)):
    for j in range(len(weight_y)):
        b = bias_x[i]
        w = weight_y[j]
        Z[j][i] = 0
        for n in range(len(x_data)):
            Z[j][i] = Z[j][i] + (y_data[n] - (b + w*x_data[n]))**2
        Z[j][i] = Z[j][i]/len(x_data)
# 画等高线
plt.contourf(bias_x, weight_y, Z, 50, alpha=0.5, cmap=plt.get_cmap('jet'))

X, Y = np.meshgrid(bias_x, weight_y)
# ydata =  b + w* xdata
b = -120 # inital b
w = -4 # inital w
# lr = 0.0000001 # learning rate
lr = 0.0000006 # learning rate
iteration = 800000

# Store initial values for plotting.
b_history = [b]
w_history = [w]

######
#learning rate 不一样
lr_b = 0
lr_w = 0
######
# Iterations, 对loss的偏微分
for i in range(iteration):
    b_grad = 0.0
    w_grad = 0.0
    for n in range(len(x_data)):
        b_grad = b_grad - 2.0*(y_data[n] - b - w*x_data[n])*1.0
        w_grad = w_grad - 2.0*(y_data[n] - b - w*x_data[n])*x_data[n]
    #############
    # lr_b = lr_b + b_grad**2
    # lr_w = lr_w + w_grad**2


    # Updata parameters
    b = b - lr * b_grad
    w = w - lr * w_grad

    # b = b - lr_b * b_grad
    # w = w - lr_w * w_grad
    # Store parameters for ploting
    b_history.append(b)
    w_history.append(w)

# plot the figure

plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color='black')
plt.xlim(-200, -100)
plt.ylim(-5,5)
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$w$', fontsize=16)
plt.show()

