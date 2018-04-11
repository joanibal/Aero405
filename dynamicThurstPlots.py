# dynamic thurst characterization thurst plots


import csv
import matplotlib.pyplot as plt
import numpy as np
from dataProcessing import getForcesMoments
from parameters import err

font = {'family': 'Times New Roman'}
plt.rc('font', **font)

data = {}
reader = csv.DictReader(open('DynamicThrust/average_of_tests.csv', 'r'))
data = {}
    
alpha = []
L = []
D = []
M = []

Lhi = []
Dhi = []
Mhi = []

Llo = []
Dlo = []
Mlo = []

for ii, row in enumerate(reader):
    v = np.matrix([[float(row['LC1'])],
                   [float(row['LC2'])],
                   [float(row['LC3'])]])


    FM = getForcesMoments(v)
    FMhi = getForcesMoments(v+ np.matrix([[err], [err], [err]]))
    FMlo = getForcesMoments(v- np.matrix([[err], [err], [err]]))

    alpha.append(float(row['AoA']))

    L.append(FM[0])
    D.append(FM[1])
    M.append(FM[2])

    Lhi.append(FMhi[0])
    Dhi.append(FMhi[1])
    Mhi.append(FMhi[2])

    Llo.append(FMlo[0])
    Dlo.append(FMlo[1])
    Mlo.append(FMlo[2])


data['Alpha'] = np.array(alpha)

data['Lift'] = np.array(L)
data['Lift High Error'] = np.array(Lhi) - np.array(L)
data['Lift Low Error'] = np.array(L) - np.array(Llo)

data['Drag'] = np.array(D)
data['Drag High Error'] = np.array(Dhi) - np.array(D)
data['Drag Low Error'] = np.array(D) - np.array(Dlo)  

data['Moment'] = np.array(M)
data['Moment High Error'] = np.array(Mhi) - np.array([M])
data['Moment Low Error'] = np.array(M) - np.array([Mlo])
# data['Moment'] = np.array(M)



plt.figure(1)
plt.errorbar(data['Alpha'], data['Lift'],  yerr=[data['Lift Low Error'],
                                                 data['Lift High Error']], fmt='-o', label='Force Lift Axis')
plt.errorbar(data['Alpha'], data['Drag'],  yerr=[data['Drag Low Error'],
                                                 data['Drag High Error']], fmt='-o', label='Force Drag Axis')
plt.plot(data['Alpha'], np.sqrt(data['Lift']**2 +
                                data['Drag']**2),   '-o', label='Total Thrust')

plt.legend()
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Forces', fontweight='bold')
plt.savefig('Figures/dynamicThrustForces.png',    bbox_inches='tight')

plt.figure(2)

plt.errorbar(data['Alpha'], data['Moment'],  fmt='-o')

plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Moment', fontweight='bold')
plt.savefig('Figures/dynamicThrustMoment.png',    bbox_inches='tight')





plt.show()


