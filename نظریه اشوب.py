import matplotlib.pyplot as plt
import random
import math


x_R = 0.0
y_R = 0.0


x_G = 1.0
y_G = 0.0


x_B = 0.5
y_B = math.sqrt(3) / 2   


list_x = []
list_y = []


x = x_R
y = y_R

n = 10000 
for i in range(n):
   
    random_number = random.randint(1, 3)
    
    if random_number == 1:

        x = (x + x_R) / 2
        y = (y + y_R) / 2
        
    elif random_number == 2:

        x = (x + x_G) / 2
        y = (y + y_G) / 2
        
    else:

        x = (x + x_B) / 2
        y = (y + y_B) / 2
        
    list_x.append(x)
    list_y.append(y)



plt.figure(figsize=(8, 7))

plt.scatter(list_x, list_y, s=1, color='blue')

plt.axis('equal')

plt.title('Sierpinski Triangle - Chaos Game')

plt.show()