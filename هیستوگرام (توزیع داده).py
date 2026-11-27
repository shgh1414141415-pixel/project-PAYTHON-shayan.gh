import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=3, color='steelblue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("count")
plt.grid(True)
plt.show()