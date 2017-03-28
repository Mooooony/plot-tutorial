import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,10000)
a1=1
a2=2
a3=5
y1=1/(1+np.exp(-1*x*a1))
y2=1/(1+np.exp(-1*x*a2))
y3=1/(1+np.exp(-1*x*a3))

fig=plt.figure()
ax=fig.add_subplot(111)

ax.plot(x,y1,'r',label="a=1")
ax.plot(x,y2,'b',label='a=2')
ax.plot(x,y3,'g',label="a=5",)
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.title("sigmod function")
plt.ylim(0,1.2)
plt.xlabel('x')
plt.ylabel('y')


plt.grid()
plt.legend()

plt.show()