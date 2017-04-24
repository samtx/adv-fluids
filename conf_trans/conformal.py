# Conformal Transformation
# Ch. 6 Assignment 
# Sam Friedman
# 4/21/2017

import numpy as np
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt

from numpy import cos, sin, pi

def main():
    
    U_inf=1     # flow velocity
    R=1         # cylinder radius

    # Stream functions
    def Phi(r, theta):
        return U_inf*(r+R**2/r)*cos(theta)
        
    def Psi(r, theta):
        return U_inf*(r-R**2/r)*sin(theta)

    # Potential Function
    def F(r, theta):
        return Phi(r, theta) + 1j*Psi(r, theta)    
        
    def Cp(theta):
        return 1-4*sin(theta)**2
        
    r=np.linspace(R,R*5)
    t=np.linspace(0,2*pi)
    rr, tt = np.meshgrid(r,t)
    # z=F(rr,tt)
    z=Psi(rr,tt)
    x=r*cos(t)
    y=r*sin(t)
    plt.contourf(x,y,z)
    plt.savefig('plt.png')
    
if __name__ == "__main__":
    main()