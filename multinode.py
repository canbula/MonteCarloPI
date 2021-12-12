import ray
import os
import random
import sys


def init_cluster():
    ray.init(address='auto')
    print(f"This cluster consists of {len(ray.nodes())} nodes and "
          f"{ray.cluster_resources()['CPU']} CPUs in total.")
    return int(ray.cluster_resources()['CPU'])


@ray.remote
def throw_points(n):
    print(f"{os.getpid()} on {os.uname().nodename} is started")
    i = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            i += 1
    print(f"{os.getpid()} on {os.uname().nodename} is finished")
    return i


def main():
    sys.stderr = open(os.devnull, "w")
    number_of_cpu = init_cluster()
    n = 10000000
    inner = ray.get([throw_points.remote(n) for _ in range(number_of_cpu)])
    pi = 4 * sum(inner) / (number_of_cpu*n)
    print(f"Estimated Pi value is {pi:.8f}")


if __name__ == "__main__":
    main()
