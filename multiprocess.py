from bc import TicToc, FindPi
import os
from multiprocessing import Process


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 100
    find_pis = []
    processes = []
    for i in range(os.cpu_count()):
        find_pis.append(FindPi())
        processes.append(Process(target=find_pis[i].throw_points, args=(n,)))
        print("Started thread number #%d" % i)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    inner = 0
    total = 0
    for find_pi in find_pis:
        inner += find_pi.i
        total += find_pi.n
    print("PI = %.8f | I / N = %d / %d | TIME = %.5f seconds"
          % (4 * inner / total, inner, total, tt.toc()))
