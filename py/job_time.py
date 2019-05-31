
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
filename = dir + jobId + "/report_time"
outputTmp = dir + jobId + "/job_time"
outputFigMap = dir + jobId + "/map_time.pdf"
outputFigReduce = dir + jobId + "/reduce_time.pdf"
outputFigShuffle = dir + jobId + "/shuffle_time.pdf"

fi = open(filename)

map_start = {}
map_stop = {}
reduce_start = {}
reduce_stop = {}
shuffle_start = {}
shuffle_stop = {}

for line in fi:
    args = line.split("-")
    if args[3] == "map" :
        if args[4] == "start\n" :
            time  = int(args[1]) / 1000
            if not map_start.has_key(time):
                    map_start[time] = 1
            else:
                map_start[time] = map_start[time] + 1
        elif args[4] == "stop\n":
            time  = int(args[1]) / 1000
            if not map_stop.has_key(time):
                    map_stop[time] = 1
            else:
                map_stop[time] = map_stop[time] + 1
    elif args[3] == "reduce" :
        if args[4] == "start\n":
            time  = int(args[1]) / 1000
            if not reduce_start.has_key(time):
                    reduce_start[time] = 1
            else:
                reduce_start[time] = reduce_start[time] + 1
        elif args[4] == "stop\n":
            time  = int(args[1]) / 1000
            if not reduce_stop.has_key(time):
                    reduce_stop[time] = 1
            else:
                reduce_stop[time] = reduce_stop[time] + 1
    elif args[3] == "shuffle" :
        if args[4] == "start\n":
            time  = int(args[1]) / 1000
            if not shuffle_start.has_key(time):
                    shuffle_start[time] = 1
            else:
                shuffle_start[time] = shuffle_start[time] + 1
        elif args[4] == "stop\n":
            time  = int(args[1]) / 1000
            if not shuffle_stop.has_key(time):
                    shuffle_stop[time] = 1
            else:
                shuffle_stop[time] = shuffle_stop[time] + 1

fi.close()

# map_start.sort()
# map_stop.sort()
# reduce_start.sort()
# reduce_stop.sort()
# shuffle_start.sort()
# shuffle_stop.sort()

start = map_start.keys()
end = reduce_stop.keys()
start.sort()
end.sort()
job_time = end[-1] - start[0]
print (job_time)

map_start_line = []
map_stop_line = []
start = map_start.keys()
stop = map_stop.keys()
start.sort()
stop.sort()
job_start = start[0]
gap = stop[0] - start[0]
for time in start:
    map_start_line.append(map_start[time])
for i in range(gap):
    map_stop_line.append(0)
for time in stop:
    map_stop_line.append(map_stop[time])
for i in range(len(map_stop_line) - len(map_start_line)):
    map_start_line.append(0)


fig, ax = plt.subplots(figsize=(12,5))
width = 8

xs = np.arange(len(map_start_line))

line_map = ax.plot(xs, map_start_line, 
            linewidth=3,
            marker="s",
            color=blue, 
            label='Map Start')
line_map_stop = ax.plot(xs, map_stop_line, 
            linewidth=3,
            marker="s",
            color=orange, 
            label='Map Stop')

ax.set_xlim(left=(xs[0]), right=(xs[-1] + 5))
ax.set_ylabel('Number of Tasks', fontsize=18)
ax.set_xlabel('Time /seconds', fontsize=18)
# ax.set_ylim(0, 30)

for a,b in zip(xs,map_start_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)
for a,b in zip(xs,map_stop_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

lines = line_map + line_map_stop
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)

plt.savefig(outputFigMap)




reduce_start_line = []
reduce_stop_line = []
start = reduce_start.keys()
stop = reduce_stop.keys()
start.sort()
stop.sort()
job_gap = start[0] - job_start
gap = stop[0] - start[0]
for i in range(job_gap):
    reduce_stop_line.append(0)
    reduce_start_line.append(0)
for time in start:
    reduce_start_line.append(reduce_start[time])
for i in range(gap):
    reduce_stop_line.append(0)
for time in stop:
    reduce_stop_line.append(reduce_stop[time])
for i in range(len(reduce_stop_line) - len(reduce_start_line)):
    reduce_start_line.append(0)


fig, ax = plt.subplots(figsize=(12,5))
width = 8

xs = np.arange(len(reduce_start_line))

line_reduce = ax.plot(xs, reduce_start_line, 
            linewidth=3,
            marker="s",
            color=blue, 
            label='Reduce Start')
line_reduce_stop = ax.plot(xs, reduce_stop_line, 
            linewidth=3,
            marker="s",
            color=orange, 
            label='Reduce Stop')

ax.set_xlim(left=(xs[0]), right=(xs[-1] + 5))
ax.set_ylabel('Number of Tasks', fontsize=18)
ax.set_xlabel('Time /seconds', fontsize=18)
# ax.set_ylim(0, 30)

for a,b in zip(xs,reduce_start_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)
for a,b in zip(xs,reduce_stop_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

lines = line_reduce + line_reduce_stop
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)

plt.savefig(outputFigReduce)


shuffle_start_line = []
shuffle_stop_line = []
start = shuffle_start.keys()
stop = shuffle_stop.keys()
start.sort()
stop.sort()
job_gap = start[0] - job_start
gap = stop[0] - start[0]
for i in range(job_gap):
    shuffle_stop_line.append(0)
    shuffle_start_line.append(0)
for time in start:
    shuffle_start_line.append(shuffle_start[time])
for i in range(gap):
    shuffle_stop_line.append(0)
for time in stop:
    shuffle_stop_line.append(shuffle_stop[time])
for i in range(len(shuffle_stop_line) - len(shuffle_start_line)):
    shuffle_start_line.append(0)


fig, ax = plt.subplots(figsize=(12,5))
width = 8

xs = np.arange(len(shuffle_start_line))

line_shuffle = ax.plot(xs, shuffle_start_line, 
            linewidth=3,
            marker="s",
            color=blue, 
            label='Shuffle Start')
line_shuffle_stop = ax.plot(xs, shuffle_stop_line, 
            linewidth=3,
            marker="s",
            color=orange, 
            label='Shuffle Stop')

ax.set_xlim(left=(xs[0]), right=(xs[-1] + 5))
ax.set_ylabel('Number of Tasks', fontsize=18)
ax.set_xlabel('Time /seconds', fontsize=18)
# ax.set_ylim(0, 30)

for a,b in zip(xs,shuffle_start_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)
for a,b in zip(xs,shuffle_stop_line):
        if b == 0: continue
        plt.text(a, b+0.5, b, ha='center', va= 'bottom',fontsize=12)

lines = line_shuffle + line_shuffle_stop
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc=1, fontsize=18, 
        bbox_to_anchor=(0., 1.02, 1., .102), 
        ncol=3, mode="expand", borderaxespad=0., 
        frameon=False)

plt.savefig(outputFigShuffle)