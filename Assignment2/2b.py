import numpy as np
from scipy.ndimage.filters import laplace
import matplotlib.pyplot as plt
import matplotlib.cm as cm

a = 3
b = 8

u0 = a
v0 = b / a


def u_deriv(u, v):
    return a - (b + 1) * u + u ** 2 * v


def v_deriv(u, v):
    return b * u - u ** 2 * v


L = 128

timestep_length = 0.005
num_timesteps = 10000
u_matrix = np.zeros((L, L))
v_matrix = np.zeros((L, L))


Ds = [2.3, 3, 5, 9]

plt.figure(figsize=(8, 14))
for i, D in enumerate(Ds):
    u_matrix = u0 -0.1 + 0.2 * np.random.random((L, L))
    v_matrix = v0 -0.1 + 0.2 * np.random.random((L, L))
    for j in range(1, num_timesteps):
        if j == 500:
            print(2 * i + 1)
            plt.subplot(len(Ds), 2, 2 * i + 1)
            plt.imshow(u_matrix, cmap=cm.coolwarm, vmin=0, vmax=10)
            plt.colorbar()
            plt.title(r'$D_v = %s$, Transient' % D)
        u_lapl = 4 * laplace(u_matrix, mode='wrap')
        v_lapl = 4 * laplace(v_matrix, mode='wrap')
        u_matrix += timestep_length * (u_deriv(u_matrix, v_matrix) + u_lapl)
        v_matrix += timestep_length * (v_deriv(u_matrix, v_matrix) + D * v_lapl)

    print(2 * i + 2)
    plt.subplot(len(Ds), 2, 2 * i + 2)
    plt.imshow(u_matrix, cmap=cm.coolwarm, vmin=0, vmax=10)
    plt.colorbar()
    plt.title(r'$D_v = %s$, Final' % D)

plt.savefig('2b.eps')
plt.show()
