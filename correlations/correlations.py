# Correlations assignment
# By Sam Friedman
# 3/24/2017

from __future__ import print_function
import numpy as np
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt
import scipy.signal as spsig
import scipy as sp
import math
from TurbulenceTools import xcorr

np.random.seed(42)  # seed the RNG

def main():
    
    imgFmt = 'eps'
    imgFolder = 'img/'
    dpi = 300
    aspectRatio = (4,3)
    imgMagnifier = 2
    imgSize = tuple(x*imgMagnifier for x in aspectRatio) 
    # imgSize = None 
    
    maxlag = 200
    n = maxlag
    t = np.arange(n)  # time steps
    y1 = 10 + np.sin(t * np.pi/180)
    
    sinewave = 10 * np.sin(np.pi/180 * t) + 30
    # samps = random_flow(maxlag,amp=3)
    samps = np.random.rand(n)*6
    y2 = sinewave + samps
    y3 = np.cumsum(9 + np.random.rand(n))
    y4 = 9 + np.random.rand(n)

    # autocorrelation
    y = y4
    rho = np.zeros(maxlag)
    lags = np.arange(maxlag)
    rho, lags = xcorr(y, norm='coeff', doDetrend=True)
    
    rho = np.delete(rho, range(maxlag-1))
    lags = np.delete(lags, range(maxlag-1))

    plot_corr(lags, rho, imgFmt, imgFolder)

    # plot
    fig = plt.figure()
    plt.plot(t, y)
    plt.xlabel(r'$t$', fontsize=20)
    plt.ylabel(r'$U$', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig(imgFolder+'random_samps.'+imgFmt, format=imgFmt, dpi=300)
    

def plot_corr(lags, rho, imgFmt='png', imgFolder='img/', fname='corr'):
    fig = plt.figure()
    plt.plot(lags, rho)
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig(imgFolder+fname+'.'+imgFmt, format=imgFmt, dpi=300)


def rms(u_prime):
    ''' Finds the root mean square of the turbulent perturbations
    of the fluid flow'''
    sq = np.square(u_prime)
    N = sq.size
    return np.sqrt(sq.sum()/sq.size)
    
    
def random_flow(n=1000,amp=3,mean=0):
    # round to nearest even number
    n = math.ceil(n/2)*2
    samps = np.random.rand(n)*amp+mean
    plusminus = np.tile(np.array([1,-1]),n/2)
    samps = np.multiply(samps, plusminus)
    return samps

    
if __name__ == "__main__":
    main()