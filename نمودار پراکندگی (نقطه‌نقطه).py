import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='red', s=50)
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()