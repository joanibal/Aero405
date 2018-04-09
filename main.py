import numpy as np 
import matplotlib.pyplot as plt
import csv
from postProcessing import *

""" Main script for generating plots from wind tunnel data"""

# Plot setup
font = {'family': 'Arial'}
plt.rc('font', **font)
fsize = 16
plt.rc('xtick', labelsize=fsize) 
plt.rc('ytick', labelsize=fsize)
plt.figure()

##################

""" Plain wing """ 

plt.subplot(1,3,1)

data1 = 'Data/clean_trial5_+2.csv'
calib1 = 'Data/calibration10.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_+2.csv'
calib2 = 'Data/calibration11.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0,0])

data1 = 'Data/clean_trial4_+1.csv'
calib1 = 'Data/calibration15.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_+1.csv'
calib2 = 'Data/calibration16.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0.65,0])

data1 = 'Data/clean_trial4_0.csv'
calib1 = 'Data/calibration19.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)


data2 = 'Data/clean_trial5_0.csv'
calib2 = 'Data/calibration20.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'g')

data1 = 'Data/clean_trial4_-1.csv'
calib1 = 'Data/calibration17.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_-1.csv'
calib2 = 'Data/calibration18.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'c')

data1 = 'Data/clean_trial5_-2.csv'
calib1 = 'Data/calibration13.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_-2.csv'
calib2 = 'Data/calibration14.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'b')

data1 = 'Data/clean_trial4_noprop.csv'
calib1 = 'Data/calibration21.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_noprop.csv'
calib2 = 'Data/calibration22.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'k--')

plt.legend(('+2"','+1"','0"','-1"','-2"','No prop'),fontsize=fsize,loc='lower right')
plt.ylim((0,2.5))
plt.title('Clean Wing',fontsize=fsize)
plt.xlabel('Alpha (deg)',fontsize=fsize)
plt.ylabel('$C_L$',fontsize=fsize)

#################################

"""Plain flapped wing Trials 1,2"""
plt.subplot(1,3,2)

data1 = 'Data/plain_trial1_+2.csv'
calib1 = 'Data/calibration33.csv'
p_dyn1 = 0.29
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+2.csv'
calib2 = 'Data/calibration34.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0,0])

data1 = 'Data/plain_trial1_+1.csv'
calib1 = 'Data/calibration29.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+1.csv'
calib2 = 'Data/calibration30.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0.65,0])

data2 = 'Data/plain_trial2_0.csv'
calib2 = 'Data/calibration25.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

data3 = 'Data/plain_trial3_0.csv'
calib3 = 'Data/calibration26.csv'
[alpha3, CL3, CD3, CM3] = process(p_dyn1, Sref1, data3, calib3, prop1)
plt.plot(alpha3,0.5*(CL2+CL3),'g')

data1 = 'Data/plain_trial1_-1.csv'
calib1 = 'Data/calibration27.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-1.csv'
calib2 = 'Data/calibration28.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'c')

data1 = 'Data/plain_trial1_-2.csv'
calib1 = 'Data/calibration31.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-2.csv'
calib2 = 'Data/calibration32.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'b')

data1 = 'Data/plain_trial1_noprop.csv'
calib1 = 'Data/calibration23.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_noprop.csv'
calib2 = 'Data/calibration35.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha2,0.5*(CL1[0:11]+CL2),'k--')

plt.legend(('+2"','+1"','0"','-1"','-2"','No prop'),fontsize=fsize,loc='lower right')
plt.ylim((0,2.5))
plt.title('Plain Flapped Wing',fontsize=fsize)
plt.xlabel('Alpha (deg)',fontsize=fsize)
plt.ylabel('$C_L$',fontsize=fsize)

###########################

"""Slotted flapped wing Trials 1,2"""
plt.subplot(1,3,3)

data1 = 'Data/slot_trial1_+2.csv'
calib1 = 'Data/calibration38.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+2.csv'
calib2 = 'Data/calibration39.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0,0])

data1 = 'Data/slot_trial1_+1.csv'
calib1 = 'Data/calibration44.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+1.csv'
calib2 = 'Data/calibration45.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),color=[1,0.65,0])

data1 = 'Data/slot_trial1_0.csv'
calib1 = 'Data/calibration46.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_0.csv'
calib2 = 'Data/calibration47.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'g')

data1 = 'Data/slot_trial1_-1.csv'
calib1 = 'Data/calibration42.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-1.csv'
calib2 = 'Data/calibration43.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'c')

data1 = 'Data/slot_trial1_-2.csv'
calib1 = 'Data/calibration40.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-2.csv'
calib2 = 'Data/calibration41.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'b')

data1 = 'Data/slot_trial1_noprop.csv'
calib1 = 'Data/calibration36.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_noprop.csv'
calib2 = 'Data/calibration37.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)
plt.plot(alpha1,0.5*(CL1+CL2),'k--')

plt.legend(('+2"','+1"','0"','-1"','-2"','No prop'),fontsize=fsize,loc='lower right')
plt.ylim((0,2.5))
plt.title('Slotted Flapped Wing',fontsize=fsize)
plt.xlabel('Alpha (deg)',fontsize=fsize)
plt.ylabel('$C_L$',fontsize=fsize)

plt.show()

#########################