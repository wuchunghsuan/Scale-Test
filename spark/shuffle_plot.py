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
jobStart = sys.argv[2]

dir = "./spark/" + jobId
requestFile = dir + "/request.log"
monitorFile = dir + "/spark/network.log"
timeFile = dir + "/spark/network_time.log"
diskFile = dir + "/spark/disk.log"
diskTimeFile = dir + "/spark/disk_time.log"
outputFig = dir + "/shuffle_plot.png"
outputFig2 = dir + "/shuffle_request_bar.jpg"

label_size=20

def compute_throughput():
    data = []
    fi = open(monitorFile)
    for line in fi:
        data.append(float(line) / 1000000000 / 5)
    fi.close()
    time = []
    fi = open(timeFile)
    for line in fi:
        time.append(int(line))
    fi.close()
    # print(data)
    # print(time)
    if len(data) != len(time):
        print("Wrong data!")
    throughput = []
    start = time[0]
    index = 0
    for i in range(len(data)):
        # tmp = (time[i] - start) / 5
        tmp = (time[i] - int(jobStart)) / 5
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

def compute_disk():
    data = []
    fi = open(diskFile)
    for line in fi:
        data.append(float(line) / 1000000000 / 5)
    fi.close()
    time = []
    fi = open(diskTimeFile)
    for line in fi:
        time.append(int(line))
    fi.close()
    # print(data)
    # print(time)
    if len(data) != len(time):
        print("Wrong data!")
    disk = []
    start = time[0]
    index = 0
    for i in range(len(data)):
        # tmp = (time[i] - start) / 5
        tmp = (time[i] - int(jobStart)) / 5
        if tmp < 0:
            continue
        if index < tmp:
            index = tmp
        # print(tmp)
        while len(disk) <= index:
            disk.append(data[i])
        disk[index] += data[i]
    print(len(disk))
    return disk

def compute_request():
    requestBar = []
    fi = open(requestFile)
    for line in fi:
        args = line.split("-")
        if len(args) < 4:
            print("Wrong line!")
            continue
        time = int(args[3])/1000 - int(jobStart)
        if time > 10000 or time < 0:
            print("Wrong time!")
            continue
        while len(requestBar) <= time:
            requestBar.append(0)
        requestBar[time] += 1
    fi.close()
    print(len(requestBar))
    return requestBar

def draw(requestBar, throughput, disk):
    x = np.arange(len(requestBar))

    # the histogram of the data
    # plt.hist(requestBar)
    fig, ax2 = plt.subplots(figsize=(12,5))
    plt.xlim(0, 400)
    # plt.ylim(0, 30)
    plt.grid(True)

    disk_x = np.arange(len(disk)) * 5
    ax2.plot(disk_x, disk, 
        # ls='--',
        marker="s",
        color=green,
        lw=3,
        label="Disk I/O")


    x2 = np.arange(len(throughput)) * 5
    ax2.plot(x2, throughput, color=orange,marker="s", lw=3, label="Network I/O")
    ax2.set_ylabel('Throughput(GB/s)',size=label_size)
    ax2.set_xlabel('Time(sec)',size=label_size)
    # ax2.tick_params(axis='y', labelcolor=orange)
    plt.legend()
    ax2.set_xlim(0, 400)
    ax2.set_ylim(0, 6.5)
    plt.savefig(outputFig)

    plt.close()

    # ax1 = ax2.twinx()
    # ax1 = plt.subplot(212)
    fig, ax1 = plt.subplots(figsize=(12,5))
    # ax1.plot(x, requestBar)
    ax1.bar(x, requestBar, 1,
                linewidth=0, color=blue, 
                edgecolor=blue, hatch="++++",
                label='Shuffle Request Count')
    ax1.set_xlabel('Time(sec)',size=label_size)
    ax1.set_ylabel('Shuffle Request Count',size=label_size)
    # ax1.tick_params(axis='y', labelcolor=blue)
    plt.grid(True)
    plt.legend()
    ax1.set_xlim(0, 400)
    ax1.set_ylim(0, 600)

    

    # fig.tight_layout()
    # plt.show()
    plt.savefig(outputFig2)

requestBar = compute_request()
throughput = compute_throughput()
disk = compute_disk()
# requestBar = compute_delete(requestBar)
draw(requestBar, throughput, disk)




# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))