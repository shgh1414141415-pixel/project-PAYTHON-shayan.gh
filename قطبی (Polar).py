import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 200)
r = 1 + 0.5 * np.cos(3 * theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.plot(theta, r, color='purple', linewidth=2)
ax.set_title("Polar Plot")
plt.show()