#!/usr/bin/env python3
# coding: utf-8
# import classy module
from classy import Class
import numpy as np
import matplotlib.pyplot as plt
from math import pi
common_settings = {
'N_ur': 3.05,
'perturbations_verbose':1,
'background_verbose':3,
'output':'mPk',
'gauge':'newtonian',
'P_k_max_1/Mpc':100,
'z_max_pk':3,
}

standardCDM = Class()
standardCDM.set(common_settings)
standardCDM.set({'omega_cdm':0.12})
standardCDM.compute()

dmcannCDM = Class()
# pass input parameters
dmcannCDM.set(common_settings)

mWDM = 3640

astar = 1.68e-7 *(mWDM/1000)**(-4/3)
dmcannCDM.set({
    #'omega_b':0.0223828,
    'omega_cdm': 0,
    'omega_ncdm': 0.12,
    'N_ncdm':1,
    'T_ncdm' : 0.16*( 1000/ mWDM)**(1./3.),
    'selfinteraction':'n',
    #'ncdm_psd_parameters': '1 , 0.0 , 1.0 , 0.0 , 0.0 , 1.0 ', ## fermi- dirac here
    'ncdm_psd_parameters': '1 , 1, 0 ,0', ## fermi- dirac here
    #'aNR': astar,
    #'sigmaovermass':0.1,
})
dmcannCDM.set({
    'tol_ncdm':1.e-6,
    'tol_ncdm_newtonian':1.e-10,
    'tol_ncdm_bg':1.e-6,
    'tol_perturbations_integration':1.e-4,
    'l_max_ncdm':20,
    'ncdm_fluid_approximation':2,
    'background_verbose':3,
})
dmcannCDM.compute()

kk = np.logspace(-4,np.log10(100),500) # k in h/Mpc
Pkcann = [] # P(k) in (Mpc/h)**3
Pkstand = [] # P(k) in (Mpc/h)**3
h = dmcannCDM.h() # get reduced Hubble for conversions to 1/Mpc
for k in kk:
    Pkcann.append(dmcannCDM.pk(k*h,0.)*h**3) # function .pk(k,z)
    Pkstand.append(standardCDM.pk(k*h,0.)*h**3 ) # function .pk(k,z)

plt.figure(dpi=100)
plt.xscale('log');plt.yscale('log');plt.xlim(kk[0],kk[464])
plt.xlabel(r'$k \,\,\,\, [h/\mathrm{Mpc}]$')
plt.ylabel(r'$P(k) \,\,\,\, [\mathrm{Mpc}/h]^3$')

plt.plot(kk,Pkcann,'r-',label=r'WDM')
plt.plot(kk,Pkstand,'k-',label=r'Standard CDM')

plt.legend(loc='best')


plt.savefig('fra_scripts/wdmmpk.pdf')