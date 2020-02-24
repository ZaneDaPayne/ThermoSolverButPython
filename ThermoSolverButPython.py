""" I'm trying to make ThermoSolver in Python for some reason.
    Run the script to initialized the functions.
    antoines is for vapor pressure.
    compressibility is for compressibility factor.
    """


import pandas as pd
import numpy as np
from scipy.interpolate import interp2d

#%% fugasity coef

fugasity_coef=pd.read_csv("fugasity_coef.txt",sep=" ",header=1,float_precision=5)
fugasity_coef = fugasity_coef.to_numpy()
#Fixes negatives
for index, i in np.ndenumerate(fugasity_coef):
    if type(i)==float:
        if i>20:
            fugasity_coef[index] = round(20-i,4)
        else:
            pass
    else:
        pass
fugasity_coef= np.split(fugasity_coef,[42,84,127])   

fugasity_coef[2] = np.delete(fugasity_coef[2],0,0)#remove log(phi1) label

fugasity_coef_0 = np.concatenate((fugasity_coef[0], fugasity_coef[1]),axis=1)#add the two arrays for phi0 along vertical axis
fugasity_coef_0 = np.delete(fugasity_coef_0,[14,27],1)#remove second list of Tr at 14 and empty column at 27   
fugasity_coef_0[1:,0]=fugasity_coef_0[1:,0].astype(float)#for some reason the first column was all str

fugasity_coef_1 = np.concatenate((fugasity_coef[2],fugasity_coef[3]),axis=1)
fugasity_coef_1 = np.delete(fugasity_coef_1,[14,27],1)
fugasity_coef_1[1:,0]=fugasity_coef_0[1:,0].astype(float)

#create linear interpolated model
phi0 = interp2d(fugasity_coef_0[0,1:],fugasity_coef_0[1:,0],fugasity_coef_0[1:,1:])#inputs are (Pr,Tr)
phi1 = interp2d(fugasity_coef_1[0,1:],fugasity_coef_1[1:,0],fugasity_coef_1[1:,1:])

#%% compressibility factor

compressibility_factor=pd.read_csv("Compressibility.txt",sep=" ",header=1,float_precision=5)
compressibility_factor = compressibility_factor.to_numpy()
#fixes negatives
for index, i in np.ndenumerate(compressibility_factor):
    if type(i)==float:
        if i>20:
            compressibility_factor[index] = round(20-i,4)
        else:
            pass
    else:
        pass
compressibility_factor= np.split(compressibility_factor,[42,84,127])   

compressibility_factor[2] = np.delete(compressibility_factor[2],0,0)#remove Z1 label

compressibility_factor_0 = np.concatenate((compressibility_factor[0], compressibility_factor[1]),axis=1)#add the two arrays for Z0 along vertical axis
compressibility_factor_0 = np.delete(compressibility_factor_0,[14,27],1)#remove second list of Tr at 14 and empty column at 27   
compressibility_factor_0[1:,0]=compressibility_factor_0[1:,0].astype(float)#for some reason the first column was all str

compressibility_factor_1 = np.concatenate((compressibility_factor[2],compressibility_factor[3]),axis=1)
compressibility_factor_1 = np.delete(compressibility_factor_1,[14,27],1)
compressibility_factor_1[1:,0]=compressibility_factor_0[1:,0].astype(float)

#create linear interpolated model
z0 = interp2d(compressibility_factor_0[0,1:],compressibility_factor_0[1:,0],compressibility_factor_0[1:,1:])#inputs are (Pr,Tr)
z1 = interp2d(compressibility_factor_1[0,1:],compressibility_factor_1[1:,0],compressibility_factor_1[1:,1:])  

#%% Enthalpy departure

enthalpy_departure=pd.read_csv("Enthalpy_departure.txt",sep=" ",header=1,float_precision=5)
enthalpy_departure = enthalpy_departure.to_numpy()
#fixes negatives, but now there are some negatives less than -10.
for index, i in np.ndenumerate(enthalpy_departure):
    if type(i)==float:
        if (i>20) & (i<100):
            enthalpy_departure[index] = round(20-i,4)
        elif i>100:
            enthalpy_departure[index] = round(200-i,4)
        else:
            pass
    else:
        pass
enthalpy_departure= np.split(enthalpy_departure,[42,84,127])   

enthalpy_departure[2] = np.delete(enthalpy_departure[2],0,0)#remove hdep(1) label

enthalpy_departure_0 = np.concatenate((enthalpy_departure[0], enthalpy_departure[1]),axis=1)#add the two arrays for hdep(0) along vertical axis
enthalpy_departure_0 = np.delete(enthalpy_departure_0,[14,27],1)#remove second list of Tr at 14 and empty column at 27   
enthalpy_departure_0[1:,0]=enthalpy_departure_0[1:,0].astype(float)#for some reason the first column was all str

enthalpy_departure_1 = np.concatenate((enthalpy_departure[2],enthalpy_departure[3]),axis=1)
enthalpy_departure_1 = np.delete(enthalpy_departure_1,[14,27],1)
enthalpy_departure_1[1:,0]=enthalpy_departure_0[1:,0].astype(float)

#create linear interpolated model
h_dep_0 = interp2d(enthalpy_departure_0[0,1:],enthalpy_departure_0[1:,0],enthalpy_departure_0[1:,1:])#inputs are (Pr,Tr)
h_dep_1 = interp2d(enthalpy_departure_1[0,1:],enthalpy_departure_1[1:,0],enthalpy_departure_1[1:,1:])  


#%% Entropy departure

entropy_departure=pd.read_csv("Entropy_departure.txt",sep=" ",header=1,float_precision=5)
entropy_departure = entropy_departure.to_numpy()
#fixes negatives, but now there are some negatives less than -10.
for index, i in np.ndenumerate(entropy_departure):
    if type(i)==float:
        if (i>20) & (i<100):
            entropy_departure[index] = round(20-i,4)
        elif i>100:
            entropy_departure[index] = round(200-i,4)
        else:
            pass
    else:
        pass
entropy_departure= np.split(entropy_departure,[42,84,127])   

entropy_departure[2] = np.delete(entropy_departure[2],0,0)#remove hdep(1) label

entropy_departure_0 = np.concatenate((entropy_departure[0], entropy_departure[1]),axis=1)#add the two arrays for hdep(0) along vertical axis
entropy_departure_0 = np.delete(entropy_departure_0,[14,27],1)#remove second list of Tr at 14 and empty column at 27   
entropy_departure_0[1:,0]=entropy_departure_0[1:,0].astype(float)#for some reason the first column was all str

entropy_departure_1 = np.concatenate((entropy_departure[2],entropy_departure[3]),axis=1)
entropy_departure_1 = np.delete(entropy_departure_1,[14,27],1)
entropy_departure_1[1:,0]=entropy_departure_0[1:,0].astype(float)

#create linear interpolated model
s_dep_0 = interp2d(entropy_departure_0[0,1:],entropy_departure_0[1:,0],entropy_departure_0[1:,1:])#inputs are (Pr,Tr)
s_dep_1 = interp2d(entropy_departure_1[0,1:],entropy_departure_1[1:,0],entropy_departure_1[1:,1:])  


#%% material properties

materials = pd.read_csv("critical_acentric_antoine.txt",sep=" ",float_precision=6)
materials.to_numpy()
#fix the negative values of C. Only works because no positive values start with 2.
for i in range(len(materials["C"])):
        if np.floor(materials["C"][i]/1000)==2:
            materials.at[i,"C"]=2000-materials["C"][i]
        elif np.floor(materials["C"][i]/100)==2:
            materials.at[i,"C"]=200-materials["C"][i]
        elif np.floor(materials["C"][i]/10)==2:
            materials.at[i,"C"]=20-materials["C"][i]
        else:
            pass
#fix the negative values of omega
for i in range(len(materials["omega"])):
        if materials["omega"][i]>=20:
            materials.at[i,"omega"]=20-materials["C"][i]
        else:
            pass 
          
#%%

def ls():
    """Lists all materials in library."""
    for i in range(len(materials["Name"])):
        print(f"{materials['Formula'][i]} {materials['Name'][i]}")
        
def material_properties(material):
    """Accepts string. Returns series of data for the specified material.
    material_properties(name)['MW(g/mol)'] is the MW of that name."""
    name_index = 0
    for i in range(len(materials["Name"])):
        if materials["Name"][i]==material:
            name_index = i
            break
        elif materials["Formula"][i]==material:
            name_index = i
            break
        else:
            pass
    return materials.iloc[name_index]


def antoins(name,temp):
    """Accepts name as string and temp in K. Returns Psat in bar.""" 
    material = material_properties(name)
    A = material['A']
    B = material['B']
    C = material['C']
    Tmax = material['Tmax']
    Tmin = material['Tmin']
    if temp>Tmax or temp<Tmin:
        print(f"The specified temperature is out of bounds.\nTemp must be between {Tmin}K and {Tmax}K")
        return
    else:
        Psat = np.exp(A-B/(temp+C))
    return Psat

def compressibility(name,temp,pres,reduced=False):
    """name as string, temp in K, pres in bar. If using reduced T and P, reduced=True.
    Returns compressibility factor."""
    material = material_properties(name)
    omega = material['omega']
    if reduced==True:
        Pr=pres
        Tr=temp 
    else:
        Tc = material['Tc(K)']
        Pc = material['Pc(Bar)']
        Tr = temp/Tc
        Pr = pres/Pc
    Z = z0(Pr,Tr)[0] + omega*z1(Pr,Tr)[0] 
    return Z

def departure(name,temp,pres,reduced=False,_print=True):
    """name as string, temp in K, pres in bar. If using reduced T and P, reduced=True.
    Prints and returns (s_departure,h_departure). hdep is h-h_ideal/RTc, sdep is s-s_ideal/R."""
    material = material_properties(name)
    omega = material['omega']
    if reduced==True:
         Pr=pres
         Tr=temp 
    else:
        Tc = material['Tc(K)']
        Pc = material['Pc(Bar)']
        Tr = temp/Tc
        Pr = pres/Pc
    sdep = s_dep_0(Pr,Tr)[0] + omega*s_dep_1(Pr,Tr)[0]
    hdep = h_dep_0(Pr,Tr)[0] + omega*s_dep_1(Pr,Tr)[0]
    if _print==True:
        print(f"Enthalpy departure function is {round(hdep,4)}.\nEntropy departure function is {round(sdep,4)}.")
    return (sdep,hdep)

def Cp(name,temp,print=True):
    """Returns the constant pressure heat capacity in J/mol."""
    Cp_data
    
print(antoins("Water",283.9))
       

   