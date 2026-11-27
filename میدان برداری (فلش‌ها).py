import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

U = -Y
V = X

plt.quiver(X, Y, U, V)
plt.title("Vector Field")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()