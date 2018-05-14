"""
Lists and Tuples

 These are called compound data types.
 Tuple: In Python, there are different data types: string, integer and float. These data types can all be contained in a tuple.
 List: A list is a sequenced collection of different objects such as integers, strings, and other lists as well. The address of each element within a list is called an 'index'. An index is used to access and refer to items within a list.

"""

#Tuple
tuple1=("disco",10,1.2)
print(type(tuple1)) #Type of variable is a tuple

#Print each value in the tuple
print( tuple1[0])
print( tuple1[1])
print( tuple1[2])

#Print type of each value in the tuple
print( type(tuple1[0]))
print( type(tuple1[1]))
print( type(tuple1[2]))

#Obtain last element using negative index
print( tuple1[-1])

#Concatenate or combine tuples
tuple2=tuple1+("hard rock", 10)
print( tuple2)

print(tuple2[0:3]) #Slice tuple #first three element
print(len(tuple2)) #Get length

Ratings =(0,9,6,5,10,8,9,6,2)

Ratings1 =Ratings #Assign to another variable
RatingsSorted=sorted(Ratings) #To sort tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2))) #Nested tuple each element can be accessed via its index
print(NestedT[2][0]) #Print 'pop'

print(NestedT.index(2)) #Get the index

#List: Nested list
list1 = [ "Michael Jackson", 10.1,1982,[1,2],("A",1) ] #We can access elements using index like above
print(list1.extend(['pop',10])) #Extend method to add new elements to list
print(list1.append(['pop',10])) #Append only one element to the list

#List are mutable we can change them
list1[1] = 11.2;
print(list1)
del(list1[1]) #To delete any element

print('hard rock'.split()) #Convert string to list

'A,B,C,D'.split(',') #Seprate with specific charcter

# When we set one variable B equal to A; both A and B are referencing the same list in memory
A=["hard rock",10,1.2]
B=A
print('A:',A)
print('B:',B)

#As A and B are referencing the same list, if we change list A, then list B also changes. If we check the first element of B we get banana instead of hard rock:
print('B[0]:',B[0])
A[0]="banana"
print('B[0]:',B[0])

#Clone list
B=A[:]
#Now if you change A, B will not change:
print('B[0]:',B[0])
A[0]="banana"
print('B[0]:',B[0])
