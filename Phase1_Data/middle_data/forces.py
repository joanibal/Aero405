from dataProcessing import *
import csv
import matplotlib.pyplot as plt

# reader = csv.DictReader(open('0spacing_0tunnel_2300.csv', 'r'))
# for ii, row in enumerate(reader):
# 	v = np.matrix([[float(row['LC1 (V)'])],[float(row['LC2 (V)'])] , [float(row['LC3 (V)'])] ]) 
# 	# print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
# 	print v
# 	print getForcesMoments(v)
# 	break
# 	# w = np.array([float(row['W1']),float(row['W2']) ,float(row['W3']) ])




reader = csv.DictReader(open('0spacing_0tunnel_2300.csv', 'r'))

alpha = []
Lprop = []
Dprop = []
Mprop = []

for ii, row in enumerate(reader):
	v = np.matrix([[float(row['LC1 (V)'])],[float(row['LC2 (V)'])] , [float(row['LC3 (V)'])] ]) 
	# print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
	# print v
	FM =  getForcesMoments(v)

	alpha.append(float(row['AoA (deg)']))

	Lprop.append(FM[0])
	Dprop.append(FM[1])
	Mprop.append(FM[2])
	# quit()
	# w = np.array([float(row['W1']),float(row['W2']) ,float(row['W3']) ])


plt.plot(alpha, Lprop)
plt.plot(alpha,Dprop)
plt.plot(alpha,np.sqrt(np.array(Dprop)**2 + np.array(Lprop)**2))
plt.title('Prop On Tunnel off')
plt.xlabel('Angle of Attack')
plt.ylabel('Force [lbf]')
plt.legend(['L','D'])
plt.show()

reader = csv.DictReader(open('0spacing_300tunnel_0.csv', 'r'))

alpha = []
L = []
D = []
M = []

for ii, row in enumerate(reader):
	v = np.matrix([[float(row['LC1'])],[float(row['LC2'])] , [float(row['LC3'])] ]) 
	# print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
	# print v
	FM =  getForcesMoments(v)

	alpha.append(float(row['AoA']))

	L.append(FM[0])
	D.append(FM[1])
	M.append(FM[2])
	# quit()
	# w = np.array([float(row['W1']),float(row['W2']) ,float(row['W3']) ])


plt.plot(alpha, L)
plt.plot(alpha,D)
plt.title('Prop Off Tunnel 300')
plt.xlabel('Angle of Attack')
plt.ylabel('Force [lbf]')
plt.legend(['L','D'])
plt.show()


reader = csv.DictReader(open('0spacing_300tunnel_2300.csv', 'r'))

alpha = []
L = []
D = []
M = []

for ii, row in enumerate(reader):
	v = np.matrix([[float(row['LC1'])],[float(row['LC2'])] , [float(row['LC3'])] ]) 
	# print np.matrix([float(row['LC1']),float(row['LC2']) ,float(row['LC3']) ]) , np.matrix([float(row['E1']),float(row['E2']) ,float(row['E3']) ])
	# print v
	FM =  getForcesMoments(v)

	alpha.append(float(row['AoA']))

	L.append(FM[0])
	D.append(FM[1])
	M.append(FM[2])
	# quit()
	# w = np.array([float(row['W1']),float(row['W2']) ,float(row['W3']) ])


plt.plot(alpha, np.array(L) - np.array(Lprop))
plt.plot(alpha, np.array(D) - np.array(Dprop))
plt.title('Prop On Tunnel 300')
plt.xlabel('Angle of Attack')
plt.ylabel('Force [lbf]')
plt.legend(['L','D'])
plt.show()

