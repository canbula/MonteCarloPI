import os
from multiprocessing import Process, Array
import random
import time


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindPi:
    def __init__(self):
        self.n = 0
        self.i = 0

    def throw_points(self, nn, p, all_i, all_n):
        for _ in range(nn):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            self.n += 1
            if (x**2 + y**2) <= 1:
                self.i += 1
        all_i[p] = self.i
        all_n[p] = self.n


if __name__ == "__main__":
    for number_of_p in range(1, os.cpu_count()+1):
        tt = TicToc()
        tt.tic()
        n = int(40320000/number_of_p)
        find_pis = []
        processes = []
        shared_i = Array('i', [0]*number_of_p)
        shared_n = Array('i', [0]*number_of_p)
        for i in range(number_of_p):
            find_pis.append(FindPi())
            processes.append(Process(target=find_pis[i].throw_points, args=(n, i, shared_i, shared_n)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        inner = 0
        total = 0
        for i, n in zip(shared_i, shared_n):
            inner += i
            total += n
        pi = 4 * inner / total
        print(f"P={number_of_p} | Pi = {pi:.8f} | i/n={inner}/{total} | Time = {tt.toc():.8f} seconds")
