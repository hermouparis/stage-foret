#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:13:08 2022

@author: boucheta
"""

import pandas as pd
import plotly.express as px

      
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
        

def prettyPlot(data):
    long_data = pd.melt(data.reset_index(), id_vars=["Date"])
    fig = px.line(long_data, x="Date", y="value", color="variable")
    fig.show()
    return fig
        
    
    
if __name__ == "__main__":
    data = jalons_transect_principal('data/jtp_20192020.xlsm')
    print(data)
    fig = prettyPlot(data)
    fig.show(renderer="browser")