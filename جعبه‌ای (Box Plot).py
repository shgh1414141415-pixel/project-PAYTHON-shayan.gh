import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10)

plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("value")
plt.grid(True)
plt.show()