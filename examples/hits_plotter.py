import matplotlib.pyplot as plt
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('Animemessub.csv', sep=',',header=None)
data = df.values
sort = np.sort(data, axis=1)
uniq = np.unique(sort)
print(uniq)
binwidth = np.abs(max(uniq) - min(uniq))/4

plt.hist(uniq, bins=np.arange(min(uniq), max(uniq) + binwidth, binwidth))

plt.show()

