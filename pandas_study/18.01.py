# coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print(np.random.randn(1000))

data = pd.Series(np.random.randn(2), index=np.arange(2))
data = data.cumsum()
print(data)
data.plot()
plt.show()

