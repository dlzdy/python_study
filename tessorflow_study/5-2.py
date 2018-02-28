# -*- coding=utf8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def show_data(x, y, w, b):
    '''
    绘图函数
    :param x: 横坐标散点
    :param y: 纵坐标散点
    :param w: 权重
    :param b: 偏移量
    :return:  无
    '''
    # plt.figure()
    plt.scatter(x, y, marker='.') # 实际点
    plt.scatter(x, (w * x + b), marker='.') #新生成的点

def draw_orignal(x, y):
    '''
    绘图函数
    :param x: 横坐标散点
    :param y: 纵坐标散点
    :return:  无
    '''
    plt.clf()  # 清图。
    # plt.cla()  # 清坐标轴。
    # plt.close()  # 关窗口
    plt.scatter(x, y, marker='.',color='g') # 实际点

def draw_target(x, y, w, b):
    plt.clf()  # 清图。
    plt.scatter(x, y, marker='.', color='g')  # 实际点
    plt.scatter(x, (w * x + b), marker='.') #新生成的点


### 生成数据 ###
x_data = np.random.rand(100).astype(np.float32) # 0--1
y_data = 0.1 * x_data + 0.3

### 创建结构 ###
#Weights ，biases 是变量取值
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))  # 损失函数 差的平方
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 优化器&学习率选择
train = optimizer.minimize(loss)  # 优化器优化目标选择

init = tf.global_variables_initializer()  # 初始化全变量节点

### 训练部分
plt.show()
with tf.Session() as sess:
    sess.run(init)
    for step in range(500):
        sess.run(train)
        if step % 50 == 0:
            print(step, sess.run(Weights), sess.run(biases), sess.run(loss))
            draw_target(x_data, y_data, sess.run(Weights), sess.run(biases))

