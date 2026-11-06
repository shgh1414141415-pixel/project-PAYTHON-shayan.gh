import matplotlib.pyplot as plt
import random

list_x = []
list_y = []

x = 0.0
y = 0.0

n = 100000

for i in range(n):
    r = random.random()
    
    if r < 0.40:
        new_x = 0.307692 * x - 0.531469 * y + 5.401953
        new_y = -0.461538 * x - 0.293706 * y + 8.655175
        
    elif r < 0.55:
        new_x = 0.307692 * x - 0.076923 * y - 1.295248
        new_y = 0.153846 * x - 0.447552 * y + 4.152990
        
    else:
        new_x = 0.000000 * x + 0.545455 * y - 4.893637
        new_y = 0.692308 * x - 0.195804 * y + 7.269794
        
    x = new_x
    y = new_y
    
    list_x.append(x)
    list_y.append(y)

plt.figure(figsize=(8, 8))
plt.scatter(list_x, list_y, s=0.1, color='coral')
plt.axis('equal')
plt.axis('off')
plt.title('Coral Fractal', fontsize=14, fontweight='bold')
plt.show()