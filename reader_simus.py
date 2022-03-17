#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:01:36 2022

@author: boucheta
"""

import pandas as pd
import numpy as np
from snowtools.utils.prosimu import prosimu

def getxyfromvar(file, var):
    with prosimu(file) as p:
        y = p.read(var)
        time = p.readtime()
        
    return time, y

def getDataFramefromvar(file, var):
    time, y = getxyfromvar(file, var)
    if var == "DSN_T_ISBA":
        y = y * 100
    y = np.array(y).flatten()
    return pd.DataFrame({var: y}, index=time)