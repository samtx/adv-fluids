# Project 3, Ensemble Averaging
# Sam Friedman, 3/16/2017

import numpy
import numpy.random
import math
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt


def main():
    '''Generate a set of random fluctuations over a period of 1 second
    (x=time, y=u'), 1000 point should be enough. The fluctuation amplitude 
    should be around 3 m/s. The two consecutive data points should fluctuate
    around zero (pos, neg), so the mean of the entire fluctuating data is 
    always zero.'''
    amp = 3
    n = 1000
    imgFmt = 'svg'
    
    x = numpy.arange(n)
    
    # Generate 1000 random fluctuations over 1 second
    samps = random_flow(amp,n)  # samples 
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(x,samps)  # make a plot
    fig1.savefig('fluctuations.'+imgFmt, format=imgFmt)
    
    # Generate 50 random observations of sample data
    obs_idx = numpy.random.permutation(n)[0:50]
    obs = samps[obs_idx]  # observed samples
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(x,samps)  # make a plot
    ax2.plot(obs_idx,obs,'o')  # make a plot
    fig2.savefig('observations.'+imgFmt, format=imgFmt)
    
    # Generate sinusoidal wave
    # amp = 10 m/s, mean = 30 m/s, period = 1000
    sinwave = 10 * numpy.sin(2*numpy.pi/1000 * x) + 30
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(x,sinwave)  # make a plot
    fig3.savefig('sinwave.'+imgFmt, format=imgFmt)
    
    # Superimpose sine wave over random fluctuations
    signal = sinwave + samps
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x,signal)  # make a plot
    fig4.savefig('signal.'+imgFmt, format=imgFmt)
    
    # Get 50 observations of signal 
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)
    ax5.plot(x,signal)  
    ax5.plot(obs_idx,signal[obs_idx],'o')
    fig5.savefig('signal_obs.'+imgFmt, format=imgFmt)
    
    # print(samps)
    print('mean=',numpy.mean(samps))
    print('std=',numpy.std(samps))

    
def random_flow(amp=3,n=1000,mean=0):
    # round to nearest even number
    n = math.ceil(n/2)*2
    samps = numpy.random.rand(n)*amp+mean
    plusminus = numpy.tile(numpy.array([1,-1]),n/2)
    samps = numpy.multiply(samps, plusminus)
    return samps
    
if __name__ == '__main__':
    main()