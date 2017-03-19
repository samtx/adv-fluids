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
    m = 50  # observations
    imgFmt = 'eps'
    imgFolder = 'img/'
    
    x = numpy.arange(n)
    
    # Generate 1000 random fluctuations over 1 second
    samps = random_flow(n,amp)  # samples 
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.plot(x,samps)  # make a plot
    fig1.savefig(imgFolder+'fluctuations.'+imgFmt, format=imgFmt)
    
    # Pick locations for 50 observations
    obs_idx = numpy.random.permutation(n)[0:m]
    obs_idx.sort()
    
    # Generate 50 more samples at each location
    # ... this is the slow way to do it
    samps2d = numpy.expand_dims(samps, axis=1)  # make 2D array
    # print('samps',samps)
    new_samps = numpy.zeros((n,m-1))
    for i in range(m-1):
        print('i=',i)
        new_samps[:,i] = random_flow(n)
    # print('new_samps',new_samps)
    tot_samps = numpy.append(samps2d, new_samps, axis=1)
    # print('tot_samps',tot_samps)
    # print('samps',samps)
    
    
    obs = samps[obs_idx]  # observed samples
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(x,samps)  # make a plot
    ax2.plot(obs_idx,obs,'ro')  # make a plot
    fig2.savefig(imgFolder+'observations.'+imgFmt, format=imgFmt)
    
    # Generate sinusoidal wave
    # amp = 10 m/s, mean = 30 m/s, period = 1000
    sinwave = 10 * numpy.sin(2*numpy.pi/n * x) + 30
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
    
    # Show just the signal observations with the sine wave 
    fig6 = plt.figure()
    ax6 = fig6.add_subplot(111)
    ax6.plot(x,sinwave,'--')  
    ax6.plot(obs_idx,signal[obs_idx],'ro-')
    fig6.savefig(imgFolder+'signal_obs_only.'+imgFmt, format=imgFmt)
    
    # Find root mean square of observed samples
    rootMeanSq = rms(tot_samps)
    totRMS = numpy.tile(rootMeanSq,m)
    totRMS
    # print('rms(tot_samps)',rootMeanSq)
    totMean = numpy.mean(tot_samps,axis=0)
    totSinMean = totMean + sinwave[obs_idx]
    totRMSplus = totSinMean + totRMS
    totRMSminus = totSinMean - totRMS
    print('totMean.shape',totMean.shape)
    print('totSinMean.shape',totSinMean.shape)
    print('totRMS.shape',totRMS.shape)
    print('obs_idx.shape',obs_idx.shape)
    plt.figure()
    # ax = fig.add_subplot(111)
    h1, = plt.plot(x,sinwave,'b-.',linewidth=1.5,label='Base Sine Wave')  
    h2,= plt.plot(x,signal,'b',alpha=0.5,label='Random Fluctuations') 
    h3,= plt.plot(obs_idx,totSinMean,'ro-',label='Observation Means')
    h4, = plt.plot(obs_idx,totRMSplus,'k--',linewidth=1.5,label='Observation RMS')
    plt.plot(obs_idx,totRMSminus,'k--',linewidth=1.5)
    plt.xlabel('Time (ms)')
    plt.ylabel('$U$ m/s')
    # lbls = [lb1,lb2,lb3,lb4]
    lbls = ('Base Sine Wave','Random Fluctuations','Observation Means','Observation RMS')
    plt.legend((h1,h2,h3,h4),lbls,fontsize = 'small')
    plt.savefig(imgFolder+'signal_rms.'+imgFmt, format=imgFmt)
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # h1, = ax.plot(x,sinwave,'b-.',linewidth=1.5,label='Base Sine Wave')  
    # h2, = ax.plot(x,signal,'b',alpha=0.5,label='Random Fluctuations') 
    # h3, = ax.plot(obs_idx,totSinMean,'ro-',label='Observation Means')
    # h4, = ax.plot(obs_idx,totRMSplus,'k--',linewidth=1.5,label='Observation RMS')
    # ax.plot(obs_idx,totRMSminus,'k--',linewidth=1.5)
    # ax.set_xlabel('Time (ms)')
    # ax.set_ylabel('$U$ m/s')
    # ax.legend([h1,h2,h3,h4])
    # #['Base Sine Wave','Random Fluctuations','Observation Means','Observation RMS']
    # fig.savefig(imgFolder+'signal_rms.'+imgFmt, format=imgFmt)
    
    # print(samps)
    # print('mean=',numpy.mean(samps))
    # print('std=',numpy.std(samps))
    # print('rms(samps)=',rms(samps))
    # print('rms(obs)=',rms(obs))


def rms(u_prime):
    ''' Finds the root mean square of the turbulent perturbations
    of the fluid flow'''
    sq = numpy.square(u_prime)
    N = sq.size
    return numpy.sqrt(sq.sum()/sq.size)
    
def random_flow(n=1000,amp=3,mean=0):
    # round to nearest even number
    n = math.ceil(n/2)*2
    samps = numpy.random.rand(n)*amp+mean
    plusminus = numpy.tile(numpy.array([1,-1]),n/2)
    samps = numpy.multiply(samps, plusminus)
    return samps
    
if __name__ == '__main__':
    main()