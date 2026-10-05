import numpy as np
from scipy import integrate

# Parameters
gca = 4.4 #uS
gk = 8
gl = 2

vca = 130 #mV
vk = -84
vl = -60

v1 = -1.2 #mV
v2 = 18
v3 = 2
v4 = 30

tau0 = 0.04
current = 0
c = 20 # uF
w = 0

#Equations:

def dV(V):
    return (-gca*Mss(V)*(V-vca)-gk*w*(V-vk)-gl*(V-vl)+current)/c

def dW(V):
    return (Wss(V)-w)/Tw(V)

def Mss(V):
    return (1+np.tanh((V-v1)/v2))/2

def Wss(V):
    return (1+np.tanh((V)))

def Tw(V):
    return tau0*(1/np.cosh((V-v3)/2*v4))


