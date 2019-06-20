
import os, sys
import matplotlib.pyplot as plt
import numpy as np
import collections


orange = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'
red = '#A00000'

if len(sys.argv) <= 2 :
    exit ("Lack of args.")
jobId = sys.argv[1]
rounds = int(sys.argv[2])

dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report"
outputTmp = dir + jobId + "/job_time"
outputFig = dir + jobId + "/task_time.pdf"

fi = open(filename)

endTimes = []
startTimes = []
mapBar = []
mapGap = []
mapSortBar = []
mapSortGap = []
copyBar = []
copyGap = []
reduceSortBar = []
reduceSortGap = []
reduceBar = []
reduceGap = []

for line in fi:
    args = line.split("-")
    time = int(args[3]) / 1000
    startTimes.append(time)
    if args[1] == "mapTask" :
        time += int(args[4]) / 1000
        time += int(args[5]) / 1000
    elif args[1] == "reduceTask" :
        time += int(args[4]) / 1000
        time += int(args[5]) / 1000
        time += int(args[6]) / 1000
    endTimes.append(time)

endTimes.sort()
startTimes.sort()
jobStart = startTimes[0]
jobStop = endTimes[-1]
jobTime = jobStop - jobStart
print (jobTime)

fi.seek(0)
for line in fi:
    args = line.split("-")
    if args[1] == "mapTask" :
        begin = int(args[3]) / 1000 - jobStart
        mapTime = int(args[4]) / 1000
        mapSortTime = int(args[5]) / 1000
        mapGap.append(begin)
        mapBar.append(mapTime)
        mapSortGap.append(begin + mapTime)
        mapSortBar.append(mapSortTime)
    elif args[1] == "reduceTask" :
        begin = int(args[3]) / 1000 - jobStart
        reduceCopyTime = int(args[4]) / 1000
        reduceSortTime = int(args[5]) / 1000
        reduceTime = int(args[6]) / 1000
        copyGap.append(begin)
        copyBar.append(reduceCopyTime)
        reduceSortGap.append(begin + reduceCopyTime)
        reduceSortBar.append(reduceSortTime)
        reduceGap.append(begin + reduceCopyTime + reduceSortTime)
        reduceBar.append(reduceTime)

fi.close()

print ("Map Task Number: " + str(len(mapBar)))
print ("Reduce Task Number: " + str(len(reduceBar)))


# fig, ax = plt.subplots(figsize=(12,12))
fig, ax = plt.subplots()
width = 1
mxs = np.arange(len(mapBar))
ax.barh(mxs, mapBar, width,
        left=mapGap,
        linewidth=0, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Map')
ax.barh(mxs, mapSortBar, width,
        left=mapSortGap,
        linewidth=0, color=red, 
        edgecolor=blue, hatch="++++",
        label='MapSort')

xs = np.arange(len(reduceBar)) * rounds
ax.barh(xs, copyBar, width,
        left=copyGap,
        linewidth=0, color=orange, 
        edgecolor=orange, hatch="++++",
        label='Copy')
ax.barh(xs, reduceSortBar, width,
        left=reduceSortGap,
        linewidth=0, color=red, 
        edgecolor=green, hatch="++++",
        label='ReduceSort')
ax.barh(xs, reduceBar, width,
        left=reduceGap,
        linewidth=0, color=green, 
        edgecolor=green, hatch="++++",
        label='Reduce')

# ax.set_xticks(np.arange(10) * len(test) * 2)
# ax.set_xlim(right=(xs[-1] + 20))
# ax.set_xticklabels(np.arange(10) *len(test)/10)
# ax.set_ylim(bottom=-10, top=800)
ax.set_ylim(bottom=-10, top=mxs[-1] + 20)
ax.set_ylabel('Task', fontsize=12)
ax.set_xlabel('Time (s)', fontsize=12)

plt.savefig(outputFig)