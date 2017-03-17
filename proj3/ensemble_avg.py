# Project 3, Ensemble Averaging
# Sam Friedman, 3/16/2017

import numpy
import numpy.random
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    '''Generate a set of random fluctuations over a period of 1 second
    (x=time, y=u'), 1000 point should be enough. The fluctuation amplitude 
    should be around 3 m/s. The two consecutive data points should fluctuate
    around zero (pos, neg), so the mean of the entire fluctuating data is 
    always zero.'''
    amp = 3
    n = 1000
    imgFmt = 'png'
    
    # Generate 1000 random fluctuations over 1 second
    samps = random_flow(amp,n)  # samples 
    
    # Generate 50 random observations of sample data
    obs_idx = numpy.random.permutation(n)[0:50]
    
    
    

    
    # print(samps)
    print('mean=',numpy.mean(samps))
    print('std=',numpy.std(samps))
    x = numpy.arange(n)
    plt.plot(x,samps)
    plt.savefig('ensemble.'+imgFmt, format=imgFmt)
    
def random_flow(amp=3,n=1000,mean=0):
    # round to nearest even number
    n = math.ceil(n/2)*2
    samps = numpy.random.rand(n)*amp/2+mean
    plusminus = numpy.tile(numpy.array([1,-1]),n/2)
    samps = numpy.multiply(samps, plusminus)
    return samps
    
if __name__ == '__main__':
    main()