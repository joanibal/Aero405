import csv
import matplotlib.pyplot as plt
import numpy as np
from dataProcessing import getForcesMoments

font = {'family': 'Times New Roman'}

plt.rc('font', **font)

data = {}

tunnel_V = 11.2 # m/s
tunnel_density = 97900.496 / (287 * 294.2)  # kg/m^3

for tunnel in np.array([0 ,300]):
    data[tunnel] = {}
    for prop in np.array([0 , 2300]):
        data[tunnel][prop] = {}
        for height in xrange(-1, 2):
            
            try:
                
                reader = csv.DictReader(open('Phase1_Data/height' + str(height)+'_tunnel'+str(tunnel)+'_prop'+str(prop)+'.csv', 'r'))
                data[tunnel][prop][height] = {}
                
            except :
                print('could open ' + 'Phase1_Data/height' + str(height) +
                      '_tunnel' + str(tunnel) + '_prop' + str(prop) + '.csv')
                continue
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
                v = np.matrix([[float(row['LC1'])], [
                            float(row['LC2'])], [float(row['LC3'])]])
                # print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
                # print v
                FM = getForcesMoments(v)
                FMhi = getForcesMoments(v+ np.matrix([[err], [err], [err]]) )
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
                
            data[tunnel][prop][height]['Alpha'] = np.array(alpha)

            data[tunnel][prop][height]['Lift'] = np.array(L)

            data[tunnel][prop][height]['Drag'] = np.array(D) 

            data[tunnel][prop][height]['Moment'] = np.array(M)      

legend = []
for key in data[300][2300].keys():

    plt.figure(1)
    plt.errorbar(data[300][2300][key]['Alpha'], data[300][2300][key]['CL'] - data[0][2300][key]['CL'],  yerr=[data[300][2300][key]['CL Low Error'], data[300][2300][key]['CL High Error']], fmt='-o' )

    plt.figure(2)
    plt.errorbar(data[300][2300][key]['Alpha'], data[300][2300][key]['CD'] - data[0][2300][key]['CD'],  yerr=[data[300][2300][key]['CD Low Error'], data[300][2300][key]['CD High Error']], fmt='-o' )

    legend.append(str(key)+ '" Prop Height')
    print(key)
    # print(data[300][2300][key]['CL'])data[300][2300][key]['CL'] - data[0][2300][key]['CL']
    print(np.max(data[300][2300][key]['CL'] - data[0][2300][key]['CL']))

legend.append('No Prop')
plt.figure(1)
# plt.plot(data[300][0][0]['Alpha'], data[300][0][0]['CL'], 'k-o')
plt.errorbar(data[300][0][0]['Alpha'], data[300][0][0]['CL'],  yerr=[data[300][0][0]['CL Low Error'], data[300][0][0]['CL High Error']], fmt='k-o' )
plt.legend(legend)
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Coefficient of Lift', fontweight='bold')
plt.savefig('Figures/CL_Alpha.png',     bbox_inches='tight')

plt.figure(2)
plt.errorbar(data[300][0][0]['Alpha'], data[300][0][0]['CD'],  yerr=[data[300][0][0]['CD Low Error'], data[300][0][0]['CD High Error']], fmt='k-o' )

# plt.plot(data[300][0][0]['Alpha'], data[300][0][0]['CD'], 'k-o')
plt.legend(legend)
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Coefficient of Drag', fontweight='bold')
plt.savefig('Figures/CD_Alpha.png',    bbox_inches='tight')

# plt.show()
alpha_xfoil = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 18])
CL_xfoil = np.array([0.2691, 0.4268, 0.5201, 0.6143, 0.7078, 0.8008, 0.8911, 0.973, 1.0413, 1.1025, 1.1951, 1.2297, 1.233, 1.2118, 1.1486, 0.855])

plt.figure(3)
plt.errorbar(data[300][0][0]['Alpha'], data[300][0][0]['CL'],  yerr=[data[300][0][0]['CL Low Error'], data[300][0][0]['CL High Error']], fmt='k-o' )
plt.plot(alpha_xfoil, CL_xfoil, 'r-o')
plt.legend(legend)
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Coefficient of Lift', fontweight='bold')
plt.savefig('Figures/CL_Alpha_xfoil.png',     bbox_inches='tight')

plt.show()
print('Done')