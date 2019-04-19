#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

HW 2 problem 1


"""

import numpy as np
import matplotlib.pyplot as plt
############################################################################
#                               Load Data (PART A)
############################################################################

Well_Data  = np.loadtxt('injWell_OK.txt', comments = '#') #loading data
Quake_Data = np.loadtxt('seism_OK.txt', comments = '#')

#Assigning the variable to the corresponding column

YR = Quake_Data[:, 1]   #year
MO = Quake_Data[:, 2]   #month
DY = Quake_Data[:, 3]   #day
HR = Quake_Data[:, 4]   #hour
MN = Quake_Data[:, 5]   #minute
SC = Quake_Data[:, 6]   #second

############################################################################
#                               Convert Columns (PART B)
############################################################################

#converting columns to decimal years
    
DecYear = YR + (MO - 1)/12 + (DY - 1)/365.25 + HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)

############################################################################
#        Find Earthquake rate and graph data (PART C)
############################################################################

k = 200                 #k value
t = DecYear*3.154e7     #time in seconds (as was in the example shown in class)

def quake_rate(t):      #Earth quake rate (as was in class)
    print(t.shape[0])
    aS   = np.arange( 0, t.shape[0]-k, 1)
    rate = np.zeros( aS.shape[0])

    iS = 0

    for i in aS:
        i1, i2 = i, i + k
        rate[iS] = k/(t[i2] - t[i1])
        iS += 1
    return rate

#variables for graphing in two subplots 

depth = Quake_Data[:, 9]  
mag   = Quake_Data[:, 10]

'''
plt.subplot( 211)      
plt.plot( t, depth)
plt.xlabel('time(s)')
plt.ylabel('depth')
plt.show()

plt.subplot( 212)
plt.plot( t, mag)
plt.xlabel('time(s)')
plt.ylabel('mag')
plt.show()
'''
############################################################################
#                               Plot active wells 
############################################################################

t0           = Well_Data[:,1]
active_wells = Well_Data[:,5]
plt.plot(t0, active_wells, 'o')
plt.show()

    



