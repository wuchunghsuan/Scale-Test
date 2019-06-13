
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import collections


orange = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'

if len(sys.argv) <= 1 :
    exit ("Lack of Job ID.")
jobId = sys.argv[1]

dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report_time"
outputTmp = dir + jobId + "/job_time"
outputFig = dir + jobId + "/task_time.pdf"

fi = open(filename)

allTimes = []
mapStart = collections.OrderedDict()
mapStop = collections.OrderedDict()
reduceStart = collections.OrderedDict()
reduceStop = collections.OrderedDict()
shuffleStart = collections.OrderedDict()
shuffleStop = collections.OrderedDict()

for line in fi:
    args = line.split("-")
    if args[3] == "map" :
        key = args[2].split("_")[4]
        time = int(args[1]) / 1000
        allTimes.append(time)
        if args[4] == "start\n" :
                mapStart[key] = time
        elif args[4] == "stop\n" :
                mapStop[key] = time
    elif args[3] == "reduce" :
        key = args[2].split("_")[4]
        time = int(args[1]) / 1000
        allTimes.append(time)
        if args[4] == "start\n" :
                reduceStart[key] = time
        elif args[4] == "stop\n" :
                reduceStop[key] = time
    elif args[3] == "shuffle" :
        key = args[2].split("_")[4]
        time = int(args[1]) / 1000
        allTimes.append(time)
        if args[4] == "start\n" :
                shuffleStart[key] = time
        elif args[4] == "stop\n" :
                shuffleStop[key] = time

fi.close()

# map_start.sort()
# map_stop.sort()
# reduce_start.sort()
# reduce_stop.sort()
# shuffle_start.sort()
# shuffle_stop.sort()

allTimes.sort()
jobStart = allTimes[0]
jobStop = allTimes[-1]
jobTime = jobStop - jobStart
print (jobTime)

print ("Map Task Number: " + str(len(mapStart.keys())))
mapBar = []
mapGap = []
for key in mapStart.keys() :
    time = mapStop[key] - mapStart[key]
    mapBar.append(time)
    mapGap.append(mapStart[key] - jobStart)

print ("Reduce Task Number: " + str(len(reduceStart.keys())))
reduceBar = []
reduceGap = []
for key in reduceStart.keys() :
    time = reduceStop[key] - reduceStart[key]
    reduceBar.append(time)
    reduceGap.append(reduceStart[key] - jobStart)

print ("Shuffle Task Number: " + str(len(reduceStart.keys())))
shuffleBar = []
shuffleGap = []
for key in shuffleStart.keys() :
    time = shuffleStop[key] - shuffleStart[key]
    shuffleBar.append(time)
    shuffleGap.append(shuffleStart[key] - jobStart)

# fig, ax = plt.subplots(figsize=(12,12))
fig, ax = plt.subplots()
width = 1
mxs = np.arange(len(mapBar))
ax.barh(mxs, mapBar, width,
        left=mapGap,
        linewidth=0, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Map')
xs = np.arange(len(reduceBar)) * 4
ax.barh(xs, reduceBar, width,
        left=reduceGap,
        linewidth=0, color=green, 
        edgecolor=green, hatch="++++",
        label='Reduce')
xs = np.arange(len(shuffleBar)) * 4
ax.barh(xs, shuffleBar, width,
        left=shuffleGap,
        linewidth=0, color=orange, 
        edgecolor=orange, hatch="++++",
        label='Shuffle')

# ax.set_xticks(np.arange(10) * len(test) * 2)
# ax.set_xlim(right=(xs[-1] + 20))
# ax.set_xticklabels(np.arange(10) *len(test)/10)
# ax.set_ylim(bottom=-10, top=800)
ax.set_ylim(bottom=-10, top=mxs[-1] + 20)
ax.set_ylabel('Task', fontsize=12)
ax.set_xlabel('Time (s)', fontsize=12)

plt.savefig(outputFig)