import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.title("Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()