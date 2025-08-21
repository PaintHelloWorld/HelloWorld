from matplotlib import pyplot as plt
import numpy as np

epsilon = 0.001
x = np.linspace(-0.5*np.pi + epsilon , 0.5*np.pi - epsilon , 100)
y = np.tan(x)

fig,ax = plt.subplots()
fig.canvas.manager.set_window_title("Alan Walker")

ax.plot(x,y)
ax.set_aspect('equal')
ax.set_xlim(-2,2)
ax.set_ylim(-5,5)

plt.xlabel("day")
plt.ylabel("gfgj")
plt.title("123456")
plt.grid(True)
plt.show()
