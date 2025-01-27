import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def zernike_gen(n,rd):
    app=aper(rd)
    az=azimuth(rd)
    rdd=radial(rd)
    phi=az
    rho=rdd
    nterms=0
    ntr=zern_term(n)
    z_n_m=[[[0. for s in range (2*rd)] for t in range(2*rd)] for r in range (ntr)]
    z_n_m=np.array(z_n_m)
    
    
    for i in range(1,n+1):
    #for i in range(2,n+1):
        for j in range(-i,i+1):
            if (i-j)%2==0:
                             
                upp=(i-abs(j))/2
                
                r_n_m=[[0 for s in range (2*rd)] for t in range(2*rd)] 
                r_n_m=np.array(r_n_m)
                for k in range(0,int(upp+1)):
                    
                    num1=(-1)**k
                    num2=factorial(i-k)
                    den1=factorial(k)
                    d1 = int((i+abs(j))/2-k)
                    d2 = int((i-abs(j))/2-k)
                    den2=factorial(d1)
                    den3=factorial(d2)
                    tm1=float(num1*num2/(den1*den2*den3))
                    poo=float(i-2*k)
                    
                    r_n_m=r_n_m+tm1*(rho**poo)

                # Determine whether the azimuthal term j is positive or negative    
                if j>=0:
                    # If j is positive, compute the Zernike pattern with cosine modulation
                    z_n_m[nterms,0:2*rd,0:2*rd]=(r_n_m*app)*np.cos(j*phi)
                else:
                    # If j is negative, compute the Zernike pattern with sine modulation
                    z_n_m[nterms,0:2*rd,0:2*rd]=(r_n_m*app)*np.sin(j*phi)
                nterms=nterms+1  
                                  
    #print("number of terms for n=",n,"is ",nterms)      
    return z_n_m

