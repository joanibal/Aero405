import csv
import matplotlib.pyplot as plt
import numpy as np
import math
from dataProcessing import *

def process(p_dyn, Sref, data, calib, prop):
    """ Processes input wind tunnel data with corresponding calibration functions and outputs lift, drag, and moment curves
    Parameters
    -----------
    p_dyn : float
        tunnel dynamic pressure in inches H2O
    data : string
        data csv file
    calib : string
        calibration csv file
    Sref : float
        wing reference area
    prop : bool
        True if prop on, False if prop off

    Outputs
    ---------
    alpha : ndarray
        AoAs (degrees)
    CL : ndarray
        lift coefficients
    CD : ndarray
        drag coefficients
    CM : ndarray
        moment coefficients
    """
    # Tunnel parameters
    p_dyn = 248.84*p_dyn # Dynamic pressure in Pa
    p = 97900 # Static pressure in Pa
    R = 287
    T = 293 # Temperature in K
    tunnel_density = p/(R*T) # Air density in kg/m^3
    tunnel_V = math.sqrt(p_dyn*2) # Tunnel velocity in m/s

    # Read data file
    reader = csv.DictReader(open(data, 'r'))

    alpha = []
    L = []
    D = []
    M = []

    # Calibrate data and compute lift, drag, moment
    for ii, row in enumerate(reader):
        v = np.matrix([[float(row['LC1:'])], [float(row['LC2:'])], [float(row['LC3:'])]])
        FM = getForcesMoments(v,calib)
        alpha.append(float(row['AoA:']))
        L.append(FM[0])
        D.append(FM[1])
        M.append(FM[2])
    
    alpha = np.array(alpha)
    L = np.array(L)
    D = np.array(D)
    M = np.array(M)

    # Subtract out forces/moments due to propeller (if on)
    if prop is True:
        Lprop = np.array([ 0.26810167,  0.33707469,  0.41038387,  0.47950852,  0.55142573, 0.62236228, 0.69515434,  0.7609083,   0.83491407,  0.90483104,  0.97472401,  1.04151394, 1.10894399,  1.17667928,  1.24386108,  1.3066423,   1.37203376,  1.43610288, 1.4978135,   1.56322995,  1.62292512])
        Dprop = np.array([-1.5082856,  -1.50657452, -1.49741988, -1.48081519, -1.4591998,  -1.44137962, -1.42913541, -1.40319858, -1.38500156, -1.36296934, -1.33807442, -1.30688843, -1.27857726, -1.24409576,-1.21306548, -1.17743631, -1.13918851, -1.10166875, -1.05841559, -1.01318959, -0.96452474])
        Mprop = np.array([ 0.05083867,  0.04978494,  0.04661813,  0.04527882,  0.04040742,  0.03658892,  0.03365973,  0.03031442,  0.02554459,  0.02314167,  0.019416,    0.01499929, 0.01127384,  0.00717226,  0.003357, -0.00226575, -0.00681793, -0.01082327, -0.01621955, -0.01861431, -0.02431079])
        Lrod = 0.0234704
        Drod = 0.12889971
        Mrod = 0.00722212
        L = L - (Lprop-Lrod)
        D = D - (Dprop-Drod)
        M = M - (Mprop-Mrod)

    # Non-dimensionalize into coefficients
    CL = L * 4.44822 / (0.5 * tunnel_density * tunnel_V**2 * Sref)
    CD = D * 4.44822 / (0.5 * tunnel_density * tunnel_V**2 * Sref)
    CM = M * 4.44822 / (0.5 * tunnel_density * tunnel_V**2 * Sref)

    return alpha, CL, CD, CM

def calibPair(datafile):
    """Pairs data file with appropriate calibration data
    Parameters
    ----------
    datafile : str
        Data csv file
    Outputs
    ----------
    icalib : int
        Index corresponding to appropriate calibration file
    """

    reader = csv.DictReader(open(datafile),'r')
    for ii, row in (enumerate(reader)):
        icalib = (int(row['Calib']))
        break

    return icalib
