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
    
    # for t in range(maxlag):
    #     # print(t)
    #     ary = np.array([y[0:len(y)-t], y[t:len(y)]])
    #     rho[t] = np.corrcoef(ary)[0][1]

    # remove negative values
        
    # print(y.shape)
    # print(rho.shape)
    # print(lags.shape)
    
    rho = np.delete(rho, range(maxlag-1))
    lags = np.delete(lags, range(maxlag-1))
    
    # print(y.shape)
    # print(rho.shape)
    # print(lags.shape)
    # y_detrend = spsig.detrend(y)
    # R = np.corrcoef(y)
    # lag = np.argmax(R)
    
    # plot
    fig = plt.figure()
    # fig = plt.figure(figsize=imgSize)
    # ax = fig.add_subplot(121)
    plt.plot(lags, rho)
    plt.plot(np.zeros(maxlag),'--')
    # h2, = plt.plot(lags,y,'--')
    # plt.plot(obs_idx,totSinMean - obsRMS,'k--',linewidth=1.5)
    plt.xlabel(r'$\tau$', fontsize=22)
    plt.ylabel(r'$\rho$', fontsize=22)
    plt.title(r'Correlation with Increasing Time Lag', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig(imgFolder+'random.'+imgFmt, format=imgFmt, dpi=300)
    
    # plot
    fig = plt.figure()
    # fig = plt.figure(figsize=imgSize)
    # ax = fig.add_subplot(121)
    plt.plot(t, y)
    # plt.plot(np.zeros(maxlag),'--')
    # h2, = plt.plot(lags,y,'--')
    # plt.plot(obs_idx,totSinMean - obsRMS,'k--',linewidth=1.5)
    plt.xlabel(r'$t$', fontsize=20)
    plt.ylabel(r'$U$', fontsize=20)
    # plt.title(r'Correlation with Increasing Time Lag', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig(imgFolder+'random_samps.'+imgFmt, format=imgFmt, dpi=300)

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