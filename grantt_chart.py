# Author Rishikesh Kushwaha
# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt
import numpy as np
# Load completion time for each job
ct = np.loadtxt('completion_time.txt', dtype=int)
# Solution have sequennce in which job is scheduled
sol = np.loadtxt('solution.txt', dtype=int)
# load processing time of each job on each machine
p = np.loadtxt('processing_time.txt')

p = p.transpose()
# Declaring a figure "gnt"
fig, gnt = plt.subplots()
fig.set_size_inches(18.5, 10.5)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('Time')
gnt.set_ylabel('Jobs')

# Setting ticks on y-axis
gnt.set_yticks([(12 * i) for i in range(20 + 1)])
# Labelling tickes of y-axis
gnt.set_yticklabels([(i) for i in range(20 + 1)])
gnt.set_prop_cycle(color=['red', 'green', 'blue', 'black', 'yellow'])

# Setting graph attribute
gnt.grid(True)
out = []
for i in range(len(p)):
    l = []
    for j in range(len(ct[i])):
        l.append((int(ct[i][j] - p[sol[i]][j]), p[sol[i]][j]))
    gnt.broken_barh(l, ((i + 1) * 12, 9), color=['red', 'green', 'blue', 'orange', 'yellow'])
# saving gantt chart
plt.savefig("gantt.png", dpi=100)