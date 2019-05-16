import matplotlib.pyplot as plt
import numpy as np

orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'
light_green = '#CCFFCC'

f = open('./data/line_job.data')

jobs = []

count = 0
tmp1 = 0.0
for line in f:
    args = line.split()
    if len(args) == 0:
        continue
    count += 1
    if count == 1:
        tmp1 = float(args[0])
    if count == 2:
        jobs.append((float(args[0]) + tmp1) / 2)
        count = 0

jobs = np.asarray(jobs)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)

# plt.rc('hatch', linewidth=2)

fig, ax = plt.subplots(figsize=(12,5))
width = 8

xs = np.arange(len(jobs))

line_map = ax.plot(xs, jobs, 
            linewidth=3,
            marker="s",
            color=blue, 
            label='Job')

ax.set_xticklabels([0,32,64,96,128,160,196,224])
ax.set_xlim(left=(xs[0] - 0.5), right=(xs[-1] + 0.5))
ax.set_ylabel('Job Completion Time /seconds', fontsize=18)
ax.set_xlabel('Scale', fontsize=18)
ax.set_ylim(0, 500)

# plot util text

for a,b in zip(xs,jobs):
    plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

lines = line_map
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)

plt.savefig("./plot/line_job.pdf")


