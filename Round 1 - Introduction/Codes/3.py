import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #the package "pandas" provides methods for loading and saving data to file 


# read in the data from "DataTask3.csv"
#df = ...
# YOUR CODE HERE
raise NotImplementedError()
X = df.as_matrix() # convert the data frame to numpy matrix



### STUDENT TASK ###
#Step 1: draw the scatter plot for data X
plt.figure(figsize=(8,8))
# YOUR CODE HERE
raise NotImplementedError()


### STUDENT TASK ###
#Step 2: compute the sample covariance of data X
#C = ...
# YOUR CODE HERE
raise NotImplementedError()
#Hint: C should be a 2x2 matrix. 

### STUDENT TASK ###
#Step 3: find eigenvalues and eigenvectors of C and print them
#values, vectors = ...
#print('eigenvalues= ', values)
#print('eigenvectors= ', vectors)
# YOUR CODE HERE
raise NotImplementedError()
print('eigenvalues= ', values)
print('eigenvectors= ', vectors)

### STUDENT TASK ###
#Step 4: plot each eigenvector as a line from [0,0] to the coordinate of the eigenvector
# YOUR CODE HERE
raise NotImplementedError()

plt.xlim((-4, 4))
plt.ylim((-4, 4))

plt.legend()
plt.show()