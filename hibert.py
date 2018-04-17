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

file_name = 'merged.csv'
win = 256
step = 128

df0 = pd.read_csv(file_name, sep=',', usecols=[0])

row = len(df0)
sldWinData_max_ppg = pd.DataFrame(df0.rolling(win).max())
sldWinData_max_ppg = sldWinData_max_ppg[win - 1:row:step]
sldWinData_max_ppg = np.array(sldWinData_max_ppg)
sldWinData_min_ppg = pd.DataFrame(df0.rolling(win).min())
sldWinData_min_ppg = sldWinData_min_ppg[win - 1:row:step]
sldWinData_min_ppg = np.array(sldWinData_min_ppg)
plt.figure(1)
pl.plot(sldWinData_min_ppg, "g", linewidth=1, label=u"lower Envelop")
pl.plot(sldWinData_max_ppg, "r", linewidth=1, label=u"upper Envelop")
pl.title(u"ppg envelope-demodulation")

df2 = pd.read_csv(file_name, sep=',', usecols=[2])
row = len(df2)
sldWinData_max_abp = pd.DataFrame(df2.rolling(win).max())
sldWinData_max_abp = sldWinData_max_abp[win - 1:row:step]
sldWinData_max_abp = np.array(sldWinData_max_abp)

sldWinData_min_abp = pd.DataFrame(df2.rolling(win).min())
sldWinData_min_abp = sldWinData_min_abp[win - 1:row:step]
sldWinData_min_abp = np.array(sldWinData_min_abp)

plt.figure(2)
pl.plot(sldWinData_min_abp, "g", linewidth=1, label=u"lower Envelop")
pl.plot(sldWinData_max_abp, "r", linewidth=1, label=u"upper Envelop")
pl.title(u"abp envelope-demodulation")

df1 = pd.read_csv(file_name, sep=',', usecols=[1])
row = len(df1)
sldWinData_max_ecg = pd.DataFrame(df1.rolling(win).max())
sldWinData_max_ecg = sldWinData_max_ecg[win - 1:row:step]
sldWinData_max_ecg = np.array(sldWinData_max_ecg)
sldWinData_min_ecg = pd.DataFrame(df1.rolling(win).min())
sldWinData_min_ecg = sldWinData_min_ecg[win - 1:row:step]
sldWinData_min_ecg = np.array(sldWinData_min_ecg)
plt.figure(3)
pl.plot(sldWinData_min_ecg, "g", linewidth=1, label=u"lower Envelop")
pl.plot(sldWinData_max_ecg, "r", linewidth=1, label=u"upper Envelop")
pl.title(u"ecg envelope-demodulation")
pl.legend()
pl.show()
data = pd.DataFrame()
abp = DataFrame(sldWinData_max_abp)
ppg = DataFrame(sldWinData_max_ppg)
data = pd.concat([ppg, abp], 1)
data.to_csv('thewhole_part1.csv', index=False)