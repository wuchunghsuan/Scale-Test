
import sys
import numpy as np

if len(sys.argv) <= 1 :
    print ("Lack of Job ID.")
jobId = sys.argv[1]

dir = "/home/wuchunghsuan/report-scale-test/"
filename = dir + jobId + "/report_fetch"
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

fo = open("output", "w")

fo.close()




