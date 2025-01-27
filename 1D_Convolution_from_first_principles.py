
from matplotlib import pyplot as plt
from my_funct import *
import sys
import glob
import numpy as np
import math
import array

# Parameters for the first signal
x1=200
wd=50
f1=[0 for i in range (x1)] 
f1=np.array(f1)
f1[int(x1/2)]=1

# Initialize convolution array
cnv=[0 for i in range (x1)] 
cnv=np.array(cnv)

# Parameters for the second signal
x2=101
wd=30
f2=[0 for i in range (x2)] 
f2=np.array(f2)
f2[int(x2/2-wd/2):int(x2/2+wd/2)]=1

# Convolution calculation loop
for i in range (0,x1-x2+1):
    g1=f1[i:i+x2]
    g2=np.multiply(g1,f2)
    cnv[int(i+x2/2)]=sum(g2)

# Create axes for plotting
ax1=np.arange(0,x1,1)-x1/2
ax2=np.arange(0,x2,1)-x2/2

# Perform convolution using numpy's convolve function
cnv2=np.convolve(f1,f2,mode='same')

# Plotting the signals and convolution result
plt.plot(ax1,f1,'g')
plt.plot(ax2,f2,'r')
plt.plot(ax1,cnv,'ob')
 
# Save and display the plot
plt.savefig("convolution_1D", dpi=200) 
plt.show()     