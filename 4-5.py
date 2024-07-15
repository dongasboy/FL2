import numpy as np
import matplotlib.pyplot as plt
import scipy

# End time [s]
t_end = 10

# Time increments [s] (Change this number if needed)
h = .01

# Points
N = int(t_end / h + 1)

# Gravitational acceleration [m / s^2] (Rewrite this number to the value obtained in the experiment)
G = 9.9

# Pendulum length [m] (Rewrite this number to the value obtained in the experiment)
L = 1.819

# Times of Day
t = np.linspace(0, t_end, N)

# Angular velocity [rad / s]
omega = np.linspace(0, t_end, N)

# Angle [rad]
theta = np.linspace(0, t_end, N)

# Initial conditions
omega[0] = 0  # rad/s
theta[0] = 30 / 180 * np.pi  # rad

# Euler method
for i in range(N-1):
    k = h * (-G/L * np.sin(theta[i]))
    m = h * omega[i]
    omega[i+1] = omega[i] + k
    theta[i+1] = theta[i] + m
theta_data=[]
t_data=[]
# Write to csv file
with open('pendulum_Euler.csv', 'w', newline='') as f:
    for i in range(N):
        f.write(f"{t[i]},{theta[i]}\n")
        t_data.append(t[i])
        theta_data.append(theta[i])
num=0
idt=[]
for i in range(len(theta_data)-1):
    if theta_data[i+1]<0 and theta_data[i]>0:
        num+=1
        idt.append(i)
print(num)
print()
print((t_data[idt[1]]-t_data[idt[0]]))

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ax1.plot(t_data, theta_data, c="r", marker="o")
ax1.set_xlabel("Time [s]", fontsize=20)
ax1.set_ylabel(f"Angle $\Theta$ [rad]",fontsize=20)
ax1.tick_params(labelsize=20)
plt.show()
