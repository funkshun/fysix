import matplotlib.pyplot as plt
import datetime
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('dankmemes_moth.csv', sep=',',header=None)
data = df.values
# datautc = []

stddev=np.std(data)
mean_t = np.mean(data)
data = np.sort(data, axis=0)

data = data[(abs((data - mean_t) / stddev) < 3)]

binwidth = np.abs(max(data) - min(data))/11
plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth))

fig, ax = plt.subplots(1, 1)

fig.canvas.draw()

labels = [item.get_text() for item in ax.get_xticklabels()]
#print(labels)
# for i in range(0, len(labels)):
#     labels[i] = str(datetime.datetime.utcfromtimestamp(int(float(labels[1]))))
# ax.set_xticklabels(labels)


plt.show()

