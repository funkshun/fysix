#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:47:06 2018

@author: ericyelton
"""

import numpy as np 
import scipy as sci


#So these are the ODEs set up for a single community
#Here the quanity y is the following vector: 
#x = [s,i,r]
#t is time 
def dydx(t,x,b,k):
    dydx = np.zeros(3)
    
    dydx[0] = -1*b*x[0]*x[1]
    dydx[1] = b*x[0]*x[1]-k*x[1]
    dydx[2] = k*x[1]
return dydx 

def stepper():
    