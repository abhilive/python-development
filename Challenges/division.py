"""
Problem Statement:
Read two integers and print two lines.
    The first line should contain integer division, // .
    The second line should contain float division, / .

You don't need to perform any rounding or formatting operations. 

Source: https://www.hackerrank.com/challenges/python-division/problem
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print("%d\n%f"%(a//b,a/b))
    #Another Way
    #print("{0}\n{1}".format((a//b),(a/b)))
