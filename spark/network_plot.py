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
jobStart = int(sys.argv[2])

dir = "./spark/" + jobId + "/spark"
monitorFile = dir + "/network.log"
timeFile = dir + "/network_time.log"
outputFig = dir + "/network_plot.pdf"

def compute():
    data = []
    fi = open(monitorFile)
    for line in fi:
        data.append(int(line))
    fi.close()
    time = []
    fi = open(timeFile)
    for line in fi:
        time.append(int(line))
    fi.close()
    print(data)
    print(time)
    if len(data) != len(time):
        print("Wrong data!")
    throughput = []
    start = time[0]
    index = 0
    for i in range(len(data)):
        # tmp = (time[i] - start) / 5
        tmp = (time[i] - jobStart) / 5
        if tmp < 0:
            continue
        if index < tmp:
            index = tmp
        # print(tmp)
        while len(throughput) <= index:
            throughput.append(data[i])
        throughput[index] += data[i]
    print(len(throughput))
    return throughput

def draw(throughput):
    x = np.arange(len(throughput)) * 5

    # the histogram of the data
    # plt.hist(requestBar)
    plt.plot(x, throughput)

    plt.xlabel('Time(s)')
    plt.ylabel('Throughput(MB/s)')
    plt.title('Shuffle Request Count and Network Throughput in a Spark Application')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.xlim(0, 80)
    # plt.ylim(0, 0.03)
    plt.grid(True)
    # plt.show()
    plt.savefig(outputFig)

requestBar = compute()
# requestBar = compute_delete(requestBar)
draw(requestBar)




# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))