# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:42:31 2018

@author: Mario
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import linear_model

def squared_sum(x): #finds sum of squared values of a given array
    sq_sum=0
    for i in x:
        sq_sum=sq_sum+(i**2)
    return sq_sum
def calc_A(x,y): #calculates y-intercept
    a=((y.sum()*squared_sum(x))-(x.sum()*x.dot(y)))/((len(x)*squared_sum(x))-(x.sum()**2))
    return a
def calc_B(x,y): #calculates slope
    b=((len(x)*x.dot(y))-(x.sum()*y.sum()))/((len(x)*squared_sum(x))-(x.sum()**2))
    return b    
def abline(slope, intercept): #plots line given slope and intercept
    """Plot a line from slope and intercept"""
    axes = plt.gca() #get current axis of plot
    x_vals = np.array(axes.get_xlim())#gets axis limits
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-')
def reg_val(x,y): #returns array of regression values for given x values
    a=calc_A(x,y)
    b=calc_B(x,y)
    reg=[]
    for i in x:
        reg.append((b*i)+a)
    return reg
def error(x,y): #returns standard error of estimate
    reg=reg_val(x,y)
    return math.sqrt((squared_sum(np.subtract(y,reg))/(len(y)-2)))
def plot_regression(x,y):
    a=calc_A(x,y)
    b=calc_B(x,y)
    abline(b,a)
def correlation(x,y):
    r= ((len(x)*x.dot(y))-(x.sum()*y.sum()))/math.sqrt((len(x)*squared_sum(x)-x.sum()**2)*(len(y)*squared_sum(y)-y.sum()**2))
    return r
def print_stats(x,y):
    print("sample size:\t%f" % len(x))
    print("slope is :\t%f" % calc_B(x,y))
    print("y-int is :\t%f" % calc_A(x,y))
    print("error is :\t%f" % error(x,y))
    print("correlation:\t%f" % correlation(x,y))


file =open("challenge1.txt","r")
lines=file.readlines()
file.close()
x,y=[],[]
for line in lines:
    a=line.split(",")
    x.append(float(a[0]))
    y.append(float(a[1].replace("\n","")))


x=np.array(x)
y=np.array(y)


#plot
plt.scatter(x,y)
plot_regression(x,y)
print_stats(x,y)
#plt.plot(x, body_reg.predict(x))
plt.show()






    
    