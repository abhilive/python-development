'''
Functions

A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.

There are two types of functions :

    1. Pre-defined functions
    2. User defined functions

PS:
1. The input to a function is called a formal parameter.
2. A variable that is declared inside a function is called a local variable.
3. A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program.

http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf
'''

def add(a):
    """
    add 1 to a
    """
    b=a+1; 
    print(a, "if you add one" ,b)
    
    return(b)

def square(a):
    """Square the input and add one  
    """
    #Local variable 
    b=1
    c=a*a+b;
    print(a, "if you square +1 ",c) 
    return(c)

def type_of_album(artist,album,year_released):
    if year_released > 1980:
        print(artist,album,year_released)
        return "Modern"
    else:
        print(artist,album,year_released)
        return "Oldie"

def PrintList(the_list):
    for element in the_list:
        print(element)

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
    else:
        print("this album is good its rating is",rating)
        
        
if __name__ == '__main__':
    add(10)
    square(10)
    x = type_of_album("Michael Jackson","Thriller",1980)
    print(x)
    PrintList(['1',1,'the man',"abc"])
    isGoodRating()
    isGoodRating(10)

#Pre-defined functions
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5] 
print(album_ratings) #BIF
sum(album_ratings) #BIF
len(album_ratings) #BIF



