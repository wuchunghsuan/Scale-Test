
import sys
import matplotlib.pyplot as plt
import numpy as np


orage = '#FF8C00'
light_orange = '#FFA500'
blue = '#4682B4'
green = '#2E8B57'
light_blue = '#87CEFA'

if len(sys.argv) <= 1 :
    exit ("Lack of Job ID.")
jobId = sys.argv[1]

dir = "/home/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report"
output = dir + jobId + "/fig_avg_rate.pdf"
outputTmp = dir + jobId + "/report.tmp"
outputMap = dir + jobId + "/fig_map_avg_time.pdf"
outputReduce = dir + jobId + "/fig_reduce_avg_time.pdf"
outputShuffle = dir + jobId + "/fig_shuffle_avg_time.pdf"
# outputMap = "./fig_map_avg_time.pdf"
# outputReduce = "./fig_reduce_avg_time.pdf"
# outputShuffle = "./fig_shuffle_avg_time.pdf"
# filename = "./report"
# outputTmp = "./report.tmp"
fi = open(filename)

reduces = []
maps = []
s_times = []
s_sizes = []
count = 0

for line in fi:
    args = line.split()
    if len(args) == 0:
        continue
    if args[0] == "Reduce" :
        reduces.append(float(args[2]))
    if args[0] == "Map" :
        maps.append(float(args[2]))
    if args[0] == "Shuffle" :
        s_sizes.append(float(args[2]))
        s_times.append(float(args[3]))
    count += 1

fi.close()

reduces = np.asarray(reduces)
maps = np.asarray(maps)
s_times = np.asarray(s_times)
s_sizes = np.asarray(s_sizes)

reduces = reduces / 1000
maps = maps / 1000
s_times = s_times / 1000
s_sizes = s_sizes / 1024/ 1024

print ("Log count: " + str(count))
print ("Average map time: " + str(np.mean(maps)) + " seconds")
print ("Average reduce time: " + str(np.mean(reduces)) + " seconds")
print ("Average shuffle time: " + str(np.mean(s_times)) + " seconds")
print ("Average shuffle size: " + str(np.mean(s_sizes)) + " MB")

fo = open(outputTmp, "w")

fo.write(str(np.mean(maps)) + "\t" + str(np.mean(reduces)) + "\t" + str(np.mean(s_times)) + "\t" + str(np.mean(s_sizes)))

fo.close()

# Map fig
fig, ax = plt.subplots()
width = 8
xs = np.arange(len(maps)) * 20
ax.bar(xs, maps, width, 
        linewidth=1, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Transfer Rate')
ax.set_xticks(np.arange(10) * len(maps) * 2)
ax.set_xlim(right=(xs[-1] + 20))
ax.set_xticklabels(np.arange(10) *len(maps)/10)
ax.set_ylim(top=15)
ax.set_ylabel('Average Map Time (s)', fontsize=12)
ax.set_xlabel('Map', fontsize=12)

plt.savefig(outputMap)

# Reduce fig
fig, ax = plt.subplots()
width = 8
xs = np.arange(len(reduces)) * 20
ax.bar(xs, reduces, width, 
        linewidth=1, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Transfer Rate')
ax.set_xticks(np.arange(10) * len(reduces) * 2)
ax.set_xlim(right=(xs[-1] + 20))
ax.set_xticklabels(np.arange(10) *len(reduces)/10)
ax.set_ylim(top=30)
ax.set_ylabel('Average Reduce Time (s)', fontsize=12)
ax.set_xlabel('Reduce', fontsize=12)

plt.savefig(outputReduce)

# Shuffle fig
fig, ax = plt.subplots()
width = 8
xs = np.arange(len(s_times)) * 20
ax.bar(xs, s_times, width, 
        linewidth=1, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Transfer Rate')
ax.set_xticks(np.arange(10) * len(s_times) * 2)
ax.set_xlim(right=(xs[-1] + 20))
ax.set_xticklabels(np.arange(10) *len(s_times)/10)
ax.set_ylim(top=15)
ax.set_ylabel('Average Shuffle Time (s)', fontsize=12)
ax.set_xlabel('Shuffle', fontsize=12)

plt.savefig(outputShuffle)



