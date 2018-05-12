"""
Problem Statement:

You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N.
Here,

0<=i<=X; 0<=j<=Y; 0<=k<=Z

Source: https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

if __name__ == '__main__':

    #More precise way to get input
    x,y,z,n = [int(input()) for i in range(4)]
    
    #x, y, z, n = int(input()), int(input()), int(input()), int(input())
    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])

    #Another Way if we don't use list comprehensions
    '''
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    result.append([i,j,k])
                    
    print(result)
    '''
