
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# تعریف میانگین و انحراف معیار
mu = 0
sigma = 1

# تولید داده‌ها
x = np.linspace(-4, 4, 1000)

# محاسبه تابع توزیع تجمعی
y = norm.cdf(x, loc=mu, scale=sigma)

# رسم نمودار
plt.plot(x, y)

plt.title("Gaussian Cumulative Distribution Function")
plt.xlabel("X")
plt.ylabel("CDF")

plt.grid()
plt.show()
