import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("test100mod.txt", delimiter="\n")
# y = np.loadtxt("1k/ORIGINAL.txt", delimiter="\n")
x = np.linspace(0,len(y),len(y))
y2 = np.loadtxt("1k/test0.txt", delimiter="\n")
y3 = np.loadtxt("1k/test9.txt", delimiter="\n")

plt.plot(x,y2, 'g-', label="Boop1")
plt.plot(x,y3, 'b-', label="Boop2")
plt.plot(x,y, 'r-', label="Time per iteration")

plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

# plt.savefig('3kgraph.png', dpi=250)


avg = 0.000122801660143341 #calculated from extract.py
lst = [avg] * len(x)

plt.plot(x,lst, '-', label="Average time")
plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.legend(loc="upper right")

# plt.savefig('3kgraph_avg.png', dpi=250)

plt.savefig('temp10.png', dpi=200)