'''
2D Array in numpy
'''
import numpy as np 
import matplotlib.pyplot as plt

#Consider a list, list contain nested list each of equal size
a=[[1,2,3],[4,5,6],[7,8,9]]

#Cast this list to a numpy array

A=np.array(a)

A.ndim #Obtain number of axes or dimensions referred to as the rank

A.shape #Returns a tuple corresponding to the size or number of each dimension.

A.size #Total number of element in array

#Accessing elements

print(A[1][2])
print(A[1,2]) #Similar to above one


#Slicing

print(A[0][0:2])
print(A[0,0:2]) #Similar to above one

#Basic Operation
X=np.array([[1,0],[0,1]]) 
Y=np.array([[2,1],[1,2]])

Z=X+Y #Addition of two array

#Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler.
Z=2*Y

#Multiplication of two arrays corresponds to an element-wise product or Hadamard product. Consider matrix X and Y. The Hadamard product corresponds to multiplying each of the elements in the same position
Z=X*Y

#Matrix multiplication
Z=np.dot(X,Y)

np.sin(Z)

C=np.array([[1,1],[2,2],[3,3]])

C.T #Transpose the matrix