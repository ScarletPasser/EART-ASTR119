#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#anaconda2/python2.7

"""
HW 1 problem 1
This script does the following:
    Commputes the area of a rectangle (A_rec = b*c) and the area of a triangle 
    (A_tri = 0.5*h*b)

@author: scarletpasser

"""


from sympy import symbols

##############################################################################
#                           parameters/variables
##############################################################################

b, c, h = symbols('b, c, h') #b = base
                             #c = height of rectangle
                             #h = height of triangle 

A_rec = b*c                  #Area of rectangle 

A_tri = 0.5*b*h              #Area of triangle 

###############################################################################
#                           output
###############################################################################

print "A =", A_rec, "A =", A_tri