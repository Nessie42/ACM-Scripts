import numpy as np
from scipy import integrate

### Parameters ###
#Channel conductances
gca = 4.4 #uS
gk = 8 #uS
gl = 2 #uS

#Channel voltages
vca = 130 #mV
vk = -84 #mV
vl = -60 #mV

# Steady State Voltages
v1 = -1.2 #mV
v2 = 18 #mV
v3 = 2 #mV
v4 = 30 #mV

#Misc remaining parameters
tau0 = 0.04
current = 0
c = 20 # uF
w = 0

### Equations: ###

def dV(V): #Differential equation for V
    return (-gca*Mss(V)*(V-vca)-gk*w*(V-vk)-gl*(V-vl)+current)/c

def dW(V): #Differential equation for W
    return (Wss(V)-w)/Tw(V)

def Mss(V): #Function governing M_ss(V)
    return (1+np.tanh((V-v1)/v2))/2

def Wss(V): #Function governing W_ss(V)
    return (1+np.tanh((V)))

def Tw(V): #Function governing T_0(V)
    return tau0*(1/np.cosh((V-v3)/2*v4))


