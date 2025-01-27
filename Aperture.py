import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def aper(rad):
	xx = 2*rad	# Calculate the width of the aperture
	yy = 2*rad	# Calculate the height of the aperture
    
    # Create a 2D list initialized with zeros to represent the aperture
	apt=[[0 for i in range (xx)] for j in range(yy)] 
   
    # Iterate over each pixel in the aperture
	for i in range(xx):
		for j in range(yy):
            
            # Calculate the distance of the current pixel from the center of the aperture
			dis=np.sqrt((i-xx/2)**2 + (j-yy/2)**2)
            
            # Check if the distance is within the specified radius
			if dis<=rad:
				apt[i][j]=1   # Set the pixel value to 1 (inside the aperture)
    
	apt=np.array(apt)	# Convert the 2D list to a NumPy array
	return apt	 #Return the aperture pattern as a NumPy array
