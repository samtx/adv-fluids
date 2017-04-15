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
    
    imgFmt = 'png'
    imgFolder = 'imgtest/'
    dpi = 300
    aspectRatio = (4,3)
    imgMagnifier = 2
    imgSize = tuple(x*imgMagnifier for x in aspectRatio) 
    # imgSize = None 
    
    maxlag = 500
    n = maxlag
    t = np.arange(n)  # time steps
    y1 = np.sin(t * np.pi/180)
    y5 = np.zeros(n)
    tau = 50
    y5[0:(n-1)-tau] = y1[tau:n-1]
    sinewave = 10 * np.sin(np.pi/180 * t) + 30
    # samps = random_flow(maxlag,amp=3)
    samps = np.random.rand(n)*6 - 3
    y2 = sinewave + samps
    y3 = np.cumsum(9 + np.random.rand(n))
    y6 = (np.random.rand(n)*2-1)
    y4 = 10 + y6
    
    # autocorrelation
    rho = np.zeros(maxlag)
    lags = np.arange(maxlag)
    rho, lags = xcorr(y6, norm='coeff', doDetrend=True)
    
    rho = np.delete(rho, range(maxlag-1))
    lags = np.delete(lags, range(maxlag-1))

    plot_corr(lags, rho, imgFmt, imgFolder, fname='random5_detrend')

    # plot
    fig = plt.figure()
    h1, = plt.plot(t, y1)
    h2, = plt.plot(t, y5)
    plt.xlabel(r'$t$', fontsize=20)
    plt.ylabel(r'$V$', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.legend([h1,h2],[r'$V(t)$',r'$V(t+50) $'],
        loc=4)
    plt.grid(True)
    plt.title(r'Velocity Signals, $\tau=50$', fontsize=18)
    plt.savefig(imgFolder+'signals.'+imgFmt, format=imgFmt, dpi=300)
    
    # plot
    data = np.loadtxt('output.txt')
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=18)
    plt.savefig(imgFolder+'sinewave1.'+imgFmt, format=imgFmt, dpi=300)
    
    # plot
    data = np.loadtxt('output2.txt')
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=18)
    plt.savefig(imgFolder+'sinewave6.'+imgFmt, format=imgFmt, dpi=300)
    
    # plot
    data = np.loadtxt('output3.txt')
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=18)
    plt.savefig(imgFolder+'random2.'+imgFmt, format=imgFmt, dpi=300)
    
        # plot
    data = np.loadtxt('output4.txt')
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=18)
    plt.savefig(imgFolder+'random3.'+imgFmt, format=imgFmt, dpi=300)
    
        # plot
    data = np.loadtxt('output5.txt')
    fig = plt.figure()
    plt.plot(data[:,0], data[:,1])
    plt.plot(np.zeros(lags.shape),'--')
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=18)
    plt.savefig(imgFolder+'sinewave7.'+imgFmt, format=imgFmt, dpi=300)
    

    # plot
    fig = plt.figure()
    plt.plot(t, y4)
    plt.xlabel(r'$t$', fontsize=20)
    plt.ylabel(r'$V$', fontsize=20)
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