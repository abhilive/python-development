"""
Problem Statement:

Read an integer N.

Without using any string methods, try to print the following:

123....N

Note that "..." represents the values in between.

Source: https://www.hackerrank.com/challenges/python-print/problem
"""

if __name__ == '__main__':
    num = int(input())
    print(*range(1, num+1), sep='')
