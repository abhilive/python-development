'''
1-D Numpy Array
'''
#Recall python list

lst = [1,'Apple', 2, "Muskmilon", "Banana"]

print("lst[0]:", lst[0]); #1

print("lst[3]:", lst[3]); #Muskmilon

# A Numpy array is similar to a list, it's usually fixed in size and each element of the same type.

import numpy as np
import matplotlib.pyplot as plt

a=np.array([1,2,3,4,5,6])

print("First element: ", a[0])
print("Second element: ", a[1])

print(type(a)) #to check the type of array will return numpy.ndarray

print(a.dtype) #to get the datatype of array element return dtype('int32')

# numpy array with real numbers
b=np.array([3.14, 2.2, 1, 3.0, 5.7])

print(type(b))
print(b.dtype)

#Change the value of the array
b[1]=10.2
b[4]=9.2

#like list we can slice value of array
c= b[1:4] #select the element from 1 to 3 and assign it to new array

# assign the correspondings index to new values
b[1:3] = 100, 200

#We can use a list to select specific index
select = [1,2]
d=b[select]

#Assign the specified elements to new values
c[select]=10000

#Basic array attributes and methods
a=np.array([0,1,2,3,4])

a.size #Number of elements in the array
a.ndim #Number of array dimension or rank of the array
a.shape #Tuple of integers indicating the size of the array 

a.mean() #Find mean
a.std() #Find standard deviation
a.max() #Maximum in arrray
a.min() #Minimum in array

#Array addition
u=np.array([1,2,3])
v=np.array([4,5,6])

z=u+v #Equivalent to vector addition

z=u-v #Equivalent to vector substraction

z=2*u #Multiply the each element of 'u' with 2

z=u+2 #Adding constant to each element

z=u*v #Product of two numpy arrays

np.dot(u,v) #Find the dot product

#Mathematical Function

np.pi #Access the value of pi in numpy

x=np.array([0, np.pi/2, np.pi]) #Numpy array in radians

y=sin(x) #This applies the sine function to each element in the array

'''
Linspace
A useful function for plotting mathematical functions is "linespace". Linespace returns evenly spaced numbers over a specified interval. We specify the starting point of the sequence and the ending point of the sequence. The parameter "num" indicates the Number of samples to generate, in this case 5
'''

np.linspace(-2,2,num=5)

np.linspace(-2,2,num=9) # 9 evenly spaced number over the interval -2 to +2

# We can use the function line space to generate 100 evenly spaced samples from the interval 0 to 2 pi:

x=np.linspace(0,2*np.pi,num=100)
y=np.sin(x)

plt.plot(x,y)