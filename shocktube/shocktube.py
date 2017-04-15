# Shock tube

import numpy as np
import Coolprop.Coolprop as CP


def cp(p, rho):
    return CP.PropsSI('CP0MOLAR', 'P', p, 'D', d, 'Air')  # get specific heat of enthalpy in J/(mol*K)

def main():
    
    # constants
    dx = 1e-2   # delta x
    L = 1.0     # length, [m]
    dt = 1e-4   # delta t [s]
    T = 1       # total time [s]
    S = 0.5     # width, [m]
    cf = 1      # coefficient of friction
    Dh = 1      # hydraulic diameter
    R = 287.1   # gas constant for air [J/(mol*K)]
    
    # unknowns
    rho = np.zeros((L/dx, T/dt))   # density
    m = np.zeros((L/dx, T/dt))     # mass flow rate
    p = np.zeros((L/dx, T/dt))     # pressure
    v = np.zeros((L/dx, T/dt))     # velocity
    k = np.zeros((L/dx, T/dt))     # kappa (cp/(cp-R))
    
    # mass transient
    m[i, t] = -1/dx * (m[i+1,t]*v[i+1,t] - m[i-1,t]*v[i-1,t] + (p[i+1,t] - p[i-1,t])*S) - cf * m[i,t]**2 / (2*Dh*rho[i,t]*S)
    
    # pressure transient
    p[i, t] = -k/dx * ( m[i+1,t]*p[i+1,t]/(rho[i+1,t]*S) - m[i-1,t]*p[i-1,t]/(rho[i-1,t]*S) ) - 


if __name__ == "__main__":
    main()