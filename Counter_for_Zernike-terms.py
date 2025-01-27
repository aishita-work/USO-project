def zern_term(n):
    nterms=0  # Initialize the counter for the number of terms
    
    # Iterate over the orders of the Zernike polynomial
    for i in range(1,n+1):
        
         # Iterate over the azimuthal terms within the current order
        for j in range(-i,i+1):
            
            # Check if the difference between order i and azimuthal term j is even
            if (i-j)%2==0:
                nterms=nterms+1  # Increment the term counter
                
    return(nterms)