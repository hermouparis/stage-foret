#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:01:36 2022

@author: boucheta
"""

import pandas as pd
import numpy as np
import netCDF4 as nc

def getxyfromvar(file, var):
    dat = nc.Dataset(file)
    time = nc.num2date(dat['time'][:], dat['time'].units, only_use_cftime_datetimes=False, only_use_python_datetimes=True)
    y = dat[var][:]
        
    return np.array(time), np.array(y).flatten()

def getDataFramefromvar(file, var):
    time, y = getxyfromvar(file, var)
    if var == "DSN_T_ISBA":
        y = y * 100
    y = np.array(y).flatten()
    return pd.DataFrame({var: y}, index=time)