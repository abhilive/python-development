"""
Strings

String: String as an ordered sequence. Each element in the sequence can be accessed using an index represented by the array of numbers.
"""

Name= "Michael Jackson"

#Indexing
print(Name[0]) #first character
print(Name[13]) #Character at the 14th position, because indexing starts from 0
print(Name[-1]) #first character from last

#Length
print(len(Name))

#Slicing
print(Name[0:4]) #Chars from 0 to 4
print(Name[8:12]) #Chars from 8 to 12

#Input stride value
print(Name[::2]) #Selecting every second charcter starting from index 0

#Slicing with stride
print(Name[0:5:2]) #Select first five elements then use stride

#Concatenate or combine strings
print(Name + ' is the best')

#Replicate string
print(3*Name)

#Escape Sequence
print(" Michael Jackson \n is the best" ) # n for newline
print(" Michael Jackson \t is the best" ) # t for tab
print(" Michael Jackson \\ is the best" ) # To dispaly a backslash in string
print(r" Michael Jackson \ is the best" ) # Other way to dispaly a backslash

#Operations
print(Name.upper()) #To covert lowercase to uppercase
print(Name.lower()) #To covert uppercase to lowercase
print(Name.replace('Michael', 'Janet')) # To replace certain part of string
print(Name.find('Jack')) #To find a sub-string, retrun first index of sequence and -1 in case of sub-string is not found 
