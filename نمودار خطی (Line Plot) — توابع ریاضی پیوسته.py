import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print("matplotlib version:", matplotlib.__version__)
print("backend:", matplotlib.get_backend())

x = np.linspace(0, 10, 100)
y = x**2

print("x first 3:", x[:3])
print("y first 3:", y[:3])

plt.plot(x, y)
plt.title("Test")
plt.savefig("test_plot.png")   # ← این خط مهمه! ذخیره می‌کنه
print("saved test_plot.png")
plt.show()
print("done")