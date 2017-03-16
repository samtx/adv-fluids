# Orr-Sommerfeld Solution for Plane Poiseuille Flow

from __future__ import print_function
import numpy as np
import scipy.linalg
import matplotlib

# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def calc_orrsommerfeld(alpha, R, N):

    a = np.zeros([N,N])
    b = np.zeros([N,N])

    for m in range(1,N-3):
        print('m=',m)
        ybar = np.cos(m * np.pi/(N-1))
        t = np.zeros([5,N])
        t[0,0] = 1.0
        t[0,1] = ybar
        for ii in range(1,N-1):
            t[0,ii+1] = 2.0*ybar*t[0,ii]-t[1,ii-1]
        for j in range(1,5):
            t[j,0] = 0.0
            t[j,1]=t[j-1,0]
            t[j,2]=4.0*t[j-1,1]
            for k in range(3,N):
                t[j,k]=2.0*(k-1.0)*t[j-1,k-1]+(k-1.0)/(k-2.0)*t[j,k-2]
        
        # Evaluate the base flow at value of ybar
        U = 1.0-ybar**2.0
        dU = -2.0*ybar
        d2U = -2.0
        # set up matrices for Orr-Sommerfeld Equation
        for j in range(N):
            a[N-m,j] = U*(t[2,j]-alpha**2*t[0,j])-d2U*t[0,j]-1.0/(1j*alpha*R)*(t[4,j]-2*alpha**2*t[2,j]+alpha**4*t[0,j])
            b[N-m,j] = t[2,j]-alpha**2*t[1,j]
        
    print(a.shape)    
    # Boundary conditions
    for j in range(N):
        # print('j=',j)
        a[0,j] = 1.0
        a[1,j] = (j-1.0)**2
        a[N-2,j] = (-1.0)**(j-2.0)*(j-1.0)**2.0
        a[N-1,j] = (-1.0)**(j-1.0)
        b[0,j] = 0.0
        b[1,j] = 0.0
        b[N-2,j] = 0.0
        b[N-1, j] = 0.0
        
    # Find eigenvalues c
    V,D = scipy.linalg.eig(a,b)
    # print('D=',D)
    imagc = np.diag(D).imag
    realc = np.diag(D).real
    # fig, ax = plt.subplots()
    plt.plot(realc, imagc, 'o')
    plt.axis([0, 1, -1, 0.1])
    plt.xlabel('c_r')
    plt.ylabel('c_i')
    plt.savefig('orrsom.png', format='png')

    print(realc)
    print(imagc)    

if __name__ == "__main__":
    alpha = 1.0
    R = 10000
    N = 121
    calc_orrsommerfeld(alpha, R, N)