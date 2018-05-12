"""
Problem Statement:

Write a function to find factorial of any given number
"""

def factorial(num):
    leap = False
    
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    
if __name__ == '__main__':
    num = int(input())
    print(factorial(num))
