"""
Problem Statement:
Given an integer,n, perform the following conditional actions:

    If n is odd, print Weird
    If n is even and in the inclusive range of 2 to 5, print Not Weird
    If n is even and in the inclusive range of 6 to 20, print Weird
    If n is even and greater than 20, print Not Weird

Source: https://www.hackerrank.com/challenges/py-if-else/problem
"""

if __name__ == '__main__':
    n = int(input())
    if n in range(6,21) or n%2!=0 :
        print("Weird")
    else:
        print("Not Weird")
