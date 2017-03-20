'''matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot
function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines
 in a plotting area, decorates the plot with labels, etc. In matplotlib.pyplot various states are preserved across
 function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions
 are directed to the current axes (please note that “axes” here and in most places in the documentation refers to the
 axes part of a figure and not the strict mathematical term for more than one axis).'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
#plt.show()

'''You may be wondering why the
x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to the plot()
 command, matplotlib assumes it is a sequence of y values, and automatically generates the x values for you.
 Since python ranges start with 0, the default x vector has the same length as y but starts with 0. Hence the x
  data are [0,1,2,3].'''


