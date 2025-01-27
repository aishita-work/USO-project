import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def azimuth(rad):
    rows_count=int(rad*2)  # Calculate the number of rows in the image
    cols_count=int(rad*2)  # Calculate the number of columns in the image
    x0=(cols_count/2)      # X-coordinate of the image center
    y0=(rows_count/2)       # Y-coordinate of the image center
     
        
    # Create a 2D list (list of lists) initialized with zeros to represent the image
    img=[[0 for j in range(cols_count)] for i in range(rows_count)]
    
    # Iterate over each pixel in the image
    for i in range (0,rows_count):
     for j in range (0,cols_count):
            
       dis=np.sqrt((j-x0)**2 +(i-y0)**2) # Calculate the distance from the center

       if i!=y0:      
            # Calculate the azimuth angle and assign it to the pixel
            img[i][j]=(np.pi/2) + (math.atan((j-x0)/(i-y0)))

            
            if i-rows_count/2>0:
                
                img[i][j]=img[i][j]+np.pi # Adjust the angle for the second half of the image
                
       elif j-cols_count/2<0:
                #img[i][j]=180
                img[i][j]=np.pi # Set the azimuth angle to pi for the center column
            
            
#     img[i][j]=img[i][j]*(np.pi/180.0)
    img=np.array(img) # Convert the 2D list to a NumPy array
    return img    # Return the azimuth pattern as a NumPy array
