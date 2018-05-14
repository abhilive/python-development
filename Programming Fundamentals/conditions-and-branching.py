'''
Conditions and Branching

Conditional Operators

a. equal: ==
b. not equal: !=
c.  greater than: >
d.  less than: <
e.  greater than or equal to: >=
f.  less than or equal to: <=

'''

print('B'>'A') #The ASCII value for A is 101, and the value for B is 102 therefore: True
print('BA'>'AB') #When there are multiple letters, the first letter takes precedence in ordering: True

#Banching

#age=19
age=18

#expression that can be true or false
if age>18:
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
elif age==18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

'''
Logical operators

a. and
b. or
c. not 
'''

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1981 and 1989")
    
print("")
print("Do Stuff..")

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

#Not Statement
album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")
