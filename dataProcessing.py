import numpy as np
import csv
import string
import matplotlib.pyplot as plt

def getCalib(filename):
	"""
	Returns calibration data

	Parameters
	----------
	filename    :   string
					name of data file

	Outputs
	-------
	W1     :   ndarray
		LC1 Weights (lbs)
	W2     :   ndarray
		LC2 Weights (lbs)
	W3     :   ndarray
		LC3 Weights (lbs)
	LC1    :   ndarray
		LC1 Voltages (V)
	LC2    :   ndarray
		LC2 Voltages (V)
	LC3    :   ndarray
		LC3 Voltages (V)      
	"""    
	# Open file and read in
	reader = csv.DictReader(open(filename,'r'))

	# Initialize
	W1 = []
	W2 = []
	W3 = []
	LC1 = []
	LC2 = []
	LC3 = []

	# Extract calibration data
	for ii, row in enumerate(reader):
		LC1.append(float(row['LC1']))
		LC2.append(float(row['LC2']))
		LC3.append(float(row['LC3']))
		W1.append(float(row['W1']))
		W2.append(float(row['W2']))
		W3.append(float(row['W3']))
		for j in range(0,len(W1)-4):
			W1.remove(0)
			W2.remove(0)
			W3.remove(0)
	return np.array(W1), np.array(W2), np.array(W3), np.array(LC1), np.array(LC2), np.array(LC3)

def getForcesMoments(V,calib):
	'''
	returns the output forces based on the calibration curves
	'''
	# Extract calibration data
	W1, W2, W3, LC1, LC2, LC3 = getCalib(calib)

	K = np.matrix(np.zeros((3,3)))
	E1 = np.matrix(np.zeros((3,1)))
	E2 = np.matrix(np.zeros((3,1)))
	E3 = np.matrix(np.zeros((3,1)))

	K[0,0], E1[0]  = np.polyfit(W1, LC1[0:4],1)
	K[1,0], E1[1]  = np.polyfit(W1, LC2[0:4],1)
	K[2,0], E1[2]  = np.polyfit(W1, LC3[0:4],1)

	K[0,1], E2[0]  = np.polyfit(W2, LC1[4:8],1)
	K[1,1], E2[1]  = np.polyfit(W2, LC2[4:8],1)
	K[2,1], E2[2]  = np.polyfit(W2, LC3[4:8],1)

	K[0,2], E3[0]  = np.polyfit(W3, LC1[8:12],1)
	K[1,2], E3[1]  = np.polyfit(W3, LC2[8:12],1)
	K[2,2], E3[2]  = np.polyfit(W3, LC3[8:12],1)

	E = (E1+E2+E3)/3

	invK = np.linalg.inv(K)

	a = 4.0/12.0 # Load cell distances
	b = 4.0/12.0 # Load cell distances

	# Compute forces
	W = invK*(V-E)
	return  float(-1*W[0] - 1*W[2]), float(W[1]), float(a*W[0] - b*W[2])