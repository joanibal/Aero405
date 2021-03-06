import numpy as np 
import matplotlib.pyplot as plt
import csv
from postProcessing import *

""" Main script for generating plots from wind tunnel data"""

# Plot setup
font = {'family': 'Times New Roman'}
plt.rc('font', **font)
fsize = 16
plt.rc('xtick', labelsize=fsize) 
plt.rc('ytick', labelsize=fsize)
fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(14,8))
##################

""" Plain wing """ 


data1 = 'Data/clean_trial5_+2.csv'
calib1 = 'Data/calibration10.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_+2.csv'
calib2 = 'Data/calibration10.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:14],0.5*(CL1[0:14]+CL2[0:14]),'-o',color=[1,0,0])

data1 = 'Data/clean_trial4_+1.csv'
calib1 = 'Data/calibration15.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_+1.csv'
calib2 = 'Data/calibration15.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:14],0.5*(CL1[0:14]+CL2[0:14]),'-o',color=[1,0.65,0])

data1 = 'Data/clean_trial4_0.csv'
calib1 = 'Data/calibration19.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_0.csv'
calib2 = 'Data/calibration19.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:15],0.5*(CL1[0:15]+CL2[0:15]),'-og')

data1 = 'Data/clean_trial4_-1.csv'
calib1 = 'Data/calibration17.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_-1.csv'
calib2 = 'Data/calibration17.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:15],0.5*(CL1[0:15]+CL2[0:15]),'-oc')

data1 = 'Data/clean_trial5_-2.csv'
calib1 = 'Data/calibration13.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_-2.csv'
calib2 = 'Data/calibration13.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:15],0.5*(CL1[0:15]+CL2[0:15]),'-ob')

data1 = 'Data/clean_trial4_noprop.csv'
calib1 = 'Data/calibration21.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_noprop.csv'
calib2 = 'Data/calibration21.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax0.plot(alpha1[0:15],0.5*(CL1[0:15]+CL2[0:15]),'k--o')

#ax0.legend(('+0.182c, +0.222D','+0.091c, +0.111D','0, 0','-0.091c, -0.111D','-0.182c, -0.222D','No Propeller'),fontsize=fsize,loc='lower right')
ax0.set_ylim((0,3.0))
ax0.set_xlim((-1,31))
ax0.set_title('Clean Wing',fontsize=fsize, fontweight='bold')
ax0.set_xlabel('Angle of Attack (deg)',fontsize=fsize)
ax0.set_ylabel(r'$C_{L}$', labelpad=30, rotation=0,fontsize=int(fsize*1.2))
# plt.text(10,1.75,'Centered propeller best',fontsize=fsize)

ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)

plt.suptitle('Test Data for Each Configuration', fontweight='bold', fontsize=fsize)
#################################

"""Plain flapped wing Trials 1,2"""

data1 = 'Data/plain_trial1_+2.csv'
calib1 = 'Data/calibration33.csv'
p_dyn1 = 0.29
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+2.csv'
calib2 = 'Data/calibration33.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax1.plot(alpha1[0:11],0.5*(CL1[0:11]+CL2[0:11]),'-o',color=[1,0,0])

data1 = 'Data/plain_trial1_+1.csv'
calib1 = 'Data/calibration29.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+1.csv'
calib2 = 'Data/calibration29.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax1.plot(alpha1[0:10],0.5*(CL1[0:10]+CL2[0:10]),'-o',color=[1,0.65,0])

data2 = 'Data/plain_trial2_0.csv'
calib2 = 'Data/calibration25.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

data3 = 'Data/plain_trial3_0.csv'
calib3 = 'Data/calibration25.csv'
[alpha3, CL3, CD3, CM3] = process(p_dyn1, Sref1, data3, calib3, prop1)
ax1.plot(alpha3[0:10],0.5*(CL2[0:10]+CL3[0:10]),'-og')

data1 = 'Data/plain_trial1_-1.csv'
calib1 = 'Data/calibration27.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-1.csv'
calib2 = 'Data/calibration27.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax1.plot(alpha1[0:11],0.5*(CL1[0:11]+CL2[0:11]),'-oc')

data1 = 'Data/plain_trial1_-2.csv'
calib1 = 'Data/calibration31.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-2.csv'
calib2 = 'Data/calibration31.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax1.plot(alpha1[0:12],0.5*(CL1[0:12]+CL2[0:12]),'-ob')

data1 = 'Data/plain_trial1_noprop.csv'
calib1 = 'Data/calibration23.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_noprop.csv'
calib2 = 'Data/calibration35.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax1.plot(alpha2[0:9],0.5*(CL1[0:9]+CL2[0:9]),'k--o')


ax1.set_ylim((0,3.0))
ax1.set_xlim((-1,31))
ax1.set_title('Plain Flapped Wing',fontsize=fsize, fontweight='bold')
ax1.set_xlabel('Angle of Attack (deg)',fontsize=fsize)
ax1.set_yticks([])

ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)



###########################

"""Slotted flapped wing Trials 1,2"""


data1 = 'Data/slot_trial1_+2.csv'
calib1 = 'Data/calibration39.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+2.csv'
calib2 = 'Data/calibration39.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:10],0.5*(CL1[0:10]+CL2[0:10]),'-o',color=[1,0,0])

data1 = 'Data/slot_trial1_+1.csv'
calib1 = 'Data/calibration44.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+1.csv'
calib2 = 'Data/calibration44.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:10],0.5*(CL1[0:10]+CL2[0:10]),'-o',color=[1,0.65,0])

data1 = 'Data/slot_trial1_0.csv'
calib1 = 'Data/calibration46.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_0.csv'
calib2 = 'Data/calibration46.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:11],0.5*(CL1[0:11]+CL2[0:11]),'-og')

data1 = 'Data/slot_trial1_-1.csv'
calib1 = 'Data/calibration42.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-1.csv'
calib2 = 'Data/calibration42.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:11],0.5*(CL1[0:11]+CL2[0:11]),'-oc')

data1 = 'Data/slot_trial1_-2.csv'
calib1 = 'Data/calibration40.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-2.csv'
calib2 = 'Data/calibration40.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:11],0.5*(CL1[0:11]+CL2[0:11]),'-ob')

data1 = 'Data/slot_trial1_noprop.csv'
calib1 = 'Data/calibration36.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_noprop.csv'
calib2 = 'Data/calibration36.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
ax2.plot(alpha1[0:7],0.5*(CL1[0:7]+CL2[0:7]),'k--o')

plt.legend(('+0.18c, +0.22D (Above)','+0.09c, +0.11D (Above)','  0.00c,   0.00D (Centered)',' -0.09c,  -0.11D (Below)',' -0.18c,  -0.22D (Below)','No Propeller'),fontsize=fsize,loc='lower right', frameon=False,)

ax2.set_ylim((0,3.0))
ax2.set_xlim((-1,31))
ax2.set_title('Slotted Flapped Wing',fontsize=fsize, fontweight='bold')
ax2.set_xlabel('Angle of Attack (deg)',fontsize=fsize)
ax2.set_yticks([])

ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['top'].set_visible(False)


#########################

plt.savefig('data.png')
plt.show()