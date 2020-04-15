import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("test100mod.txt", delimiter="\n")

x = np.linspace(0,len(y),len(y))


plt.plot(x,y, '-')

plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.savefig('3kgraph.png', dpi=250)