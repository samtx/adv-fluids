# Shock tube

import numpy as np
import Coolprop.Coolprop as CP

R = 287.1   # gas constant for air [J/(mol*K)]


def get_cp(p, rho):
    return CP.PropsSI('CP0MOLAR', 'P', p, 'D', d, 'Air')  # get specific heat of enthalpy in J/(mol*K)

def get_kappa(p, rho):
    cp = get_cp(p, rho)
    return cp/(cp - R)
    
def get_rho(p, T):
    '''p[i-1,i+1]
       T[i-1,i+1]'''
    return (p[1]+p[0])/(R * (T[1]-T[0]))

def main():
    
    # constants
    dx = 1e-2   # delta x
    L = 1.0     # length, [m]
    dt = 1e-4   # delta t [s]
    T = 1       # total time [s]
    S = 0.5     # width, [m]
    cf = 1      # coefficient of friction
    Dh = 1      # hydraulic diameter
    
    # unknowns
    rho = np.zeros((L/dx, T/dt))   # density
    m = np.zeros((L/dx, T/dt))     # mass flow rate
    p = np.zeros((L/dx, T/dt))     # pressure
    v = np.zeros((L/dx, T/dt))     # velocity
    k = np.zeros((L/dx, T/dt))     # kappa (cp/(cp-R))
    q = np.zeros((L/dx, T/dt))     # heat [kJ/kg] 
    
    # mass transient
    dmdt[i, t] = -1/dx * (m[i+1,t]*v[i+1,t] - m[i-1,t]*v[i-1,t] + (p[i+1,t] - p[i-1,t])*S) - cf * m[i,t]**2 / (2*Dh*rho[i,t]*S)
    
    # pressure transient
    dpdt[i, t] = -k[i,t]/dx * (m[i+1,t]*p[i+1,t]/(rho[i+1,t]*S) - m[i-1,t]*p[i-1,t]/(rho[i-1,t]*S)) - \
        (k[i,t]-1) * (m[i,t]*q[i,t]/dV + cf*m[i+1,t]*m[i,t]**2/(2*Dh*S*rho[i,t]**2 * S**2)) - \
        (k[i,t]-2) * m[i,t]/(rho[i,t]*(S**2))*(m[i,t]/(2*rho[i,t]*dx)*(m[i+1,t]/S - m[i-1,t]/S) + dmdt[i+1,t]) - \ 
        (k[i,t]-2) / (2*dx) * (m[i+1,t]**3/(rho[i+1,t]**2 * S**3) - m[i-1,t]**3/(rho[i-1,t]**2 * S**3))
              
    


if __name__ == "__main__":
    main()