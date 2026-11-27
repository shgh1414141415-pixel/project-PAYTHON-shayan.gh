import matplotlib.pyplot as plt

sizes  = [18, 15, 20, 17, 12]
labels =  ['Ali', 'Reza', 'Sara', 'Maryam', 'Babak']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()