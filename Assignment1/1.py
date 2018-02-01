import numpy as np
import matplotlib.pyplot as plt

A = 20
K = 100
r = 0.1
N0 = 50

timestepFactor = 100


def do_magic(T, endTime=50):
    timestep = T/timestepFactor
    ts = np.arange(-T, endTime, timestep)
    N = np.zeros((len(ts),))
    Nderivs = np.zeros((len(ts),))

    for i, t in enumerate(ts):
        if t < 0:
            N[i] = N0
            Nderivs[i] = 0
        else:
            deriv = r*N[i-1]*(1-N[i-1-timestepFactor]/K)*(N[i-1]/A-1)
            Nderivs[i] = deriv
            N[i] = N[i-1] + deriv*timestep

    return ts, N, Nderivs


"""OSCILLATIONS"""

# fig = plt.figure(figsize=(10,5))
# st = fig.suptitle("Population dynamics for different T values")
#
# ax1 = fig.add_subplot(131)
# T = 1
# ts, N, _ = do_magic(T)
# ax1.plot(ts, N)
# ax1.set_xlabel("t")
# ax1.set_ylabel("N(t)")
# ax1.set_title("T=%s" % T)
#
# ax2 = fig.add_subplot(132)
# T = 1.5
# ts, N, _ = do_magic(T)
# ax2.plot(ts, N)
# ax2.set_xlabel("t")
# ax2.set_ylabel("N(t)")
# ax2.set_title("T=%s" % T)
#
# ax3 = fig.add_subplot(133)
# T = 3
# ts, N, _ = do_magic(T)
# ax3.plot(ts, N)
# ax3.set_xlabel("t")
# ax3.set_ylabel("N(t)")
# ax3.set_title("T=%s" % T)
#
# fig.tight_layout()
# st.set_y(0.96)
# fig.subplots_adjust(top=0.85)
# fig.savefig("population_dynamics.eps", format='eps')


"""LIMIT CYCLE"""

fig2 = plt.figure(figsize=(10,5))
st = fig2.suptitle("Delay embedding for different T values")

ax1 = fig2.add_subplot(121)
T = 3.9
_, N, _ = do_magic(T, endTime=20000)
ax1.plot(N[2*timestepFactor-1:-1], N[timestepFactor:-timestepFactor])
ax1.set_xlabel("N(t)")
ax1.set_ylabel("N(t-T)")
ax1.set_title("T=%s" % T)

ax2 = fig2.add_subplot(122)
T = 4
_, N, _ = do_magic(T, endTime=20000)
ax2.plot(N[2*timestepFactor-1:-1], N[timestepFactor:-timestepFactor])
ax2.set_xlabel("N(t)")
ax2.set_ylabel("N(t-T)")
ax2.set_title("T=%s" % T)

fig2.tight_layout()
st.set_y(0.96)
fig2.subplots_adjust(top=0.85)
fig2.savefig("limit_cycle.eps", format='eps')

# plt.plot(N,Nderivs)
plt.show()

# print(max(N))
# print(np.argmax(N))
# print(N[-1])