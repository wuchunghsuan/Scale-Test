
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

def pre_compute():
    global jobStart
    global jobStop
    global jobTime
    fi = open(filename)
    endTimes = []
    startTimes = []
    for line in fi:
        args = line.split("-")
        startTimes.append(int(args[6]) / 1000)
        if args[1] == "Map" :
            endTimes.append(int(args[8]) / 1000)
        elif args[1] == "Reduce" :
            endTimes.append(int(args[10]) / 1000)
    fi.close()
    startTimes.sort()
    endTimes.sort()
    jobStart = startTimes[0]
    jobStop = endTimes[-1]
    jobTime = jobStop - jobStart
    print ("Job start: " + str(jobStart))
    print ("Job stop: " + str(jobStop))
    print ("Job time: " + str(jobTime))

def compute(stageNum):
    fi = open(filename)
    taskType = 0
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
        if args[2] != str(stageNum):
            continue
        if args[1] == "Map" :
            start = int(args[6]) / 1000 - jobStart
            SortStart = int(args[7]) / 1000 - jobStart
            stop = int(args[8]) / 1000 - jobStart
            spillTime = int(args[9]) / 1000
            mapGap.append(start)
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
            copyGap.append(start)
            copyBar.append(reduceStart - spillTime - start)
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
        print("Map sort time: " + str(np.mean(sort)) + " s")
        return ("Map", mapBar, mapGap, mapSortBar, mapSortGap)
    elif taskType == 2:
        copy = np.asarray(copyBar)
        sort = np.asarray(reduceSortBar)
        red = np.asarray(reduceBar)
        print ("Copy time: " + str(np.mean(copy)) + " s")
        print ("Sort time: " + str(np.mean(sort)) + " s")
        print ("Reduce time: " + str(np.mean(red)) + " s")
        return ("Reduce", copyGap, copyBar, reduceSortGap, reduceSortBar, reduceGap, reduceBar)
    
    return ()

def draw(data, ax):
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
        ax.set_ylim(bottom=-(len(mapBar)/10), top=len(mapBar) + (len(mapBar)/10))
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


pre_compute()
fig, ax = plt.subplots()
for i in range(int(stageNum)):
    rets = compute(i)
    draw(rets, ax)
# ax.set_ylim(bottom=-10, top=len(mapBar) + 20)
ax.set_ylabel('Task', fontsize=12)
ax.set_xlabel('Time (s)', fontsize=12)

plt.savefig(outputFig)


# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))