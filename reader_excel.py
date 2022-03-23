#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:13:08 2022

@author: boucheta
"""

import pandas as pd

      
def jalons_transect_principal(file, sheet_num=1, column_dates=0, cols="B,D:U"):
    data = pd.read_excel(file, sheet_name=sheet_num, index_col=column_dates, header=3, usecols=cols)
    data.index = pd.to_datetime(data.index, errors="coerce", dayfirst=True)
    data = data[data.index.notnull()]  # We only keep the HTN values
    data = data.replace("traces", 0)
    data.index.name = "Date"
    
    return data

def feuille_de_travail(file):
    data = pd.read_excel (file, header=0, index_col=0, skiprows=[1], sheet_name='feuilledetravail')

    return data


def armoire_arbre(file):
    meta_label = {
        "Temp_C(1)" : "Tronc Sud",
        "Temp_C(2)" : "Tronc Nord",
        "Temp_C(3)" : "Branche Nord",
        "Temp_C(4)" : "Branche Sud"
    }
    na_values = ['INF', 'NAN']
    data = pd.read_csv(file, header=0, index_col=0, low_memory=False, na_values=na_values)
    data.index = pd.to_datetime(data.index)

    return data