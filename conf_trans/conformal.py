# Conformal Transformation
# Ch. 6 Assignment
# Sam Friedman
# 4/21/2017

import numpy as np
# import matplotlib
# matplotlib.use('cairo')
import matplotlib.pyplot as plt

from numpy import cos, sin, pi, log, exp, sqrt, nan

def main():

    u_inf = U_inf=1     # flow velocity
    R=0.2         # cylinder radius
    alpha = 0.5
    # gamma = 1
    kappa = k = gamma = 4
    # Stream functions
    xd, yd = 0.0, 0.0
    xv, yv = 0.0, 0.0
    N = 100                                # Number of points in each direction
    x_start, x_end = -2.0, 2.0            # x-direction boundaries
    y_start, y_end = -1.0, 1.0            # y-direction boundaries
    x = np.linspace(x_start, x_end, N)    # computes a 1D-array for x
    y = np.linspace(y_start, y_end, N)    # computes a 1D-array for y
    X, Y = np.meshgrid(x, y)              # generates a mesh grid
    # calculate the cylinder radius
    R = sqrt(kappa/(2*pi*u_inf))
    # remove X,Y coordinates outside of cylinder
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            if sqrt(X[i,j]**2+Y[i,j]**2) < R:
                X[i,j], Y[i,j] = nan, nan
    # X = X[~np.isnan, ~np.isnan]
    # Y = Y[~np.isnan, ~np.isnan]
    psi_doublet = -k/(2*pi)*(Y-yd)/((X-xd)**2+(Y-yd)**2)
    psi_freestream = u_inf * Y
    psi_vortex = k/(4*pi)*log((X-xv)**2+(Y-yv)**2)
    psi = psi_doublet + psi_freestream + psi_vortex
    # calculate the stagnation points
    x_stagn1, y_stagn1 = +sqrt(R**2-(gamma/(4*pi*u_inf))**2), -gamma/(4*pi*u_inf)
    x_stagn2, y_stagn2 = -sqrt(R**2-(gamma/(4*pi*u_inf))**2), -gamma/(4*pi*u_inf)
    print(psi.shape)
    print(psi)
    # plot the streamlines
    size = 10
    plt.figure(figsize=(size, (y_end-y_start)/(x_end-x_start)*size))
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.contour(X,Y,psi,50)
    circle = plt.Circle((0, 0), radius=R, color='#CD2305', alpha=0.5)
    plt.gca().add_patch(circle)
    plt.scatter(xv, yv, color='#CD2305', s=80, marker='o')
    plt.scatter([x_stagn1, x_stagn2], [y_stagn1, y_stagn2], color='g', s=80, marker='o');
    plt.show()
    return
    def Phi(r, theta):
        return U_inf*(r+R**2/r)*cos(theta)

    def Psi(r, theta):
        return U_inf*(r-R**2/r)*sin(theta)

    # Potential Function
    def F(z):
        return U_inf*(z*exp(-1j*alpha)+R**2/z*exp(1j*alpha)) - 1j*gamma/(2*pi)*log(z*exp(-1j*alpha)/R)

    def F2(r, theta):
        return Phi(r, theta) + 1j*Psi(r, theta)

    def Cp(theta):
        return 1-4*sin(theta)**2

    r=np.linspace(R,R*5)
    t=np.linspace(0,2*pi)
    rr, tt = np.meshgrid(r,t)
    # z=F(rr,tt)
    axes = [-1, 1, -1, 1]
    x = np.linspace(axes[0],axes[1])
    y = np.linspace(axes[2],axes[3])
    xx, yy = np.meshgrid(x, y)
    f = np.zeros((len(x),len(y)))
    z = xx + 1j*yy
    f =  U_inf*(z[:,:]*exp(-1j*alpha)+R**2/z[:,:]*exp(1j*alpha)) - 1j*gamma/(2*pi)*log(z[:,:]*exp(-1j*alpha)/R)
    # print(zz)
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         f(i,j) = F(zz[i][j])
    # f = F(zz
    z=Psi(rr,tt)
    x=r*cos(t)
    y=r*sin(t)
    print('f.shape=',f.shape)
    print(f)
    plt.contourf(xx,yy,f)
    plt.show()
    # plt.savefig('plt.png')

# Potential Function
def F(z, alpha=0.5, gamma=1, U_inf=1, R=0.5):
    return U_inf*(z*exp(-1j*alpha)+R**2/z*exp(1j*alpha)) - 1j*gamma/(2*pi)*log(z*exp(-1j*alpha)/R)


if __name__ == "__main__":
    main()
