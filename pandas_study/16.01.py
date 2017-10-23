# coding=utf-8
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4))*0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res = pd.concat([df1,df2], axis=1, join_axes=[df1.index])
print(res)

s1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)
print(res)