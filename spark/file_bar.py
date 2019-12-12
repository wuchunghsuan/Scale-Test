
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

dir = "./spark/" + jobId + "/watchData"
createFile = dir + "/create"
deleteFile = dir + "/delete"
outputTmp = dir + "/file_tmp"
outputFig = dir + "/file_bar.pdf"

# jobStart = 0
# jobStop = 0
# jobTime = 0

def compute_create():
    fileBar = []
    fi = open(createFile)
    for line in fi:
        args = line.split(" ")
        if len(args) != 4:
            print("Wrong line!")
            continue
        time = int(args[0]) - int(jobStart)
        if time > 10000 or time < 0:
            print("Wrong time!")
            continue
        while len(fileBar) <= time:
            fileBar.append(0)
        fileBar[time] += 1
    fi.close()
    print(fileBar)
    return fileBar
    
def compute_delete(fileBar):
    fi = open(deleteFile)
    for line in fi:
        args = line.split(" ")
        if len(args) != 4:
            print("Wrong line!")
            continue
        time = int(args[0]) - int(jobStart)
        if time >= len(fileBar):
            print("Wrong time!")
            continue
        fileBar[time] -= 1
    fi.close()
    return fileBar


def draw(fileBar):
    x = np.arange(len(fileBar))

    # the histogram of the data
    # plt.hist(fileBar)
    plt.bar(x, fileBar, 1,
                linewidth=0, color=orange, 
                edgecolor=orange, hatch="++++",
                label='Copy')

    plt.xlabel('Time(s)')
    plt.ylabel('Number of Created File')
    plt.title('New Created File in a Job')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.xlim(40, 160)
    # plt.ylim(0, 0.03)
    plt.grid(True)
    # plt.show()
    plt.savefig(outputFig)

fileBar = compute_create()
# fileBar = compute_delete(fileBar)
draw(fileBar)




# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))