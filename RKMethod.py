#Jeffrey Wiedrich
#07/05/2020
#GCU CST305
#Basically, I went ahead and used my Runge Katta code from class as a base, and then implemented the rest that we needed

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import time
import sys
sys.setrecursionlimit(1500) #Changing the recursion limit so it can run past 993 steps

xAxisPoints = [1] #Adding in x0
yAxisPoints = [5] #Adding in y0

def rungeKatta(x0, y0, h, depthLimit):
    print("(", x0, ", ", y0, ")") #Printing out starting points

    k = [formula(x0, y0), 0, 0, 0] #Declaring k0, or k1 if you are doing it by hand and setting array size
    k[1] = formula(x0 + (h/2), y0 + (h/2) * k[0]) #Inputting k1
    k[2] = formula(x0 + (h/2), y0 + (h/2) * k[1]) #Inputting k2
    k[3] = formula(x0 + h, y0 + h * k[2]) #Inputting k3

    T = k[0] + 2 * k[1] + 2 * k[2] + k[3] #Getting T

    y1 = y0 + (h/6) * T #Usint T to solve y1
    yAxisPoints.append(y1) #Adding y1 to the graph

    x1 = x0 + h #Solving for x1
    xAxisPoints.append(x1) #Adding x1 to the graph

    print (1000 - depthLimit, "steps\n") #Printing out the step number

    if (depthLimit > 0): #Limiting the depth of recursion
        rungeKatta(x1, y1, h, depthLimit - 1) #Starts the recursion to find further values
    else:
        plt.plot(xAxisPoints, yAxisPoints, color = 'green', linestyle = 'dashed', marker = 'o', markerfacecolor='blue', markersize=12) #Adding graph values in and customizing the graph
        plt.ylim(5, 8) #Setting the graph limits for the y axis
        plt.xlim(1, 21) #Setting the graph limits for the x axis

        plt.xlabel("x axis") #Labeling the x axis
        plt.ylabel("y axis") #Labeling the y axis
        print("Ran in %s seconds" % (time.time() - start_time))  # Prints the runtime
        plt.show() #Printing the graph


def formula(x, y):
    dydx = y / (math.exp(x) - 1) #The equation for the given problem
    return dydx #Returning the value


start_time = time.time() #Starts the timer
rungeKatta(1, 5, 0.02, 1000) #Starts the program
print("Looked at the graph for %s seconds" % (time.time() - start_time)) #Prints the total runtime, including all the time the graph is open
