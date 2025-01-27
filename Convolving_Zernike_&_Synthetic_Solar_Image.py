import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from my_funct import *
from scipy import signal

# Open a FITS file and extract data
file = fits.open('Synthetic-Solar-Image.fits')
data = file[0].data
obj = data[128:384, 128:384]  # Extract a subset of the data

n = 5  # Zernike polynomial order
rd = 32  # Radius
zern = zernike_gen(n, rd)   # Generate Zernike polynomials
A = aper(rd)  # Generate an aperture function
 
z = complex(0, 1)  # Imaginary unit

cf = 10.0   # Coefficient for phase calculation

zernike_term_names = [
    "Tip", "Tilt", "Oblique Astig","Defocus",  
    "Vertical Astig", "Vertical Coma", "Horizontal Coma", "Spherical"]

# Loop through Zernike terms
for i in range(0, 9):
    # Set coefficient based on index for different Zernike terms
    if i < 2:
        cf = 50.0
    else:
        cf = 10.0
    zen = zern[i, 0:2*rd, 0:2*rd]  # Get specific Zernike term
    ph = cf * zen    # Calculate phase
    wf = A * np.exp(z * ph)     # Generate wavefront
    f_wf = np.fft.fft2(wf)     # Compute 2D FFT of the wavefront
    f_wf = np.fft.fftshift(f_wf)  # Shift the FFT
    psf = abs(np.conj(f_wf) * f_wf)  # Calculate point spread function

    # Convolve object with PSF to generate the convolved image
    img = signal.convolve2d(obj, psf, mode='same', boundary='wrap')
    
    # Create a figure with subplots
    fig, axs = plt.subplots(1, 3, figsize=[20, 6])
    
    # Display the cut-out region of the original image
    axs[0].imshow(obj, cmap='gray')
    axs[0].set_title('Cut-out Region', fontsize=14)
    
    # Display the current Zernike term
    axs[1].imshow(zen, cmap='gray')
    axs[1].set_title(f'Zernike Term: {zernike_term_names[i]}', fontsize=14)
    
    # Display the convolved image
    axs[2].imshow(img, cmap='gray')
    axs[2].set_title('Convolved Image', fontsize=14)