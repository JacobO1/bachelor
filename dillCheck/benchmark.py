from __future__ import print_function
import numpy as np
from benchpress.benchmarks import util
import json
import dill
import sys

bench = util.Benchmark("Solving the heat equation using the jacobi method", "height*width*iterations")

#Global variables needed to save and resume program
counter = 0
H = bench.args.size[0]
W = bench.args.size[0]
I = 29000

grid = bench.load_data()


def init_grid(height, width, dtype=np.float32):
    grid = np.zeros((height + 2, width + 2), dtype=dtype)
    grid[:, 0] = dtype(-273.15)
    grid[:, -1] = dtype(-273.15)
    grid[-1, :] = dtype(-273.15)
    grid[0, :] = dtype(40.0)
    return grid


def jacobi(grid, max_iterations, epsilon=0.005):
    def loop_body(grid):
        global counter
        center = grid[1:-1, 1:-1]
        north = grid[0:-2, 1:-1]
        east = grid[1:-1, 2:]
        west = grid[1:-1, 0:-2]
        south = grid[2:, 1:-1]
        work = 0.2 * (center + north + east + west + south)
        delta = np.sum(np.absolute(work - center))
        center[:] = work
        bench.plot_surface(grid, "2d", 0, 200, -200)
        counter += 1
        print(counter)

#DEBUG PRINTS
#        print('grid:\n {}'.format(grid))
#        print('center:\n {}'.format(center))
#        print('north:\n {}'.format(north))
#        print('east:\n {}'.format(east))
#        print('west:\n {}'.format(west))
#        print('south: \n {}'.format(south))


#PRINT ALL GLOBALS
#        for name, value in globals().items():
#        	print('\n\n\n\n\n')
#        	print(name, "-->", value)
#        	try:
#        	    print(json.dumps(name, value))
#        	except:
#        	    pass

#DUMP
        return delta > epsilon
    bench.do_while(loop_body, max_iterations, grid)
    return grid


def main():
    global H, W, I, grid
    
    if grid is None:
    	grid = init_grid(H, W, dtype=bench.dtype)
    
    bench.start()
    grid = jacobi(grid, max_iterations=I)
    bench.stop()
    bench.save_data({'grid': grid})
    bench.pprint()
    dill.dump_session('bch.pkl')
    np.savetxt('yesCheck', grid)

if __name__ == "__main__":
    main()
