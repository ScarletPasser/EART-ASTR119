#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
HW 1 problem 2
This script does the following:
    Part A: 
        Calculates the area of an irregular polygon given it's coordinates. 
    Part B:
        Calculates the area of an irregular polygon given it's coordinates, 
        using vector notation. 
        
@author: scarletpasser

"""

from numpy import zeros
import numpy as np

##############################################################################
#                      Parameters / variables (part A)
##############################################################################

x    = zeros(6)  # x values of the coordinates 
x[0] = 1
x[1] = 3
x[2] = 4
x[3] = 3.5
x[4] = 2
x[5] = 1         # a repeat of x[0], in order to achieve the last term 
#                in the sum (x[n]*y[1])

  
y    = zeros(6)  # y values of the coordinates
y[0] = 1
y[1] = 1
y[2] = 2
y[3] = 5
y[4] = 4
y[5] = 1         # a repeat of x[0], in order to achieve the last term 
#                in the sum (y[n]*x[1])

##############################################################################
#                       Parameters / variables (part B)
##############################################################################

x_vec = np.array([1, 3, 4, 3.5, 2, 1]) #x coordinates 
y_vec = np.array([1, 1, 2, 5, 4, 1,])  #y coordinates 

##############################################################################
#                         Computations/output (part A)
##############################################################################

#computing the area from the manualy defined variables 
area_polygon = 0                #initial area
                                
for i in range (0, 5):          #for loop 
    area_polygon += .5*((y[i+1]*x[i])-(x[i+1]*y[i]))
        
print "The area of my polygon is:", area_polygon

##############################################################################
#                           Computations/output (part B)
##############################################################################

#computing the area using the vector notation 
area_polygon_vec = 0.5*((np.dot(y_vec[1:], x_vec[:5]))-(np.dot(x_vec[1:], y_vec[:5])))

print "The area of my polygon using vector notation is:", area_polygon_vec




   