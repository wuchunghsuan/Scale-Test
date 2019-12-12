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
outputFig = dir + "/request_plot.pdf"

def compute_create():
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
    print(requestBar)
    return requestBar

def draw(requestBar):
    x = np.arange(len(requestBar))

    # the histogram of the data
    # plt.hist(requestBar)
    plt.plot(x, requestBar)

    plt.xlabel('Time(s)')
    plt.ylabel('Shuffle Request Count')
    plt.title('Shuffle Request Count and Network Throughput in a Spark Application')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.xlim(0, 80)
    # plt.ylim(0, 0.03)
    plt.grid(True)
    # plt.show()
    plt.savefig(outputFig)

requestBar = compute_create()
# requestBar = compute_delete(requestBar)
draw(requestBar)




# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))