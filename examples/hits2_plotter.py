import matplotlib.pyplot as plt
import datetime
import pandas as pd
import pylab
import numpy as np


df = pd.read_csv('mothmemes_moth.csv', sep=',',header=None)
data = df.values
# datautc = []

stddev=np.std(data)
mean_t = np.mean(data)
data = np.unique(np.sort(data, axis=0))
print(len(data))

#engaging in... sigma cutting :(
data = data[(abs((data - mean_t) / stddev) < 3)]
print(len(data))

binwidth = np.abs(max(data) - min(data))/17

plt.hist(data, bins=np.arange(min(data), max(data) + binwidth, binwidth))
locs, labels = plt.xticks()
plt.title('The Moth meme in r/mothmemes')
plt.ylabel("'Moth' or 'lamp' hits on top posts/comments for r/mothmemes")
plt.xlabel('date')
plt.xticks(locs, ['', '9/22/18', '', '9/26/18', '', '10/1/18', '', '10/6/18', ''])


# fig, ax = plt.subplots()

# fig.canvas.draw()

# labels = [item.get_text() for item in ax.get_xticklabels()]
# print(labels)
# # for i in range(0, len(labels)):
# #     labels[i] = str(datetime.datetime.utcfromtimestamp(int(float(labels[1]))))
# # ax.set_xticklabels(labels)


plt.show()

