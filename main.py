import numpy as np 
import matplotlib.pyplot as plt
import csv
from postProcessing import *

""" Main script for generating plots from wind tunnel data"""

# Plot setup
font = {'family': 'Times New Roman'}
plt.rc('font', **font)

# Read in proper calibration files - NOT WORKING YET
# reader = csv.DictReader(open('Data/clean_trial1_+1.csv'),'r')
# for ii, row in (enumerate(reader)):
#     print(row['LC1:'])
#     #break

# data = 'Data/clean_trial1_-1.csv'
# calib = 'Data/calibration' + str(calibPair(data)) + '.csv'
# print(calib)

#Trial 1
plt.figure(1)
data1 = 'Data/clean_trial1_noprop.csv'
calib1 = 'Data/calibration3.csv'
p_dyn1 = 0.29
Sref1 = 0.154838  # m^2
prop1 = False
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL,'k--')

data1 = 'Data/clean_trial1_+2.csv'
calib1 = 'Data/calibration4.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial1_+1.csv'
calib1 = 'Data/calibration1.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial1_0.csv'
calib1 = 'Data/calibration2.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial1_-1.csv'
calib1 = 'Data/calibration1.csv'
p_dyn1 = 0.285
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial1_-2.csv'
calib1 = 'Data/calibration4.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

plt.legend(('No Prop', '+2"', '+1"', '0"', '-1"', '-2"'),fontsize=12)
plt.title('Trial 1 - Clean Wing',fontsize=12)
plt.xlabel('Alpha (deg)'fontsize=12)
plt.ylabel('$C_L$',fontsize=12)

# Trial 2
plt.figure(2)
data2 = 'Data/clean_trial1_noprop.csv'
calib2 = 'Data/calibration3.csv'
p_dyn2 = 0.29
Sref2 = 0.154838  # m^2
prop2 = False
[alpha, CL, CD, CM] = process(p_dyn2, Sref2, data2, calib2, prop2)
plt.plot(alpha,CL,'k--')

data1 = 'Data/clean_trial2_+2.csv'
calib1 = 'Data/calibration5.csv'
p_dyn1 = 0.31
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial2_+1.csv'
calib1 = 'Data/calibration1.csv'
p_dyn1 = 0.31
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial2_0.csv'
calib1 = 'Data/calibration2.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial2_-1.csv'
calib1 = 'Data/calibration1.csv'
p_dyn1 = 0.285
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial2_-2.csv'
calib1 = 'Data/calibration5.csv'
p_dyn1 = 0.295
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

plt.legend(('No Prop', '+2"', '+1"', '0"', '-1"', '-2"'),fontsize=12)
plt.title('Trial 2 - Clean Wing',fontsize=12)
plt.xlabel('Alpha (deg)',fontsize=12)
plt.ylabel('$C_L$',fontsize=12)

# # Trial 3
plt.figure(3)
data2 = 'Data/clean_trial1_noprop.csv'
calib2 = 'Data/calibration3.csv'
p_dyn2 = 0.29
Sref2 = 0.154838  # m^2
prop2 = False
[alpha, CL, CD, CM] = process(p_dyn2, Sref2, data2, calib2, prop2)
plt.plot(alpha,CL,'k--')

data1 = 'Data/clean_trial3_+2.csv'
calib1 = 'Data/calibration7.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial3_+1.csv'
calib1 = 'Data/calibration6.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial3_0.csv'
calib1 = 'Data/calibration6.csv'
p_dyn1 = 0.30
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial3_-1.csv'
calib1 = 'Data/calibration6.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

data1 = 'Data/clean_trial3_-2.csv'
calib1 = 'Data/calibration7.csv'
p_dyn1 = 0.3
Sref1 = 0.154838  # m^2
prop1 = True
[alpha, CL, CD, CM] = process(p_dyn1, Sref1, data1, calib1, prop1)
plt.plot(alpha,CL)

plt.legend(('No Prop', '+2"', '+1"', '0"', '-1"', '-2"'),fontsize=12)
plt.title('Trial 3 - Clean Wing',fontsize=12)
plt.xlabel('Alpha (deg)',fontsize=12)
plt.ylabel('$C_L$',fontsize=12)

plt.show()