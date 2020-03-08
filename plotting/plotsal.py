import numpy as np
import matplotlib.pyplot as plt

#get the sweet-sweet data
salary = np.fromfile("salaries.txt", dtype=int, sep=",")

#important difference between string and int retrival!
names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

#lower-upper cut
salary = salary[2:-1]
names = names[2:-1]

x = np.arange(len(names))

#labeling
plt.bar( x, salary)
plt.xticks( x, names)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

#for nicer comparison
plt.yscale("log")
plt.grid( which='both', axis = 'y', linestyle ="-.", linewidth = 1)

#console print
#print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

#magic
plt.show()
