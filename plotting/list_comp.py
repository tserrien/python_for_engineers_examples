import numpy as np
import matplotlib.pyplot as plt

x = [5,10,15,20,25]
y = []

#oldschool
for counter in x:
    y.append(counter / 5)

#new
z = [n / 5 for n in x]

#the numpy way
a = np.array(x)
b = a / 5 #because numpy is awesome

#print("\nOld fashioned way: x = {} y = {} \n".format(x, y))
#print("\nCompact way: x = {} z = {} \n".format(x, z))
#print("\nNumpy way: a = {} b = {} \n".format(a, b))

x = np.linspace(0,20,3000)
#print(x)

y1 = np.sin(x)
y2 = np.cos(x)

#plotting funtions
plt.plot(x, y1, "-g", label = 'sine')
plt.plot(x, y2, "-b", label = "cos")

#labeling
plt.legend(loc="upper right")

#setting limits
#plt.ylim(-1.1, 1.1)

#magic
plt.show()
