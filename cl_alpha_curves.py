import csv
import matplotlib.pyplot as plt
import numpy as np
from dataProcessing import getForcesMoments

data = {}

tunnel_V = 10.64 # m/s
tunnel_density = 97900.496 / (283 * 294.2)  # kg/m^3
Sref = 0.154838  # m^2


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

            for ii, row in enumerate(reader):
                v = np.matrix([[float(row['LC1'])], [
                            float(row['LC2'])], [float(row['LC3'])]])
                # print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
                # print v
                FM = getForcesMoments(v)

                alpha.append(float(row['AoA']))

                L.append(FM[0])
                D.append(FM[1])
                M.append(FM[2])
                # quit()
                # w = np.array([float(row['W1']),float(row['W2']) ,float(row['W3']) ])
            data[tunnel][prop][height]['Alpha'] = np.array(alpha)
            data[tunnel][prop][height]['Lift'] = np.array(L)
            data[tunnel][prop][height]['Drag'] = np.array(D)
            data[tunnel][prop][height]['Moment'] = np.array(M)

            data[tunnel][prop][height]['CL'] = np.array(
                L) * 4.44822 / (0.5 * tunnel_density * tunnel_V**2 * Sref)
            data[tunnel][prop][height]['CD'] = np.array(
                D) * 4.44822 / (0.5 * tunnel_density * tunnel_V**2 * Sref)
            # data[tunnel][prop][height]['Moment'] = np.array(M)
            

legend = []
for key in data[300][2300].keys():

    plt.figure(1)
    plt.plot(data[300][2300][key]['Alpha'], data[300][2300]
             [key]['CL'] - data[0][2300][key]['CL'], '-o')

    plt.figure(2)
    plt.plot(data[300][2300][key]['Alpha'], data[300][2300]
             [key]['CD'] - data[0][2300][key]['CD'], '-o')

    legend.append(str(key)+ '" Prop Height')
    # print key

legend.append('No Prop')
plt.figure(1)
plt.plot(data[300][0][0]['Alpha'], data[300][0][0]['CL'], 'k-o')
plt.legend(legend)
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Coefficient of Lift', fontweight='bold')
plt.savefig('Figures/CL_Alpha.png',     bbox_inches='tight')


plt.figure(2)
plt.plot(data[300][0][0]['Alpha'], data[300][0][0]['CD'], 'k-o')
plt.legend(legend)
plt.xlabel('Angle of Attack [Deg]', fontweight='bold')
plt.ylabel('Coefficient of Drag', fontweight='bold')
plt.savefig('Figures/CD_Alpha.png',    bbox_inches='tight')



plt.show()

print('Done')
