import numpy as np
import matplotlib.pyplot as plt

N = 200
alpha = 0.8
beta = 0.6
I0 = (1 - beta / alpha)

timesteps = 5 * 10 ** 5
combined_infectives = np.zeros((timesteps))
combined_nonextinct_infectives = np.zeros((timesteps))

exctinction_time = 0

runs = 0
nonextinct_runs = 0
while runs < 40:
    runs += 1
    infectives = np.zeros((timesteps))
    infectives[0] = I0
    for i in range(1, timesteps):
        n = infectives[i - 1]
        prob_increase = alpha * (1 - n) * n
        prob_decrease = beta * n
        # Normalize probabilities since we don't care about the situation where nothing changes
        prob_norm_factor = prob_decrease + prob_increase
        if np.random.rand() < prob_increase / prob_norm_factor:
            infectives[i] = n + 1 / N
        else:
            infectives[i] = n - 1 / N
        if infectives[i] <= 0:
            exctinction_time += i
            print("DEAD")
            break
    combined_infectives += infectives
    if infectives[timesteps - 1] >= 1 / N:
        nonextinct_runs += 1
        combined_nonextinct_infectives += infectives
        print("UNDEAD")

combined_infectives /= runs
combined_nonextinct_infectives /= nonextinct_runs

print("Total runs: %s" % runs)
print("Nonextinct runs: %s" % nonextinct_runs)

avg_extinction_time = exctinction_time / (runs - nonextinct_runs)
print("Average exctinction time: %s" % avg_extinction_time)

plt.plot(combined_nonextinct_infectives)
plt.plot(combined_infectives)
plt.ylim(0, 1)
plt.show()
