import subprocess
import os
import io

for i in range(10):
	print(i)
	process = subprocess.Popen(["python3 benchmark.py {}".format(i)], shell=True)
	process.wait()
	print(process.returncode)