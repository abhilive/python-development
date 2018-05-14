'''
Loops

Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by loops.

'''

##For loop
dates = [1982,1980,1973]
N=len(dates)

for i in range(N):
     
    print(dates[i])

#Change the element in list
squares=['red','yellow','green','purple','blue ']

for i in range(0,5):
    print("Before square ",i, 'is',  squares[i])
    
    squares[i]='white'
    
    print("After square ",i, 'is',  squares[i])


#Method2 using enumerate
squares=['red','yellow','green','purple','blue ']

for i,square in enumerate(squares):
    print(i,square)

##While Loop
dates = [1982,1980,1973,2000]

i=0;
year=0
while(year!=1973):
    year=dates[i]
    i=i+1
    print(year)
    
    
print("it took ", i ,"repetitions to get out of loop")

#Write a while loop to copy the strings 'orange' of the list 'squares' to the list 'new_squares'. Stop and exit the loop if the value on the list is not 'orange':

squares=['orange','orange','purple','blue ','orange']
new_squares=[];
i=0
while(squares[i]=='orange'):
    new_squares.append(squares[i])
    i += 1
    
print(new_squares)
