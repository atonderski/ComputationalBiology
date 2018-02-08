import numpy as np
import matplotlib.pyplot as plt


eta0 = 900
alpha= 0.01

for R in np.arange(1,30,0.1):
    etas = np.zeros((300,))
    etas[0] = eta0
    for i in range(1, 300):
        etas[i] = etas[i-1] * R * np.exp(-alpha * etas[i-1])
    plt.plot(np.zeros(100,) + R, etas[-101:-1], 'b.', markersize=1)
    print("R: %s, max: %.2f, min: %.2f" % (R, max(etas[-101:-1]), min(etas[-101:-1])))

plt.plot((7.4, 7.4), (0, 800), 'k--')
plt.plot((12.5, 12.5), (0, 800), 'k--')
plt.xlabel("R")
plt.ylabel("N")
plt.title("Bifurcation diagram")
plt.savefig("chaos_bifurcation.eps", format='eps')

plt.show()


# FIRST SPLIT AROUND R=7.4
# SECOND SPLIT AROUND R=12.5