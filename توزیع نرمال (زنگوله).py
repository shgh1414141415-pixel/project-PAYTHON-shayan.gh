import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 200)
y = np.exp(-(x-2)**2 / 2)

plt.plot(x, y, color='green', linewidth=2)
plt.title("Normal Distribution (Bell Curve)")
plt.xlabel("x")
plt.ylabel("density")
plt.grid(True)
plt.show()