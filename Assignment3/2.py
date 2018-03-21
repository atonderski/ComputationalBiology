import numpy as np
import matplotlib.pyplot as plt

N = 20
gamma = 0.1
Kc = 2 * gamma

step_length = 0.01
num_steps = 30000
time = 0.01 * np.arange(0, num_steps)


def run_simulation(kMultiplier, subplot):
    K = kMultiplier * Kc
    omegas = -gamma / np.tan(np.pi * np.random.random((N, 1)))
    phases = (np.random.random((N, 1)) - 0.5) * np.pi
    order_parameters = np.zeros((num_steps, 1))
    for i in range(num_steps):
        # First calculate the order parameter (using angle averaging haxx)
        avg_phase = np.angle(np.mean(np.exp(1j*phases)))
        order_parameters[i] = np.real(1 / N * np.sum(np.exp(1j * (phases - avg_phase))))
        # Then update the phases
        phase_diffs = phases.transpose() - phases
        sum = np.sum(np.sin(phase_diffs), axis=1).reshape((N, 1))
        phases += step_length * (omegas + K / N * sum)
    plt.subplot(subplot)
    plt.plot(time, order_parameters)
    plt.title(r'$K=%sK_c$, $\gamma=%s$, $N=%s$' % (kMultiplier, gamma, N))
    plt.xlabel(r't')
    plt.ylabel(r'r')
    plt.ylim(0, 1)
    plt.xlim(0, num_steps * step_length)
    if Kc < K < 2 * Kc:
        expected_r = np.sqrt((K - Kc) / Kc)
        print("expected r = %s" % expected_r)
        plt.plot([0, num_steps * step_length], [expected_r, expected_r], 'r--')
        plt.legend(["Simulated order parameter", "Expected order parameter"])
    else:
        plt.legend(["Simulated order parameter"])


plt.figure(figsize=(10, 15))
for i, kFactor in enumerate([0.5, 1.15, 5]):
    run_simulation(kFactor, 310 + i + 1)
# plt.savefig("2_%s.eps" % N)
plt.show()
