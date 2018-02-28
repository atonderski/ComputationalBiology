import numpy as np
from scipy.ndimage.filters import laplace
import matplotlib.pyplot as plt
import matplotlib.cm as cm

a = 0.1
b = 1
c = 0.5
K = 30
D = 1

S0 = b / a
I0 = K * (b - c) - b / a


def s_deriv(I, S):
    return b * (I + S) - c * S - S * (I + S) / K - a * S * I


def i_deriv(I, S):
    return -c * I - I * (I + S) / K + a * S * I


num_patches = 100

timestep_length = 0.01
num_timesteps = 5000
infected_matrix = np.zeros((num_patches, num_timesteps))
susceptible_matrix = np.zeros((num_patches, num_timesteps))

infected_matrix[0,0] = I0
susceptible_matrix[0,0] = S0

for i in range(1, num_timesteps):
    infected = infected_matrix[:,i - 1]
    susceptible = susceptible_matrix[:,i - 1]
    inf_lapl = 4*laplace(infected, mode='wrap')
    sus_lapl = 4*laplace(susceptible, mode='wrap')
    infected_matrix[:,i] = infected + timestep_length * (i_deriv(infected, susceptible) + D * inf_lapl)
    susceptible_matrix[:,i] = susceptible + timestep_length * (s_deriv(infected, susceptible) + D * sus_lapl)
    print(sum(infected) + sum(susceptible))

print(susceptible_matrix[:,-1])
print(infected_matrix[:,-1])

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.imshow(susceptible_matrix[:,::10], cmap=cm.jet)
ax2 = fig.add_subplot(212)
ax2.imshow(infected_matrix[:,::10], cmap=cm.jet)
plt.show()
