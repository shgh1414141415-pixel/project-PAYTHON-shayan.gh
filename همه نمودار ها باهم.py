import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 4, figsize=(18, 10))
fig.suptitle("12 Main Charts", fontsize=16)

# 1) خطی
x = np.linspace(0, 10, 100)
axs[0,0].plot(x, x**2)
axs[0,0].set_title("Line")

# 2) پراکندگی
axs[0,1].scatter(np.random.rand(50), np.random.rand(50))
axs[0,1].set_title("Scatter")

# 3) هیستوگرام
axs[0,2].hist(np.random.randn(1000), bins=30)
axs[0,2].set_title("Histogram")

# 4) جعبه‌ای
axs[0,3].boxplot(np.random.randn(100))
axs[0,3].set_title("Box")

# 5) میله‌ای
axs[1,0].bar(['A','B','C','D','E'], [18,15,20,17,12])
axs[1,0].set_title("Bar")

# 6) دایره‌ای
axs[1,1].pie([30,25,20,15,10], labels=['A','B','C','D','E'])
axs[1,1].set_title("Pie")

# 7) زنگوله
x2 = np.linspace(-4, 4, 200)
axs[1,2].plot(x2, np.exp(-x2**2/2))
axs[1,2].set_title("Normal")

# 8) سطح ۳بعدی
X, Y = np.meshgrid(np.linspace(-3,3,30), np.linspace(-3,3,30))
Z = np.sin(X) + np.cos(Y)
ax3d = fig.add_subplot(3, 4, 9, projection='3d')
ax3d.plot_surface(X, Y, Z, cmap='viridis')
ax3d.set_title("3D Surface")

# 9) کانتور
axs[2,1].contour(X, Y, Z, levels=10)
axs[2,1].set_title("Contour")

# 10) Heatmap
axs[2,2].imshow(np.random.rand(5,5), cmap='hot')
axs[2,2].set_title("Heatmap")

# 11) میدان برداری
Xq, Yq = np.meshgrid(np.linspace(-2,2,10), np.linspace(-2,2,10))
axs[2,3].quiver(Xq, Yq, -Yq, Xq)
axs[2,3].set_title("Vector Field")

# 12) قطبی (جای جدا می‌خواد، پس یه شکل جدید)
fig2 = plt.figure(figsize=(5,5))
axp = fig2.add_subplot(111, projection='polar')
theta = np.linspace(0, 2*np.pi, 200)
axp.plot(theta, 1 + 0.5*np.cos(3*theta))
axp.set_title("Polar")

plt.tight_layout()
plt.show()