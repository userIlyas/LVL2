import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-4.6, 5)
x2 = np.linspace(-3, 3)
x3 = np.linspace(-5.1, -3)
x4 = np.linspace(3, 5.3)
x5 = np.linspace(-7.7, -4.3)
x6 = np.linspace(4.5, 5.5)
x7 = np.linspace(-7.5, -6.5)
x8 = np.linspace(-5.5, -4.5)

y1 = -3/25 * x1**2 + 6
y2 = -1/3 * x2**2 + 2
y3 = 6 * (x3 + 4)**2 - 7
y4 = 6 * (x4 - 4)**2 - 7
y5 = (x5 + 6)**2
y6 = -24 * (x6 - 5)**2 + 9
y7 = -4 * (x7 + 7)**2 + 4
y8 = -4 * (x8 + 5)**2 + 4

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of cat')
plt.grid(True)
plt.show()