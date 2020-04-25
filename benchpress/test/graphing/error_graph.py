import numpy as np
import matplotlib.pyplot as plt

counter = 1

#setup step:
avg_arr = np.loadtxt('../bench_results/checkpoint_500/5test10.txt')
min_max_arr = np.empty([2,3000])
min_max_arr[0] = np.loadtxt('../bench_results/checkpoint_500/5test10.txt')
min_max_arr[1] = np.loadtxt('../bench_results/checkpoint_500/5test10.txt')

# print(avg_arr.shape)
# print(avg_arr)
# print("----------------------------------------------------------------")
# print(min_max_arr.shape)
# print(min_max_arr)


#Skipping 10 first executions for warmup purposes
for i in range(11,2001):
	counter += 1
	curr_exec = np.loadtxt('../bench_results/checkpoint_500/5test' + str(i) + '.txt')
	for j in range(len(curr_exec)):
	
	
		avg_arr[j] += curr_exec[j]

		if (curr_exec[j] < min_max_arr[0][j]):
			#MIN
			min_max_arr[0][j] = curr_exec[j]
		elif (curr_exec[j] > min_max_arr[1][j]):
			#MAX
			min_max_arr[1][j] = curr_exec[j]


final_avg_arr = [(x/counter) for x in avg_arr]

actual_avg = sum(final_avg_arr)/len(final_avg_arr)

x = np.linspace(0,len(final_avg_arr),len(final_avg_arr))


plt.figure(figsize=(20,10))


#Aspect ratio between axis
# ax = plt.gca()
# ax.set_aspect(0.7)

plt.errorbar(x, final_avg_arr, elinewidth=0.75, fmt='midnightblue', yerr=min_max_arr, label="Blue= Iteration average\nRed = Iteration variance", ecolor='tomato')

plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

# plt.savefig('3kgraph.png', dpi=250)

actual_avg_list = [actual_avg] * len(x)

# plt.plot(x, final_avg_arr, 'go', label="Iteration average")
plt.plot(x,actual_avg_list, '-', color='limegreen', label="Overall average time")
plt.xlabel('Iterations')
plt.ylabel('Time in seconds')

plt.legend(loc="upper right")



# plt.savefig('3kgraph_avg.png', dpi=250)
plt.savefig('test.png', dpi=150)
# plt.show()
