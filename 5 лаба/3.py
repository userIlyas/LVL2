import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, 2*math.pi)
r = 10 * (1 + np.cos(t))

plt.plot(t, r)
plt.xlabel('f')
plt.ylabel('r')
plt.title('Graph')
plt.grid(True)
plt.show()