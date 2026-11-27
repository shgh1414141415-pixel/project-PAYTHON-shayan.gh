import numpy as np
import matplotlib.pyplot as plt

names  = ['Ali', 'Reza', 'Sara', 'Maryam', 'Babak']
scores = [18, 15, 20, 17, 12]

plt.bar(names, scores, color='orange', edgecolor='black')
plt.title("Scores")
plt.xlabel("name")
plt.ylabel("score")
plt.grid(True, axis='y')
plt.show()