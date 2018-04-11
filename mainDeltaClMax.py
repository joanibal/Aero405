import numpy as np 
import matplotlib.pyplot as plt
import csv
from postProcessing import *
import scipy as sp
import scipy.stats
""" Main script for generating plots from wind tunnel data"""

# Plot setup
font = {'family': 'Times New Roman',
        'size': 18}
plt.rc('font', **font)
# fsize = 16
# plt.rc('xtick', labelsize=fsize) 
# plt.rc('ytick', labelsize=fsize)
# plt.figure()

p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True


def mean_confidence_interval(data, confidence=0.90):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
     
    return m, h

##################

""" Plain wing """ 


Clmax = np.array([])
ErrorBars = np.array([])
data1 = 'Data/clean_trial5_+2.csv'
calib1 = 'Data/calibration10.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_+2.csv'
calib2 = 'Data/calibration10.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:14]), max(CL2[0:14])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)


data1 = 'Data/clean_trial4_+1.csv'
calib1 = 'Data/calibration15.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_+1.csv'
calib2 = 'Data/calibration15.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:14]), max(CL2[0:14])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)



data1 = 'Data/clean_trial4_0.csv'
calib1 = 'Data/calibration19.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_0.csv'
calib2 = 'Data/calibration19.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:15]), max(CL2[0:15])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)



data1 = 'Data/clean_trial4_-1.csv'
calib1 = 'Data/calibration17.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_-1.csv'
calib2 = 'Data/calibration17.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:15]), max(CL2[0:15])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)



data1 = 'Data/clean_trial5_-2.csv'
calib1 = 'Data/calibration13.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial6_-2.csv'
calib2 = 'Data/calibration13.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)


avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:15]), max(CL2[0:15])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)


data1 = 'Data/clean_trial4_noprop.csv'
calib1 = 'Data/calibration21.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/clean_trial5_noprop.csv'
calib2 = 'Data/calibration21.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)




propHieghts = np.array([ 2, 1, 0 ,-1, -2])/9.0
propHieghtsChord = np.array([ 2, 1, 0 ,-1, -2])/12.0
deltaClmax = Clmax - max(0.5*(CL1[0:14]+CL2[0:14]))




print Clmax, deltaClmax




fig = plt.figure(figsize=(15,9))
ax1 = fig.add_subplot(111)
print propHieghts,deltaClmax,[ErrorBars]
ax1.errorbar(propHieghts,deltaClmax,yerr=[ErrorBars, ErrorBars], fmt='-o', capsize=10, markersize=10)


# plt.ylim((0,2.5))
# plt.xlim((0,30))
ax1.set_xlim(np.array([ 2.5, -2.5])/9.0)

ax1.set_xlabel('Prop Position (Fracation of Prop Diameter)')
ax1.set_xticks(propHieghts)
ax1.set_xticklabels(np.round(propHieghts, 2))
ax1.set_ylabel(r'$\Delta C_{L_{max}}$', labelpad=25, rotation=0, fontsize=24)
ax2 = ax1.twiny()

ax2.set_xlim(np.array([ 2.5, -2.5])/12.0)
ax2.set_xlabel('Prop Position (Fracation of Chord)')
ax2.set_xticks(propHieghtsChord)
ax2.set_xticklabels(np.round(propHieghtsChord, 2))

plt.suptitle(r'$\Delta C_{L_{max}}$' + ' Increase for Each Configuration', fontweight='bold')

ax1.annotate('Clean Wing', xy=(propHieghts[0],deltaClmax[0]), xytext=(propHieghts[0]+ .0375, deltaClmax[0]+ 0.075), color='C0', fontweight='bold')


#################################

"""Plain flapped wing Trials 1,2"""
Clmax = np.array([])
ErrorBars = np.array([])

data1 = 'Data/plain_trial1_+2.csv'
calib1 = 'Data/calibration33.csv'
p_dyn1 = 0.29
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+2.csv'
calib2 = 'Data/calibration33.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:11]), max(CL2[0:11])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/plain_trial1_+1.csv'
calib1 = 'Data/calibration29.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_+1.csv'
calib2 = 'Data/calibration29.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:10]), max(CL2[0:10])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data2 = 'Data/plain_trial2_0.csv'
calib2 = 'Data/calibration25.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

data3 = 'Data/plain_trial3_0.csv'
calib3 = 'Data/calibration25.csv'
[alpha3, CL3, CD3, CM3] = process(p_dyn1, Sref1, data3, calib3, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:10]), max(CL2[0:10])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/plain_trial1_-1.csv'
calib1 = 'Data/calibration27.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-1.csv'
calib2 = 'Data/calibration27.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:11]), max(CL2[0:11])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/plain_trial1_-2.csv'
calib1 = 'Data/calibration31.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_-2.csv'
calib2 = 'Data/calibration31.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:12]), max(CL2[0:12])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/plain_trial1_noprop.csv'
calib1 = 'Data/calibration23.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/plain_trial2_noprop.csv'
calib2 = 'Data/calibration35.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)



print Clmax, deltaClmax
deltaClmax = Clmax - max(0.5*(CL1[0:9]+CL2[0:9]))
ax1.errorbar(propHieghts,deltaClmax,yerr=[ErrorBars, ErrorBars], fmt='-o', capsize=15, markersize=10)

ax1.annotate('Plain Flapped Wing', xy=(propHieghts[2],deltaClmax[2]), xytext=(propHieghts[2] - .025, deltaClmax[2]- 0.03), color='C1', fontweight='bold')


###########################

"""Slotted flapped wing Trials 1,2"""
Clmax = np.array([])
ErrorBars = np.array([])


data1 = 'Data/slot_trial1_+2.csv'
calib1 = 'Data/calibration39.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+2.csv'
calib2 = 'Data/calibration39.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:10]), max(CL2[0:10])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/slot_trial1_+1.csv'
calib1 = 'Data/calibration44.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_+1.csv'
calib2 = 'Data/calibration44.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:10]), max(CL2[0:10])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/slot_trial1_0.csv'
calib1 = 'Data/calibration46.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_0.csv'
calib2 = 'Data/calibration46.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:11]), max(CL2[0:11])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/slot_trial1_-1.csv'
calib1 = 'Data/calibration42.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-1.csv'
calib2 = 'Data/calibration42.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:11]), max(CL2[0:11])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/slot_trial1_-2.csv'
calib1 = 'Data/calibration40.csv'
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_-2.csv'
calib2 = 'Data/calibration40.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)

avgCLmax, errorBars = mean_confidence_interval([max(CL1[0:11]), max(CL2[0:11])])
ErrorBars = np.append(ErrorBars, errorBars)
Clmax = np.append(Clmax, avgCLmax)




data1 = 'Data/slot_trial1_noprop.csv'
calib1 = 'Data/calibration36.csv'
prop1 = False
[alpha1, CL1, CD1, CM1] = process(p_dyn1, Sref1, data1, calib1, prop1)

data2 = 'Data/slot_trial2_noprop.csv'
calib2 = 'Data/calibration36.csv'
[alpha2, CL2, CD2, CM2] = process(p_dyn1, Sref1, data2, calib2, prop1)



print Clmax, deltaClmax
# ax1.plot(propHieghts,deltaClmax )
deltaClmax = Clmax - max(0.5*(CL1[0:7]+CL2[0:7]))
ax1.errorbar(propHieghts,deltaClmax,yerr=[ErrorBars, ErrorBars], fmt='-o', capsize=15, markersize=10)


ax1.annotate('Slotted Flapped Wing', xy=(propHieghts[2],deltaClmax[2]), xytext=(propHieghts[2] + .19, deltaClmax[2]), color='C2', fontweight='bold')





#########################

plt.savefig('clmaxComp.png')
plt.show()