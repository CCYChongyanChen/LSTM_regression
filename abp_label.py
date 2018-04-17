# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:35:47 2018

@author: addca
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:40:38 2018

@author: chongyanchen
"""
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import scipy.signal as signal

from scipy import fftpack

file_name = 'merge1.csv'
win = 256
step = 128



df50 = pd.read_csv(file_name, sep=',', usecols=[2])
df2 = df50.iloc[1:,:]
row = len(df2)
sldWinData_max_abp = pd.DataFrame(df2.rolling(win).max())
sldWinData_max_abp = sldWinData_max_abp[win - 1:row:step]
sldWinData_max_abp = np.array(sldWinData_max_abp)
a = []
b = []
c = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for _, item1 in enumerate(sldWinData_max_abp):
    item3 = float(item1)
    if 160<item3:
        a.append(8)
        c[8]+= 1
    if 160> item3 >150:
        a.append(7)
        c[7]+= 1
    if 150 > item3 > 140:
        a.append(6)
        c[6] += 1
    if 140 > item3 > 130:
        a.append(5)
        c[5] += 1
    if 130 > item3 > 120:
        a.append(4)
        c[4] += 1
    if 120 > item3 > 110:
        a.append(3)
        c[3] += 1
    if 110 > item3 > 100:
        a.append(2)
        c[2] += 1
    if 100 > item3 > 90:
        a.append(1)
        c[1] += 1
    elif 90 > item3:
        a.append(0)
        c[0] += 1

print(c)
sldWinData_min_abp = pd.DataFrame(df2.rolling(win).min())
sldWinData_min_abp = sldWinData_min_abp[win - 1:row:step]
sldWinData_min_abp = np.array(sldWinData_min_abp)

d = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for _, item2 in enumerate(sldWinData_min_abp):
    item4 = float(item2)
    if 110<item4:
        b.append(8)
        d[8]+= 1
    if 110> item4 >100:
        b.append(7)
        d[7]+= 1
    if 100 > item4 > 90:
        b.append(6)
        d[6] += 1
    if 90 > item4 > 80:
        b.append(5)
        d[5] += 1
    if 80 > item4 > 70:
        b.append(4)
        d[4] += 1
    if 70 > item4 > 60:
        b.append(3)
        d[3] += 1
    if 60 > item4 > 50:
        b.append(2)
        d[2] += 1
    if 50 > item4 > 40:
        b.append(1)
        d[1] += 1
    elif 40 > item4:
        b.append(0)
        d[0] += 1
print(d)
plt.figure(1)
pl.plot(a, "g", linewidth=1, label=u"lower Envelop")
plt.figure(2)
pl.plot(b, "r", linewidth=1, label=u"upper Envelop")
pl.title(u"abp envelope-demodulation")

pl.legend()
pl.show()
data = pd.DataFrame()
a1 = DataFrame(a)
b1 = DataFrame(b)
data = pd.concat([a1, b1], 1)
data.to_csv('newdata_label1.csv', index=False)