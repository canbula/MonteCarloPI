from bc import TicToc, FindPi
import os
from threading import Thread


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 10000000
    find_pis = []
    threads = []
    for i in range(os.cpu_count()):
        find_pis.append(FindPi())
        threads.append(Thread(target=find_pis[i].throw_points, args=(n,)))
        print("Started thread number #%d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    inner = 0
    total = 0
    for find_pi in find_pis:
        inner += find_pi.i
        total += find_pi.n
    print("PI = %.8f | I / N = %d / %d | TIME = %.5f seconds"
          % (4 * inner / total, inner, total, tt.toc()))
