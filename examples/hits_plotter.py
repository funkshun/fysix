import matplotlib.pyplot as plt
import datetime
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('mothmemessub.csv', sep=',',header=None)
raw_data = df.values
data = []
for datum in raw_data:
    data.append(datetime.datetime.fromtimestamp(datum).strftime('%c'))

stddev=np.std(data)
mean_t = np.mean(data)

data = data[(abs((data - mean_t) / stddev) < 3)]



binwidth = np.abs(max(data) - min(data))/100
print(binwidth)

plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth))

plt.show()
