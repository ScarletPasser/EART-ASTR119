#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
HW 1 problem 4

This script does the following:
    - Part A: Computes the remaining amount of a substance in radioactive decay,
    given the halflife (T), and the initial amount (N0). If N0 is not given it 
    returns the fractional amount. 
    - Part B: Uses the script from part A to compute the remaining amounts of 
    Carbon 14 given its half life and three values of time (t).
    - Part C: Computes the same function as in part A butt allows the user to 
    input their own half life and ttime elapsed. 
    

@author: scarletpasser
"""
from math import e

#############################################################################
#                           parameters/variables
#############################################################################

hlf_life = 5730         #Half life for carbon 14
initial_amount = 1      #initial amount of carbon 14 

##############################################################################
#                           define functions
##############################################################################

def Remain_amt(t):         #Radioactive decay as a function of time
    T  = hlf_life       
    N0 = initial_amount
    return N0*e**(-t/T)
    
##############################################################################
#                           computations/output (Part A/B)
##############################################################################

for t in range(10000, 1000001):                     #setting time equal to  
    if t==10000 or t==100000 or t==1000000:         #10kyr, 100kyr, and 10Myr
        print 'remaining amount is', Remain_amt(t)
        
##############################################################################
#                           computations/output (Part C)
##############################################################################
        
T = int(raw_input("what is the half life?: "))      #setting T as a user input
t = int(raw_input("what is the time elapsed?: "))   #setting t as a user input
    
print 'the remaining amount is:', Remain_amt(t)     #computing remaining amount
    