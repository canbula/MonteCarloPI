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

    def throw_points(self, nn):
        for _ in range(nn):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            self.n += 1
            if (x**2 + y**2) <= 1:
                self.i += 1

    def value_of_pi(self):
        return 4 * self.i / self.n
