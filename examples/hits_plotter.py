import matplotlib.pyplot as plt
import datetime
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('mothmemessub.csv', sep=',',header=None)
data = df.values
datautc = []

stddev=np.std(data)
mean_t = np.mean(data)

data = data[(abs((data - mean_t) / stddev) < 3)]



binwidth = np.abs(max(data) - min(data))/100
print(binwidth)
fig, ax = plt.subplots()
fig.canvas.draw()

plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth))


plt.show()
