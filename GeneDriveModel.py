import numpy as np 

#Simplified Population Prediction with no Gene Drive
arr = ([0.45, 100, 0], [0.135, 0.25, 0], [0.135, 0, 0])
x = [0, 300, 300]
m = 0

while m < 30:
    x = (np.dot(arr, x))
    m = m+1
    x = [int(item) for item in x]
print (x)


#Population Prediction with Gene Drive
m2 = 0
x2 = [0, 0, 0, 300, 0, 0, 150, 150, 0]

while m2 < 46:
    #breed1 calculates liklihood of the child's genotype based on the population
    breed1 = ((int(x2[6])) / int((x2[6] + x2[7] + x2[8])) *100)
    breed1 = int(breed1)
    breed2 = (100 - breed1)
    arr2 = ([0.45, 0, 0, breed1, 0, 0, 0, 0, 0], 
        [0, 0.45, 0, breed2, breed1, 0, 0, 0, 0], 
        [0, 0, 0.45, 0, breed2, 0, 0, 0, 0], 
        [0.135, 0, 0, 0.25, 0, 0, 0, 0, 0],  
        [0, 0.135, 0, 0, 0.25, 0, 0, 0, 0], 
        [0, 0, 0.135, 0, 0, 0.25, 0, 0, 0], 
        [0.135, 0, 0, 0, 0, 0, 0.01, 0, 0,], 
        [0, 0.135, 0, 0, 0, 0, 0, 0.01, 0,],
        [0, 0, 0.135, 0, 0, 0, 0, 0, 0.01,])
    x2 = (np.dot(arr2, x2))
    #turns everything into integers-can't have half a mosquito!
    x2 = [int(item) for item in x2]
    print (x2)
    m2 = m2+1

