import numpy as np
import string
import matplotlib.pyplot as plt



# def getData(filename):
#     """
#     Parameters
#     ----------
#     filename    :   string
#                     name of data file


#     Outputs
#     -------
#     port:     :   ndarray
#                     Angles of attack for each data point
#     voltage:    :   ndarray
#                     voltages for each data point              
#     """    

#     # Open file and read in
#     f = open(filename, 'r')
#     flines = f.readlines()


#     # # Initialize
#     port = []
#     voltage = []

#     # Read data
#     for i in range(21,len(flines) - 1): 
#         words = string.split(flines[i])
#         # print i, words 
#         port.append(float(words[0]) + 1)
#         voltage.append(float(words[1]))

#     return np.array(port), np.array(voltage)


W1 = np.array([0.75, 1.75, 2.75, 3.75])
W2 = np.array([0.75, 1.75, 2.75, 3.75])
W3 = np.array([0.75, 1.75, 2.75, 3.75])

K = np.matrix(np.zeros((3,3)))
E1 = np.matrix(np.zeros((3,1)))
E2 = np.matrix(np.zeros((3,1)))
E3 = np.matrix(np.zeros((3,1)))

LC1 = np.array([-0.137, -0.376, -0.703, -0.99, 0.012, -0.071, -0.156, -0.239, 0.08, 0.093, 0.091, 0.097 ])
# E1 = np.array([ 0.069, 0.069, 0.069, 0.069, 0.0746, 0.0746, 0.0746, 0.0746, 0.075, 0.075, 0.075, 0.075, ])
LC2 = np.array([ -0.131, -0.129, -0.119, -0.121, -0.131, -0.132, -0.128, -0.133, -0.297, -0.559, -0.837, -1.12])
# E2 = np.array([ -0.12666, -0.12666, -0.12666, -0.12666, -0.12433, -0.12433, -0.12433, -0.12433, -0.1306, -0.1306, -0.1306, -0.1306])
LC3 = np.array([ -0.151, -0.221, -0.32, -0.41, -0.308, -0.6, -0.915, -1.2, -0.085, -0.102, -0.106, -0.119])
# E3 = np.array([ -0.086, -0.086, -0.086, -0.086, -0.093, -0.093, -0.093, -0.093, -0.09133, -0.09133, -0.09133, -0.09133])

K[0,0], E1[0]  = np.polyfit(W1, LC1[0:4],1)
K[1,0], E1[1]  = np.polyfit(W1, LC2[0:4],1)
K[2,0], E1[2]  = np.polyfit(W1, LC3[0:4],1)

K[0,1], E2[0]  = np.polyfit(W2, LC1[4:8],1)
K[1,1], E2[1]  = np.polyfit(W2, LC2[4:8],1)
K[2,1], E2[2]  = np.polyfit(W2, LC3[4:8],1)

K[0,2], E3[0]  = np.polyfit(W3, LC1[8:12],1)
K[1,2], E3[1]  = np.polyfit(W3, LC2[8:12],1)
K[2,2], E3[2]  = np.polyfit(W3, LC3[8:12],1)

# K[0,2], E3[0]  = np.polyfit(W2, LC1[4:8],1)
# K[1,2], E3[1]  = np.polyfit(W2, LC2[4:8],1)
# K[2,2], E3[2]  = np.polyfit(W2, LC3[4:8],1)

# K[0,1], E3[0]  = np.polyfit(W3, LC1[8:12],1)
# K[1,1], E3[1]  = np.polyfit(W3, LC2[8:12],1)
# K[2,1], E3[2]  = np.polyfit(W3, LC3[8:12],1)



E = (E1+E2+E3)/3


invK = np.linalg.inv(K)

a = 3.875/12.0
b = 4.0/12.0

def getForcesMoments(V):
	'''
	returns the output forces based on the calibation curves
	'''
	W = invK*(V-E)
	# print W
	return  float(-1*W[0] - 1*W[1]), float(W[2]), float(a*W[0] - b*W[1])

def getForcesMomentsPropON(V, T, alpha):
	'''
	returns the output forces based on the calibation curves
	'''

	return  invK*(V-E)


# print getForcesMoments(np.matrix([[0.012], [-0.131], [-0.308]]))
# print getForcesMoments(np.matrix([[-.99], [-0.121], [-0.41]]))


