import numpy as np
import matplotlib.pyplot as plt


eta0 = 900
alpha= 0.01


fig = plt.figure(figsize=(15,5))
st = fig.suptitle("Population dynamics for varying R values")


for i, R in enumerate([5, 10, 13]):
    ax1 = fig.add_subplot(131+i)
    etas = np.zeros((300,))
    etas[0] = eta0
    for i in range(1, 300):
        etas[i] = etas[i-1] * R * np.exp(-alpha * etas[i-1])
    ax1.plot(etas)
    ax1.set_title("R=%s" % R)
    ax1.set_xlabel(r't')
    ax1.set_ylabel(r'$\eta_t$')

fig.savefig("chaos_population_dynamics.eps", format='eps')
plt.show()
