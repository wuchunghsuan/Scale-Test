
import os, sys
import matplotlib.pyplot as plt
import numpy as np


orange = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'

if len(sys.argv) <= 1 :
    exit ("Lack of Job ID.")
jobId = sys.argv[1]

dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report_fetch"
outputTmp = dir + jobId + "/fetch_rate"
outputFig = dir + jobId + "/fetch_rate.pdf"
fi = open(filename)

size_dict = {}

for line in fi:
    args = line.split()
    if len(args) == 0 or float(args[5]) > 100:
        continue
    time = int(args[3]) / 1000
    duration = int(args[2]) / 1000
    if duration == 0:
        duration = 1
    size = int(args[4]) / 1000000 / duration
    for i in range(duration):
        if not size_dict.has_key(time - i):
            size_dict[time - i] = size
        size_dict[time - i] = size_dict[time - i] + size

fi.close()

times = size_dict.keys()
times.sort()
print (times)
sizes = []
for time in times:
    sizes.append(size_dict[time])
sizes = np.asarray(sizes)
print (sizes)

fig, ax = plt.subplots(figsize=(12,5))

xs = np.arange(len(sizes))

line_map = ax.plot(xs, sizes, 
            linewidth=3,
            marker="s",
            color=blue, 
            label='Job')

# ax.set_xticklabels([0,32,64,96,128,160,196,224])
ax.set_xlim(left=(xs[0] - 0.5), right=(xs[-1] + 0.5))
ax.set_ylabel('Transfer data size /MB', fontsize=18)
ax.set_xlabel('Time /seconds', fontsize=18)
# ax.set_ylim(0, 500)

# plot util text

for a,b in zip(xs,sizes):
    plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

lines = line_map
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)

plt.savefig(outputFig)




