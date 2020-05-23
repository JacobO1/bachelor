import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("../bench_results/new_filename/spike.txt", delimiter="\n")
x = np.linspace(0,len(y),len(y))


plt.figure(figsize=(10,6))
plt.plot(x,y, 'r-', label="Time per iteration")

plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

avg = sum(y)/len(y)
lst = [avg] * len(x)

plt.title("Graph with spiked results")
plt.plot(x,lst, '-', label="Average time")
plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.legend(loc="upper right")
plt.savefig('spike_newname.png', dpi=150)