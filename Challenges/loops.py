"""
Problem Statement:

Read an integer N. For all non-negative integers i<N, print i^2.

Source: https://www.hackerrank.com/challenges/python-loops/problem
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n) :
        print(i*i)
    #Another way
    #print(*[num**2 for num in range(n)], sep='\n')
