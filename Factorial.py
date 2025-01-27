def factorial(n):
  
    if n==0:
        fac=1 # Factorial of 0 is 1
    else:
        fac=1  #Initialize the factorial value to 1
        for i in range (1,n+1):
            fac=i*fac  # Multiply the current number with the running factorial value
    return fac  # Return the calculated factorial