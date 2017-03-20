"""For every x, y pair of arguments, there is an optional third argument which is the format string that indicates
the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate
a color string with a line style string. The default format string is ‘b-‘, which is a solid blue line. For example,
to plot the above with red circles, you would issue"""
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()



