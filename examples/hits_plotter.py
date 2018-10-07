import matplotlib.pyplot as plt
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('moth_meme.csv', sep=',',header=None)
data = df.values
binwidth = np.abs(max(data) - min(data))/30
print(binwidth)

plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth))

plt.show()
