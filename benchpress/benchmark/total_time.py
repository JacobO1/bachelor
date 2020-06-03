import io
import sys

total = 0


with open('timings/lb/100/test0.txt', 'r') as f:
	for line in f:
		total += float(line)


# gennemsnit i alt:



print("samlet tid 100: ", total)

total = 0


with open('timings/lb/stripped/test0.txt', 'r') as f:
	for line in f:
		total += float(line)


# gennemsnit i alt:



print("samlet tid stripped: ", total)
