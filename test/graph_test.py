import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("test100mod.txt", delimiter="\n")
x = np.linspace(0,len(y),len(y))


plt.plot(x,y, '-', label="Time per iteration")

plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.savefig('3kgraph.png', dpi=250)


avg = 0.000122801660143341 #calculated from extract.py
lst = [avg] * len(x)

plt.plot(x,lst, '-', label="Average time")
plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.legend(loc="upper right")

plt.savefig('3kgraph_avg.png', dpi=250)
