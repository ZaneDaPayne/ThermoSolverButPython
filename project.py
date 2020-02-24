#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:40:24 2020

@author: harini
"""


#%%
import csv
import numpy as np
def material(a,b):
    """Defines material properties"""
    values=[]
    with open('txtdata.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for line in readCSV:
            if a in line:
                j= np.array(line)
                if b =="Name":
                    return[line[2]]
                if b=="MW": #MW in g/mol
                    return[line[4]]
                if b== "Tc": #Tc in K  
                    return[line[5]]
                if b=="Pc":  #Pc in bars
                    return[line[6]]
                if b=="Tc and Pc": #Tc in K and Pc in bars
                    return[line[5],line[6]]
                if b=="omega":
                    return[j[7]]
                if b=="A,B,C":
                    return[line[8],line[9],line[10]]
                if b=="Tmin":
                    return[line[11]]
                if b=="Tmax": #Tmax in K
                    return(line[12])
                if b== "Tmin and Tmax": #Tmin and Tmax in K
                    return[line[11],line[12]]
values=(material('Oxygen','Pc'))
print(values)
#Antoinne's Calculator
T=343.15#define T in K
Psat=np.exp(float(values[0])-(float(values[1])/(T+float(values[2]))))  
print("The Saturation pressure is {} bars".format(Psat))
#%%
import numpy as np
def chemical(a):
    """Send in a chemical and function outputs array of chemical properties"""
    properties=[]
    with open('txtdata.csv') as csvfile:
        readCSV=csv.reader(csvfile)
        for line in readCSV:
            if a in line:
                r=np.array(line)
                return([["Molecular Formula = {}".format(r[1])],
                      ["Molecular Name = {}".format(r[2])],
                      ["Molecular Weight = {} g/mol".format(r[4])],
                      ["Tc={} [K]".format(r[5])],
                      ["Pc={}[bars]".format(r[6])],
                      ["A,B, and C = {},{}, and {}".format((r[7]),(r[8]),(r[9]))],
                      ["Tmin and Tmax={} and {} [K]".format(r[10],r[11])]])
properties=(chemical('Methanol'))
print(properties)

    






  