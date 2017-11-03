# coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#print(np.random.randn(1000))

data = pd.Series(np.random.randn(2), index=np.arange(2))
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
#data = data.cumsum()
print(data.head());
data = data.cumsum()
# plot methods
# bar, hist, box, kde, area, hexbin, pie
data.plot()
plt.show()

