#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:14:30 2019

@author: spasser
"""

"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows



"""


import os
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.basemap import Basemap



#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------

file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'


dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,

             'tmin'      : 2005, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------

# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq, comments = '#').T
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
YR = mSeis[1, :]
MO = mSeis[2, :]
DY = mSeis[3, :]
HR = mSeis[4, :]
MN = mSeis[5, :]
SC = mSeis[6, :]

at = YR + (MO - 1)/12 + (DY - 1)/365.25 + HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)

mSeis  = np.array( [at, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well, comments = '#').T


#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------

# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    k_win = 200
    
    def eqRate( at, k_win):
        
        # smoothed rate from overlapping sample windows normalized by delta_t
        aS          = np.arange( 0, at.shape[0]-k_win, 1)
        aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
        iS = 0
        for s in aS:
            i1, i2 = s, s+k_win
            aBin[iS]  = 0.5*( at[i1]+at[i2])
            aRate[iS] = k_win/( at[i2]-at[i1])
            iS += 1
        return aBin, aRate
    
    aBin  = eqRate(at,k_win)[0]     #binned time 
    aRate = eqRate(at,k_win)[1]     #rate of earthquakes 
    
    #plot seismicity rates
    plt.plot( aBin, aRate)
    
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    
    
    
    #TODO: plot cumulative number of earthquakes
   
    #cummulative_num = np.cumsum( np.ones( N))
   
    
    
    ax2 = plt.subplot( 212)     
    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()

