
import os, sys
import matplotlib.pyplot as plt
import numpy as np


orange = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'

dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test/"
filename = dir + "report_ops"
fi = open(filename)

jobId = [4,5]

jobs = {}

for line in fi:
    args = line.split("-")
    if len(args) != 6:
        continue
    jId = int(args[2])
    if jId not in jobId:
        continue
    if not jobs.has_key(jId) :
        jobs[jId] = {}
    job = jobs.get(jId)
    time = int(args[3]) / 1000
    duration = int(args[4]) / 1000
    if duration == 0:
        duration = 1
    size = float(args[5]) / 1000000 / duration
    for i in range(duration):
        if not job.has_key(time - i):
            job[time - i] = size
        job[time - i] = job[time - i] + size
    # jobs[jId] = job

fi.close()

def draw(id, job):
    times = job.keys()
    times.sort()
    sizes = []
    for time in times:
        sizes.append(int(job[time]))
    sizes = np.asarray(sizes)

    fig, ax = plt.subplots(figsize=(12,5))

    xs = np.arange(len(sizes))

    line = ax.plot(xs, sizes, 
                linewidth=3,
                marker="s",
                color=blue, 
                label='Job')

    ax.set_xlim(left=(xs[0] - 0.5), right=(xs[-1] + 0.5))
    ax.set_ylabel('Transfer Data Rate /MBps', fontsize=18)
    ax.set_xlabel('Time /seconds', fontsize=18)
    # ax.set_ylim(0, 500)

    # plot util text

    for a,b in zip(xs,sizes):
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

    lines = line
    labels = [l.get_label() for l in lines]
    ax.legend(lines, labels, loc=1, fontsize=18, 
            bbox_to_anchor=(0., 1.02, 1., .102), 
            ncol=3, mode="expand", borderaxespad=0., 
            frameon=False)

    print(np.mean(sizes))
    plt.savefig(dir + "ops-rate-" + str(id) + ".pdf")

for key in jobs.keys():
    draw(key, jobs[key])