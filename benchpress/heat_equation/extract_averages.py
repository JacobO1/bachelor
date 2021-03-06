import io
import sys

counter = 0

reg_avg = 0
reg_count = 0

dump_avg = 0
dump_count = 0


with open('bench_results/performance_difference.txt', 'r') as f:
	for line in f:
		counter += 1
		if counter % 100 == 0:
			dump_avg += float(line)
			dump_count += 1
		else:
			reg_avg += float(line)
			reg_count += 1

print('\n\nAverage of dump iterations: \t {}'.format(dump_avg/dump_count))
print('Average of regular iterations: \t {}\n\n'.format(reg_avg/reg_count))

# gennemsnit i alt:

avg = (reg_avg+dump_avg)/(reg_count+dump_count)

print(avg)
