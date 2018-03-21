from multiprocessing.pool import Pool
import numpy as np
import matplotlib.pyplot as plt

alpha = 1
beta = 0.75
I0 = (1 - beta / alpha)
S0 = np.log(alpha / beta) - (1 - beta / alpha)

Nmax = 1 / S0
print(Nmax)
Ns = np.linspace(10 ** 1, 2 * Nmax, 20)


def run_for_n(N):
    print("Starting simulation for N=%s" % N)
    extinction_time = 0
    runs = 40
    for _ in range(runs):
        n = I0
        i = 0
        while True:
            i += 1
            prob_increase = alpha * (1 - n) * n
            prob_decrease = beta * n
            # Normalize probabilities since we don't care about the situation where nothing changes
            prob_norm_factor = prob_decrease + prob_increase
            if np.random.rand() < prob_increase / prob_norm_factor:
                n += 1 / N
            else:
                n -= 1 / N
            if n < 1 / N:
                extinction_time += i
                print("Exctintion for N=%s after %s" % (N, i))
                break
    avg_extinction_time = extinction_time / runs
    print("Average exctinction time for N=%s: %s" % (N, avg_extinction_time))
    # print("S0=%s" % S0)
    expected = np.exp(N * S0)
    print("Expected extinction time for N=%s : %s" % (N, expected))
    return N, avg_extinction_time, expected


p = Pool(8)
results = p.map(run_for_n, Ns, chunksize=1)
results.sort(key=lambda x: x[0])
print(results)
ns = [ext[0] for ext in results]
extinction_times = np.array([ext[1] for ext in results])
expected_extinction_times = np.array([ext[2] for ext in results])
magic_constant = extinction_times[int(len(ns)/2)]/expected_extinction_times[int(len(ns)/2)]
print(extinction_times)
plt.semilogy(ns, extinction_times)
plt.semilogy(ns, magic_constant * expected_extinction_times, '--')
plt.show()
