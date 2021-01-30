#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sc

def mu_full_ion(x,y,z):
    print("X+Y+Z=",round(x+y+z,4))
    return round(4/(3+5*x-z),2)

def roche_lobe_sep(m1,m2,r1):
    q = m1/m2
    A = r1/(0.49*q**(2/3))
    A = round(A*(0.6*q**(2/3) + np.log(1 + q**(1/3))),2)
    print("Binary separation: ",round(A,2))
    print("Mass ratio: ",round(q,2))
    return [A,q]
    