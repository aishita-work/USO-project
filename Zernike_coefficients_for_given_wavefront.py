import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from my_funct import   *   # Importing functions from 'my funct' module


file=fits.open('Wavefront.fits')  # Opening a FITS file
data=file[0].data  # Extracting data from the FITS file
plt.imshow(data, cmap = 'coolwarm' )
plt.colorbar()
plt.show()

rd=32 # Defining a variable 'rd'
ap=aper(rd)  # Calling a function 'aper' with 'rd' as argument n=5 # Defining a variable 'n'
n=5

id= np.where(ap==1) # Finding indices where 'ap' equals 1 
B=data[id] #Extracting data at the indices 'id' from 'data'

zern=zernike_gen(n, rd) # Generating Zernike terms up to order 'n'

xx=len(B) # Getting the length of 'B'
yy=zern_term(n)-2 # Calculating the number of Zernike terms up to order 'n' minus 2

A=[[0. for i in range (yy)] for i in range(xx)] # Initializing a matrix 'A' with zeros 
A=np.array(A) # Converting 'A' to a numpy array

#Filling the matrix 'A' with Zernike terms corresponding to 'id'
for i in range (0,yy):
    zz=zern[i+2,0:2*rd, 8:2*rd] # Extracting Zernike term
    A[0:xx,i]=zz[id] # Filling the matrix 'A' with Zernike term values

Ainv = np.linalg.pinv(A) # Calculating the pseudo-inverse of matrix 'A'
result = np.dot (Ainv,B) # Multiplying pseudo-inverse 'Ainv' with 'B' to get coefficien 
print(result)
print("-----------------------------------------------------------------------------------------------")

#Given Zernike coefficients
cff=[0.875227,0.778227,0.728550,0.701542,0.580200,0.454615,0.414680,0.382099,0.396558,
     0.362266,0.358363,0.312173,0.235039,0.250885,0.258540,0.226653,0.0976633,0.18705]

print(cff)

#Initializing a matrix 'ph' for phase calculation
ph=[[0. for i in range (2*rd)] for i in range (2*rd)]
ph=np.array(ph)

#... (previous code remains the same)

#Calculating phase using Zernike coefficients and adding to 'ph'
for i in range(0, yy):
    ph = zern[1+2, 0:2*rd, 0:2*rd]* result[i] + ph

#Calculate the difference between the input phase and the calculated phase 
diff= ph-data

# Displaying the original data plot
plt.figure(figsize=(12, 4)) # Creating a new figure with a specific size 
plt.subplot(1, 3, 1) # Creating the first subplot

plt.imshow(data, cmap='coolwarm') 
plt.colorbar()
plt.title("Original Data")

# Displaying the calculated phase plot 
plt.subplot(1, 3, 2) # Creating the second subplot 
plt.imshow(ph, cmap='coolwarm') 
plt.colorbar()
plt.title("Calculated Phase")

# Displaying the difference plot
plt.subplot(1, 3, 3) # Creating the third subplot 
plt.imshow(diff, cmap='coolwarm') 
plt.colorbar()
plt.title("Difference")

# Adjust Layout to prevent overlapping titles and Labels 
plt.tight_layout()

# Save the combined figure as a single image 
plt.savefig("combined_plots.png")

# Show the combined figure 
plt.show()