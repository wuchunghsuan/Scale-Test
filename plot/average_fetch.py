
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
filename = dir + jobId + "/report_fetch"
output = dir + jobId + "/fig_fetch_avg_rate.pdf"
outputTmp = dir + jobId + "/fetch.tmp"
# outputFig = "./fig_fetch_avg_rate.pdf"
# filename = "./report_fetch"
fi = open(filename)

times = []
sizes = []
rates = []
count = 0

for line in fi:
    args = line.split()
    if len(args) == 0 or int(args[1]) < 10:
        continue
    times.append(float(args[1]))
    sizes.append(float(args[2]))
    rates.append(float(args[3]))
    count += 1

fi.close()

times = np.asarray(times)
sizes = np.asarray(sizes)
rates = np.asarray(rates)

sizes = sizes / 1024

print ("Log count: " + str(count))
print ("Average time: " + str(np.mean(times)) + " mills")
print ("Average size: " + str(np.mean(sizes)) + " KB")
print ("Average rate: " + str(np.mean(rates)) + " MBps")

fo = open(outputTmp, "w")

fo.write(str(np.mean(times)) + "\t" + str(np.mean(sizes)) + "\t" + str(np.mean(rates)))

fo.close()

# fig, ax = plt.subplots()
# width = 8

# xs = np.arange(len(rates)) * 20

# ax.bar(xs, rates, width, 
#         linewidth=1, color=blue, 
#         edgecolor=blue, hatch="++++",
#         label='Transfer Rate')
# ax.set_xticks(np.arange(10) * len(rates) * 2)
# ax.set_xlim(right=(xs[-1] + 20))
# ax.set_xticklabels(np.arange(10) *len(rates)/10)
# ax.set_ylim(top=30)
# # ax.legend(loc=4, fontsize=16, frameon=False)
# ax.set_ylabel('Transfer Rate (MB/s)', fontsize=12)
# ax.set_xlabel('Fetcher', fontsize=12)
# # ax.set_aspect(0.23 / ax.get_data_ratio())
# # plt.legend(loc=2, fontsize=24, frameon=False)

# plt.savefig(outputFig)
# size = fig.get_size_inches()
# print (size)




