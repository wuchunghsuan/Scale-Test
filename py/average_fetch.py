
import os, sys
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

dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report_fetch"
# dir = "/Users/admin/Downloads/wuchunghsuan/report-scale-test-2/"
# filename = dir + "report-fetch-" + jobId
outputTmp = dir + jobId + "/fetch.tmp"
outputFig = dir + jobId + "/fetch_distribution.pdf"
# output = dir + jobId + "/fig_fetch_avg_rate.pdf"
# outputTmp = dir + jobId + "/fetch.tmp"
# os.mkdir(dir + jobId)
fi = open(filename)

times = []
sizes = []
rates = []
rates0 = []
rates1 = []
rates2 = []
rates3 = []
rates4 = []
count = 0

for line in fi:
    args = line.split()
    if len(args) == 0 or int(args[1]) < 10:
        continue
    times.append(float(args[1]))
    sizes.append(float(args[2]))
    if float(args[3]) < 1:
        rates0.append(float(args[3]))
    elif float(args[3]) < 10:
        rates1.append(float(args[3]))
    elif float(args[3]) < 20:
        rates2.append(float(args[3]))
    elif float(args[3]) < 30:
        rates3.append(float(args[3]))
    else:
        rates4.append(float(args[3]))
    rates.append(float(args[3]))
    count += 1

fi.close()

bars = []
bars.append(len(rates0))
bars.append(len(rates1))
bars.append(len(rates2))
bars.append(len(rates3))
bars.append(len(rates4))

percent = []
for i in bars:
    percent.append('%.2f%%' % (i*100.0/count))
times = np.asarray(times)
sizes = np.asarray(sizes)
rates = np.asarray(rates)

sizes = sizes / 1024

print ("Log count: " + str(count))
print ("Average time: " + str(np.mean(times)) + " mills")
print ("Average size: " + str(np.mean(sizes)) + " KB")
print ("Average rate: " + str(np.mean(rates)) + " MBps")
print ("Rate variance: " + str(np.std(rates)))
print (percent)

fo = open(outputTmp, "w")

fo.write(str(np.mean(times)) + "\t" + str(np.mean(sizes)) + "\t" + str(np.mean(rates)) + "\n")
for p in percent:
    fo.write(p + "\t")

fo.close()

fig, ax = plt.subplots()
width = 1

xs = np.arange(5) * 2

ax.bar(xs, bars, width, 
        linewidth=1, color=blue, 
        edgecolor=blue, hatch="++++",
        label='Transfer Rate')
ax.set_xticks(np.arange(5) * 2)
ax.set_xlim(left=(xs[0] - 0.5), right=(xs[-1] + 1.5))
ax.set_xticklabels(["<1","1~10","10~20","20~30", ">30"])
# ax.set_ylim(top=30)
# ax.legend(loc=4, fontsize=16, frameon=False)
ax.set_ylabel('Number', fontsize=12)
ax.set_xlabel('Transfer Rate (MB/s)', fontsize=12)
# ax.set_aspect(0.23 / ax.get_data_ratio())
# plt.legend(loc=2, fontsize=24, frameon=False)

for a,b in zip(xs, bars):
    plt.text(a+0.5, b+0.5, b, ha='center', va= 'bottom',fontsize=8)

plt.savefig(outputFig)




