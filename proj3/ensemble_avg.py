# Project 3, Ensemble Averaging
# Sam Friedman, 3/16/2017

from __future__ import print_function
import numpy
import numpy.random
import math
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt

numpy.random.seed(42)  # seed the RNG

def main():
    '''Generate a set of random fluctuations over a period of 1 second
    (x=time, y=u'), 1000 point should be enough. The fluctuation amplitude 
    should be around 3 m/s. The two consecutive data points should fluctuate
    around zero (pos, neg), so the mean of the entire fluctuating data is 
    always zero.'''
    amp = 3
    n = 1000
    imgFmt = 'eps'
    imgFolder = 'img/'
    
    x = numpy.arange(n)
    
    # Generate 1000 random fluctuations over 1 second
    samps = random_flow(amp,n)  # samples 
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(x,samps)  # make a plot
    fig1.savefig(imgFolder+'fluctuations.'+imgFmt, format=imgFmt)
    
    # Generate 50 random observations of sample data
    obs_idx = numpy.random.permutation(n)[0:50]
    obs_idx.sort()
    obs = samps[obs_idx]  # observed samples
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(x,samps)  # make a plot
    ax2.plot(obs_idx,obs,'ro')  # make a plot
    fig2.savefig(imgFolder+'observations.'+imgFmt, format=imgFmt)
    
    # Generate sinusoidal wave
    # amp = 10 m/s, mean = 30 m/s, period = 1000
    sinwave = 10 * numpy.sin(2*numpy.pi/1000 * x) + 30
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.plot(x,sinwave)  # make a plot
    fig3.savefig(imgFolder+'sinwave.'+imgFmt, format=imgFmt)
    
    # Superimpose sine wave over random fluctuations
    signal = sinwave + samps
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(111)
    ax4.plot(x,signal)  # make a plot
    fig4.savefig(imgFolder+'signal.'+imgFmt, format=imgFmt)
    
    # Get 50 observations of signal 
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)
    ax5.plot(x,signal)  
    ax5.plot(obs_idx,signal[obs_idx],'ro')
    fig5.savefig(imgFolder+'signal_obs.'+imgFmt, format=imgFmt)
    
    # Show just the signal observations with the sine wave 
    fig6 = plt.figure()
    ax6 = fig6.add_subplot(111)
    ax6.plot(x,sinwave,'--')  
    ax6.plot(obs_idx,signal[obs_idx],'ro-')
    fig6.savefig(imgFolder+'signal_obs_only.'+imgFmt, format=imgFmt)
    
    # print(samps)
    print('mean=',numpy.mean(samps))
    print('std=',numpy.std(samps))
    print('rms(samps)=',rms(samps))
    print('rms(obs)=',rms(obs))


def rms(u_prime):
    ''' Finds the root mean square of the turbulent perturbations
    of the fluid flow'''
    sq = numpy.square(u_prime)
    N = sq.size
    return numpy.sqrt(sq.sum()/sq.size)
    
def random_flow(amp=3,n=1000,mean=0):
    # round to nearest even number
    n = math.ceil(n/2)*2
    samps = numpy.random.rand(n)*amp+mean
    plusminus = numpy.tile(numpy.array([1,-1]),n/2)
    samps = numpy.multiply(samps, plusminus)
    return samps
    
if __name__ == '__main__':
    main()