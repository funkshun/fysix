import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import simulator as sm

#
simulname = "gaming"
y = sm.simulate(simulname)[1]
y= np.transpose(y)
#print(y[0])
#print(x)
T_test = 200
t = np.arange(T_test)

subnames_test = ['gaming',
'Overwatch',
'leagueoflegends',
'Warframe',
'Rainbow6',
'titanfall',
'DestinyTheGame',
'pcmasterrace',
'Games',
'skyrim',
'csgo',
'DotA2',
'wow',
'Fallout',
'PUBG',
'FortNiteBR',
'hearthstone',
'smashbros',
'starcraft',
'truegaming']

colors = []
fig, ax = plt.subplots()
lines = ax.plot(t, y)
i = 0
for line in lines:
    #print(line)
    colors.append(line.get_color())
    i += 1
#print(len(lines))
y= np.transpose(y)

#print(y[4])
def update(num, t, y, lines):
    for i in range(len(lines)):
        lines[i].set_data(t[:num], y[i][:num])
        lines[i].axes.axis([0, 200, 0, 1])
    return lines

ani = animation.FuncAnimation(fig, update, len(t), fargs=[t, y, lines],
                              interval=25, blit=False)
#ani.save('test.gif')
plt.ylabel('Subreddit Infection Percentage')
plt.xlabel('Time')
plt.grid()
for i in range(len(lines)):
    plt.plot(np.array([]), np.array([]), color = colors[i], label = subnames_test[i])
plt.legend()
plt.show()

ani.save(simulname + '.gif')
