#!/bin/python2.7
"""

--> 1) load OK seismicity and well data
--> 2) plot eqs and wells using matplotlib
--> 3) select polygon that encompasses seism., project to equal area
       and compute area of polygon



"""

import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap


#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'

dPar  =  {   'nClicks' : 1,
             'tmin'    : 2010,
             'areaOK'  : 181*1e3,#in km
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# or 'cea' 'aea' for equal area projections
             'dt_map'    : 6./12
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------

# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
# data-time to decimal years
YR = mSeis[1, :]
MO = mSeis[2, :]
DY = mSeis[3, :]
HR = mSeis[4, :]
MN = mSeis[5, :]
SC = mSeis[6, :]

aTime = YR + (MO - 1)/12 + (DY - 1)/365.25 + HR/(365.25*24) + MN/(365.25*24*60) + SC/(365.25*24*3600)
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])

#TODO: select most recent seismic events
t0 = 2010
tf = 2017
sel    = sel_eq = np.logical_and( mSeis[0]  >= t0, mSeis[0]   <= tf)
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T

#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
#plot wells
#plot seismicity

at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
   
    
    # select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    # select wells with start dates before t1
    sel_we = np.logical_and( mWells[1] <= t1, mWells[1]  <= t1)
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()

    ### create basemap object
    plt.figure(1)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
   
    # draw state boundaries
    m.drawcoastlines()

    #plot seismicity and well locations
    #aX_eq, aY_eq = m(  mSeis[1][sel_eq], mSeis[2][sel_eq]
    aX_we, aY_we = m( mWells[2][sel_we],  mWells[3][sel_we])
    m.plot(aX_we, aY_we, 'ro', ms = 2)
    
        # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------
    
    print("Please click %i times"%( dPar['nClicks']))
    tCoord = plt.ginput( dPar['nClicks'])
    print("clicked", tCoord)
    plt.show()
       

    aLon =  np.array( tCoord).T[0]
    aLat =  np.array( tCoord).T[1]




# project into equal area coordinate system
    
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
#compute area using eis_utils.area_poly
def area_poly( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    #sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    # or:
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    #sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or:
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)

aX, aY = ( aX_we/1000 , aY_we/1000)
A_seis = area_poly( aX, aY)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(dPar['areaOK']) # about 1/3



