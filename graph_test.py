import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,29001,29001)

y = np.loadtxt("dillCheck/mod100_timeit.txt", delimiter="\n")

plt.plot(x,y)
plt.show()
