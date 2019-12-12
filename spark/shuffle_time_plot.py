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

label_size=20

dir = "./spark/"
outputFig1 = dir + "/shuffle_time_plot.pdf"
outputFig2 = dir + "/shuffle_request_plot.pdf"
outputFig3 = dir + "/size_per_task_plot.pdf"
outputFig4 = dir + "/fetch_size_plot.pdf"

xlim=7000

x = [
        640,
        1280,
        1920,
        2560,
        3200,
        3840,
        4480,
        5120,
        5760,
        6400
    ]

def draw1():
    data = [
        14307,
        14480,
        14465,
        13973,
        14999,
        16344,
        19492,
        22344,
        25892,
        30912
    ]

    plt.plot(x, data,
            linewidth=3.0,
            markersize=10.0,
            markeredgewidth=0,
            color=blue,
            marker="o",
            label='Total Shuffle Time')

    # for a,b in zip(x, data):
    #     plt.text(a, b+0.5, "(" + str(a/100) + "," + str(b/100) + ")", ha='center', va= 'bottom',fontsize=12)

    plt.xlabel('Number of Tasks',size=label_size)
    plt.ylabel('Time(sec)',size=label_size)
    plt.xlim(0, xlim)
    plt.ylim(10000, 35000)
    plt.grid(True)
    plt.legend()
    plt.savefig(outputFig1)

def draw2():
    data = [
        65,
        262,
        589,  
        1048,
        1638,
        2359,
        3211,
        4194,
        5308,
        6553,
    ]

    plt.close()
    plt.plot(x, data,
            linewidth=3.0,
            markersize=10.0,
            markeredgewidth=0,
            color=green,
            marker="h",
            label='Shuffle Request')

    plt.xlabel('Number of Tasks',size=label_size)
    plt.ylabel('Shuffle Request Count/${10_3}$',size=label_size)
    plt.xlim(0, xlim)
    plt.ylim(0, 8000)
    plt.grid(True)
    plt.legend()
    plt.savefig(outputFig2)

def draw3():
    data = [
        800,
        400,
        267,
        200,
        160,
        133,
        114,
        100,
        89,
        80,
    ]

    plt.close()
    plt.plot(x, data,
            linewidth=3.0,
            markersize=10.0,
            markeredgewidth=0,
            color=orange,
            marker="s",
            label='Data Size of each Task')

    plt.xlabel('Number of Tasks',size=label_size)
    plt.ylabel('Data Size(MB)',size=label_size)
    plt.xlim(0, xlim)
    plt.ylim(0, 1000)
    plt.grid(True)
    plt.legend()
    plt.savefig(outputFig3)

def draw4():
    data = [
        7813,
        1953,
        868,
        488,
        313,
        217,
        159,
        122,
        96, 
        78
    ]

    plt.close()
    plt.plot(x, data,
            linewidth=3.0,
            markersize=10.0,
            markeredgewidth=0,
            color=light_blue,
            marker="D",
            label='Shuffle Request Fetch Size')

    plt.xlabel('Number of Tasks',size=label_size)
    plt.ylabel('Data Size(KB)',size=label_size)
    plt.xlim(0, xlim)
    plt.ylim(0, 10000)
    plt.grid(True)
    plt.legend()
    plt.savefig(outputFig4)


draw1()
draw2()
draw3()
draw4()




# print ("Map Task Number: " + str(len(mapBar)))
# print ("Reduce Task Number: " + str(len(reduceBar)))