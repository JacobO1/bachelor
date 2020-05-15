from __future__ import print_function
import numpy as np
from benchpress.benchmarks import util
import dill
import timeit
import psutil

bench = util.Benchmark("Solving the heat equation using the jacobi method", "height*width*iterations")

# Global variables needed to save and resume program
counter = 0
H = 1000
W = 1000
I = 3000

grid = bench.load_data()


def init_grid(height, width, dtype=np.float32):
    grid = np.zeros((height + 2, width + 2), dtype=dtype)
    grid[:, 0] = dtype(-273.15)
    grid[:, -1] = dtype(-273.15)
    grid[-1, :] = dtype(-273.15)
    grid[0, :] = dtype(40.0)
    return grid


def jacobi(grid, max_iterations, epsilon=0.005):
    # save = 'bachelor/benchpress/test/bench_results/100k_500/test' + str(bench.args.size[0]) + '.txt'
    save = 'tmp/actualtmp/TIMING_TMP' + str(bench.args.size[0]) + '.txt'
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
        # print(counter)
        if counter % 500 == 0:
            dill.dump_session('tmp/actualtmp/TEMP_PLSDELETE.pkl')

# DUMP
        return delta > epsilon
# BENCH.DO_WHILE CHANGED TO WHILE TRUE AND IF STATEMENT TO ACCURATELY EXTRACT
# TIME PER ITERATION OF LOOP_BODY.
    while True:
        if counter < max_iterations:
            start_time = timeit.default_timer()
            loop_body(grid)
            stop_time = timeit.default_timer()
            with open(save, 'a') as f:
                f.write(str(stop_time - start_time) + '\n')
        else:
            break
    # bench.do_while(loop_body, max_iterations, grid)
    return grid


def main():
    global H, W, I, grid

    if grid is None:
        grid = init_grid(H, W, dtype=bench.dtype)

    bench.start()
    grid = jacobi(grid, max_iterations=I)
    # print("\n\nTotal context switches during execution = {}".format(psutil.Process().num_ctx_switches()))
    print("\nTotal time waiting for blocking I/O to complete = {} seconds".format(psutil.Process().cpu_times()[4]))
    # print("\nDisk info = {}\n\n".format(psutil.Process().io_counters()))
    bench.stop()
    bench.save_data({'grid': grid})
    bench.pprint()


if __name__ == "__main__":
    main()
