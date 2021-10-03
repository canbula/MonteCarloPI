from bc import TicToc, FindPi


if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_pi = FindPi()
    finding_pi.throw_points(1000000)
    pi = finding_pi.value_of_pi()
    print("PI = %12.8f | I = %d | N = %d" %
          (pi, finding_pi.i, finding_pi.n))
    print("TIME = %.6f seconds" % (tt.toc()))
