import numpy as np
import matplotlib.pyplot as plt

K = 10 ** 3
r = 0.1
b = 1

Nstar = K * r ** (1 / b)
print(Nstar)
deriv = 1 - r * b / (1 + r)


def next_step(old):
    return (r + 1) * old / (1 + (old / K) ** b)


steps = 200
N = np.zeros((steps, 1))
dN = np.zeros((steps, 1))

for dN0 in [-15, -2, 2, 5, 10]:
    N[0] = Nstar + dN0
    dN[0] = dN0
    for i in range(1, steps):
        N[i] = next_step(N[i - 1])
        dN[i] = deriv * (dN[i - 1])
    plt.loglog(N)
    plt.loglog(Nstar + dN, '--')

plt.xlabel("Timestep")
plt.ylabel("N")
plt.title("Population dynamics for N0 close to stable fixed point")
plt.axis((0.1, 200, 84, 111))
plt.savefig("linapprox_stable.eps", format='eps')

plt.show()
