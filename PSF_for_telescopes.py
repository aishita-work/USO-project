import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from my_funct import *
import sys
import glob
import numpy as np
import math
import array

# Dimensions of the images
nx=256
ny=256

# Create a figure with 3 rows and 4 columns of subplots
fig,axs= plt.subplots(3,4,figsize=[38,28])

# Loop through each of the 4 columns
for i in range (0,4):
    
    # Calculate the radius of the point spread function (PSF)
    rad=8*2**i
    
    # Generate the point spread function and aperture using the function point_spread
    psf_tele,apt=point_spread(nx,ny,rad)
    
    # Plot the aperture in the first row of the current column
    axs[0,i].imshow(apt,cmap='gray',vmax=0.1)
    
    # Plot the negative of the PSF in the second row of the current column
    axs[1,i].imshow(-psf_tele,cmap='gray',vmax=0.1)
    
    # Set the title for the current column based on the radius of the PSF
    axs[0,i].set_title( 'D=%d' % (2*rad), fontsize = 28)
    
    # Plot a graph of the PSF along a central row in the third row of the current column
    axs[2,i].plot(psf_tele[int(nx/2)][0:ny-1])
    
    # Turn off the axes for the plots in all rows of the current column
    axs[0,i].set_axis_off()
    axs[1,i].set_axis_off()
    axs[2,i].set_axis_off()
    
plt.savefig("three_row_display", dpi=200) 
plt.show()    



