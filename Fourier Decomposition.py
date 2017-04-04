# a step function equals the sum of many sin function
import numpy as np
import matplotlib.pyplot as plt

def fou(t):
    y=0
    for i in range(1,25000,2):
        y=y+(1/i)*np.sin(i*t)
    return y
x=np.linspace(0,2*np.pi,10000)
add=fou(x)
#y=np.sin(x)+1/3*np.sin(3*x)+1/5*np.sin(5*x)+1/7*np.sin(7*x)+1/9*np.sin(9*x)
plt.plot(x,add)
plt.xlim(0,6.5)
plt.show()
