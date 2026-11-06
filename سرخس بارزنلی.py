import matplotlib.pyplot as plt
import random

list_x = []
list_y = []

x = 0.0
y = 0.0

n = 100000

for i in range(n):
    r = random.randint(1, 100)
    
    if 1 <= r <= 2: 
        new_x = 0
        new_y = 0.27 * y
        
    elif 3 <= r <= 17: 
        new_x = -0.14 * x + 0.26 * y + 0.57
        new_y = 0.25 * x + 0.22 * y - 0.04
        
    elif 18 <= r <= 30: 
        new_x = 0.17 * x - 0.21 * y + 0.41
        new_y = 0.22 * x + 0.18 * y + 0.09
        
    else: 
        new_x = 0.78 * x + 0.03 * y + 0.11
        new_y = -0.03 * x + 0.74 * y + 0.27
        
    x = new_x
    y = new_y
    
    list_x.append(x)
    list_y.append(y)

plt.figure(figsize=(6, 9))
plt.scatter(list_x, list_y, s=0.1, color='green')
plt.axis('off') 
plt.title('Barnsley Fern', fontsize=14, fontweight='bold')
plt.show()