# -*- coding=utf8 -*-
import numpy as np
np.random.seed(1337) # for reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# create some data
X = np.linspace(-1, 1, 200)