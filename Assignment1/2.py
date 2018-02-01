import numpy as np
import matplotlib.pyplot as plt

K = 10 ** 3
r = 0.1
b = 1


def next_step(old):
    return (r + 1) * old / (1 + (old / K) ** b)


steps = 200
nlin_steps = 60
N = np.zeros((steps, 1))
Nlin = np.zeros((nlin_steps, 1))

for N0 in [1, 2, 3, 10]:
    N[0] = N0
    Nlin[0] = N0
    for i in range(1, steps):
        N[i] = next_step(N[i - 1])
    plt.loglog(N)

    for i in range(1, nlin_steps):
        Nlin[i] = (r + 1) * Nlin[i - 1]
    plt.loglog(Nlin, '--')

plt.xlabel("Timestep")
plt.ylabel("N")
plt.title("Population dynamics for N0 close to unstable fixed point")
plt.axis((0.1, 200, 1, 150))
plt.savefig("linapprox_unstable.eps", format='eps')

plt.show()
