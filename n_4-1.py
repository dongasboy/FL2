import numpy as np

# End time [s]
t_end = 2
# Time increments [s]
h = 0.1
# Points
N = int(t_end / h + 1)
# Time
t = np.linspace(0, t_end, N)

# Exact solution
x_true = np.exp(t ** 2 / 2)

# Write to csv file
with open('practice_true.csv', 'w', newline='') as f:
    f.write('time,Exact_solution')  
    f.write('\n') # line feed code
    for i in range(N):
        f.write(str(t[i]) + ',' + str(x_true[i]))
        f.write('\n')
