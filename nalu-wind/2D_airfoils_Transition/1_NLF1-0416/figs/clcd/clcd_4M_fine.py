import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import yaml

size=13
params = {'legend.fontsize': 'large',
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size,
          'ytick.labelsize': size}
plt.rcParams.update(params)
co_list   = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

co0=co_list[0]
co1=co_list[1]

# Experiment
cl = pd.read_csv('exp_Re4M_aoa.csv',names=['aoa','cl'],header=None)
cdcl = pd.read_csv('exp_Re4M_polar.csv',names=['cd','cl'],header=None)

with open('nlf0416_F_rey04000000_turb.yaml', "r") as data0:
    turb=yaml.safe_load(data0)

with open('nlf0416_F_rey04000000.yaml', "r") as data1:
    trans=yaml.safe_load(data1)


plt.figure(figsize=(12,4.5))
plt.subplot(1, 2, 1)
#fig = plt.figure(1)
plt.plot(cl['aoa'],cl['cl'],'ko')
plt.plot(turb['nlf0416_F']['aoa'],turb['nlf0416_F']['cl'])
plt.plot(trans['nlf0416_F']['aoa'],trans['nlf0416_F']['cl'])
plt.xlim([-7,20])
plt.ylim([-0.5,2.0])
plt.xlabel('Angle of Attack [deg]')
plt.ylabel('Lift coefficient, $C_{l}$')
plt.legend(['Experiment','Turbulent','Transition'])
plt.tight_layout()

plt.subplot(1, 2, 2)
plt.plot(cdcl['cd'],cdcl['cl'],'ko')
plt.plot(turb['nlf0416_F']['cd'],turb['nlf0416_F']['cl'])
plt.plot(trans['nlf0416_F']['cd'],trans['nlf0416_F']['cl'])
plt.xlim([0.0,0.025])
plt.ylim([-0.5,2.0])
plt.xlabel('Drag coefficient, $C_{d}$')
plt.ylabel('Lift coefficient, $C_{l}$')
plt.legend(['Experiment','Turbulent','Transition'])
plt.tight_layout()
plt.savefig("nlf0416_clcd.png",dpi=300)

plt.show()
