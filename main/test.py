import simulator as sm
import numpy as np
import matplotlib.pyplot as plt

x = sm.simulate("entertainment")[1]
#print(x)

T_test = 200
t = np.arange(T_test)

subnames_test = ['movies',
'television',
'music',
'celebrities',
'actors',
'movieclub',
'documentaries',
'westerns']

plt.figure(1)

for name in subnames_test:
    x1 = np.array(x[name])
    plt.plot(t, x1, c=np.random.rand(3,), label = name)

plt.grid()
plt.legend()
plt.show()
