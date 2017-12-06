# -*- coding=utf8 -*-
import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32) # 0~1
y_data = x_data*0.1 + 0.3 # y=0.1x + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))# -1 -- 1
biases = tf.Variable(tf.zeros([1])) # = 0
y = Weights*x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5) # 学习效率
train = optimizer.minimize(loss)

init = tf.initialize_all_tables()
### create tensorflow structure end ###

sess = tf.Session()
sess.run(init)  #Very important , 激活

#训练
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights), sess.run(biases))