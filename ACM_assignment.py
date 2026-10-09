import numpy as np
import matplotlib.pyplot as plt


### Explicit Numerical Methods ###
def EulerEx(y0, h, n, f):
    n = int(n/h)
    
    y = [y0]
    x = [0]

    for i in range(n):

        y.append(y[i]+h*(f(x[i],y[i])))
        x.append(x[i]+h)
        
    return x, y

def HeunEx(y0, h, n, f):
    n = int(n/h)
    
    y = [y0]
    x = [0]
    
    for i in range(n):
        
        k1 = f(x[i],y[i])
        y_star = y[i]+h*k1
        k2 = f(x[i]+h, y_star)
        
        y.append(y[i]+(h/2)*(k1+k2))
        x.append(x[i]+h)
        
    return x, y

def RK4Ex(y0, h, n, f):
    n = int(n/h)
        
    y = [y0]
    x = [0]
    
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i]+(h/2), y[i]+(h/2)*k1)
        k3 = f(x[i]+(h/2), y[i]+(h/2)*k2)
        k4 = f(x[i]+h, y[i]+h*k3)
        
        y.append(y[i]+(h/6)*(k1+2*k2+2*k3+k4))
        x.append(x[i]+h)
        
    return x, y


### Analysis of differential equations ###
def PhasePortrait(f, *crit_points):
    portrait = []
    
    if f(crit_points[0]-0.1, 0) < 0:
        portrait.append("<")
    else:
        portrait.append(">")
        
    for i in crit_points:
        if f(crit_points[i]+0.1, 0) < 0:
            portrait.append("<")
            portrait.append(crit_points[i])
        else:
            portrait.append(">")
            portrait.append(crit_points[i])
            
    return portrait

def SlopeField(y0, n, h, f,):
    X = np.linspace(y0, n, h)
    Y = np.linspace(y0, n, h)
    X, Y = np.meshgrid(X,Y)
    
    
    Dx, Dy = [1, f(X,Y)]
    
    
    N = np.sqrt(Dx**2 + Dy**2)    
    N[N==0] = 1
    Dx = Dx/N
    Dy = Dy/N

    
    return X, Y, Dx, Dy

def Function(x,y):
    return y - (np.sqrt(x**2))

X, Y, Dx, Dy = SlopeField(-10, 10, 20, Function)

#plt.quiver(X, Y, Dx, Dy, pivot="middle")

x, y = RK4Ex(0, 1, 10, Function)

### Plotting results ###
plt.plot(x,y)
plt.show()