from matplotlib import pyplot as plt
import numpy as np

epsilon = 0.001
x = np.linspace(epsilon , 6 , 100)
y = np.log10(x)

fig,ax = plt.subplots()
fig.canvas.manager.set_window_title("y = lg x")

ax.plot(x , y)
ax.set_aspect("equal")
ax.set_xlim(-6,6)
ax.set_ylim(-6,6)

plt.xlabel("x")
plt.ylabel("y")
plt.title("y = lg x")
plt.grid(True)
plt.show()
