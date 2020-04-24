import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("dillCheck/mod100_timeit.txt", delimiter="\n")

x = np.linspace(0,len(y),len(y))

plt.plot(x,y, '.')
plt.show()
