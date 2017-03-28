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
from TurbulenceTools import xcorr

np.random.seed(42)  # seed the RNG

def main():
    
    imgFmt = 'png'
    dpi = 300
    aspectRatio = (4,3)
    imgMagnifier = 2
    imgSize = tuple(x*imgMagnifier for x in aspectRatio) 
    # imgSize = None 
    imgFolder = 'imgtest/'
    
    maxlag = 530
    t = np.arange(maxlag)  # time steps
    y = np.sin(t * np.pi/180)
    
    
    # autocorrelation
    rho = np.zeros(maxlag)
    lags = np.arange(maxlag)
    rho, lags = xcorr(y, norm='coeff')
    # for t in range(maxlag):
    #     # print(t)
    #     ary = np.array([y[0:len(y)-t], y[t:len(y)]])
    #     rho[t] = np.corrcoef(ary)[0][1]

    # remove negative values
        
    print(y.shape)
    print(rho.shape)
    print(lags.shape)
    
    rho = np.delete(rho, range(maxlag-1))
    lags = np.delete(lags, range(maxlag-1))
    
    print(y.shape)
    print(rho.shape)
    print(lags.shape)
    # y_detrend = spsig.detrend(y)
    # R = np.corrcoef(y)
    # lag = np.argmax(R)
    
    # plot
    fig = plt.figure()
    # fig = plt.figure(figsize=imgSize)
    ax = fig.add_subplot(121)
    ax.plot(lags, rho)
    ax.plot(lags,y,'--')
    
    
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    fig.savefig(imgFolder+'sinewave4.'+imgFmt, format=imgFmt, dpi=300)

    
    
if __name__ == "__main__":
    main()