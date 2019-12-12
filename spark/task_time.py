
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

if len(sys.argv) <= 3 :
    exit ("Lack of args.")
jobId = sys.argv[1]
stageNum = sys.argv[2]
rounds = int(sys.argv[3])

dir = "./spark/"
filename = dir + jobId + "/spark.log"
outputTmp = dir + jobId + "/job_time"
outputFig = dir + jobId + "/task_time.pdf"

jobStart = 0
jobStop = 0
jobTime = 0

bars = []

def pre_compute():
    global jobStart
    global jobStop
    global jobTime
    fi = open(filename)
    mapEndTimes = []
    reduceEndTimes = []
    startTimes = []
    for line in fi:
        args = line.split("-")
        if len(args) < 6:
            continue
        startTimes.append(int(args[6]) / 1000)
        if args[1] == "Map" :
            mapEndTimes.append(int(args[8]) / 1000)
        elif args[1] == "Reduce" :
            reduceEndTimes.append(int(args[10]) / 1000)
    fi.close()
    startTimes.sort()
    mapEndTimes.sort()
    reduceEndTimes.sort()
    jobStart = startTimes[0]
    jobStop = reduceEndTimes[-1]
    mapStop = mapEndTimes[-1]
    jobTime = jobStop - jobStart
    mapTime = mapStop - jobStart
    reduceTime = jobStop - mapStop
    print ("Job Start timestamp:" + str(jobStart))
    print ("Job time: " + str(jobTime))
    print ("Map time: " + str(mapTime))
    print ("Reduce time: " + str(reduceTime))

def compute(stageNum):
    fi = open(filename)
    taskType = 0
    mapTaskTime = []
    reduceTaskTime = []
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
        if len(args) < 6:
            continue
        if args[2] != str(stageNum):
            continue
        if args[1] == "Map" :
            start = int(args[6]) / 1000 - jobStart
            sortStart = int(args[7]) / 1000 - jobStart
            stop = int(args[8]) / 1000 - jobStart
            spillTime = int(args[9]) / 1000
            mapTaskTime.append(int(args[8]) / 1000 - int(args[6]) / 1000)
            mapGap.append(start)
            # mapBar.append(sortStart - start)
            # mapSortGap.append(sortStart)
            # mapSortBar.append(stop - sortStart)
            mapBar.append(stop - spillTime - start)
            mapSortGap.append(stop - spillTime)
            mapSortBar.append(spillTime)
            taskType = 1
        elif args[1] == "Reduce" :
            start = int(args[7]) / 1000 - jobStart
            sortStart = int(args[8]) / 1000 - jobStart
            reduceStart = int(args[9]) / 1000 - jobStart
            stop = int(args[10]) / 1000 - jobStart
            spillTime = int(args[11]) / 1000
            reduceTaskTime.append(int(args[10]) / 1000 - int(args[7]) / 1000)
            copyGap.append(start)
            # copyBar.append(reduceStart - spillTime - start)
            copyBar.append(reduceStart - start) # no spill time
            reduceSortGap.append(reduceStart - spillTime)
            reduceSortBar.append(spillTime)
            reduceGap.append(reduceStart)
            reduceBar.append(stop - reduceStart)
            taskType = 2

    fi.close()
    if taskType == 1:
        tmp = np.asarray(mapSortBar)
        tmpMean = np.mean(tmp)
        newSortBar = []
        for bar in mapSortBar:
            if bar < tmpMean * 2:
                newSortBar.append(bar)
        sort = np.asarray(newSortBar)
        # print("Map sort time: " + str(np.mean(sort)) + " s")
        base = np.mean(mapTaskTime)
        tmp = []
        for i in range(len(mapTaskTime)):
            if mapTaskTime[i] > base * 2:
                continue
            tmp.append(mapTaskTime[i])
        print ("Average map task time: " + str(np.mean(tmp)) + " s")
        return ("Map", mapBar, mapGap, mapSortBar, mapSortGap)
    elif taskType == 2:
        copy = np.asarray(copyBar)
        sort = np.asarray(reduceSortBar)
        red = np.asarray(reduceBar)
        print ("Copy time: " + str(np.mean(copy)) + " s")
        print ("Sort time: " + str(np.mean(sort)) + " s")
        print ("Total Copy time: " + str(np.sum(copy)) + " s")
        print ("Sort len: " + str(len(copy)) + " s")
        print ("Reduce time: " + str(np.mean(red)) + " s")
        print ("Average reduce task time: " + str(np.mean(reduceTaskTime)) + " s")
        return ("Reduce", copyGap, copyBar, reduceSortGap, reduceSortBar, reduceGap, reduceBar)
    
    return ()

def draw(data, ax):
    global bars

    if len(data) == 0:
        print ("Wrong stage.")
        return
    if data[0] == "Map":
        mapBar = data[1]
        mapGap = data[2]
        mapSortBar = data[3]
        mapSortGap = data[4]
        width = 1
        mxs = np.arange(len(mapBar))
        bar = ax.barh(mxs, mapBar, width,
                left=mapGap,
                linewidth=0, color=blue, 
                edgecolor=blue, hatch="++++",
                label='Map')
        # ax.barh(mxs, mapSortBar, width,
        #         left=mapSortGap,
        #         linewidth=0, color=red, 
        #         edgecolor=blue, hatch="++++",
        #         label='MapSort')
        ax.set_ylim(bottom=-(len(mapBar)/10), top=len(mapBar) + (len(mapBar)/10))
        bars += bar
    elif data[0] == "Reduce":
        copyGap = data[1]
        copyBar = data[2]
        reduceSortGap = data[3]
        reduceSortBar = data[4]
        reduceGap = data[5]
        reduceBar = data[6]
        global rounds

        width = 1
        xs = np.arange(len(reduceBar)) * rounds
        # xs = np.arange(len(reduceBar))
        bar1 = ax.barh(xs, copyBar, width,
                left=copyGap,
                linewidth=0, color=orange, 
                edgecolor=orange, hatch="++++",
                label='Shuffle')
        # ax.barh(xs, reduceSortBar, width,
        #         left=reduceSortGap,
        #         linewidth=0, color=red, 
        #         edgecolor=green, hatch="++++",
        #         label='ReduceSort')
        bar2 = ax.barh(xs, reduceBar, width,
                left=reduceGap,
                linewidth=0, color=green, 
                edgecolor=green, hatch="++++",
                label='Reduce')
        bars += bar1
        bars += bar2


pre_compute()
fig, ax = plt.subplots()
for i in range(int(stageNum)):
    rets = compute(i)
    draw(rets, ax)
# ax.set_ylim(bottom=-10, top=len(mapBar) + 20)
ax.set_ylabel('Task', fontsize=20)
ax.set_xlabel('Time(sec)', fontsize=20)

labels = [l.get_label() for l in bars]
ax.legend(loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)
print(len(bars))
plt.savefig(outputFig)


# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))