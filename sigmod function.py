import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,10000)
a1=1
a2=2
a3=5
y1=1/(1+np.exp(-1*x*a1))
y2=1/(1+np.exp(-1*x*a2))
y3=1/(1+np.exp(-1*x*a3))
plt.plot(x,y1,'r',label="a=1")
plt.plot(x,y2,'b',label='a=2')
plt.plot(x,y3,'g',label="a=5",)
plt.title("sigmod function")
plt.ylim(0,1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.show()