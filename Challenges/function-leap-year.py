"""
Problem Statement:

You are given the year, and you have to write a function to check if the year is leap or not.

Source: https://www.hackerrank.com/challenges/write-a-function/problem
"""

def leap_year(year):
    leap = False
    
    if year%4==0 and year%100!=0 or year %400 == 0:
        leap = True;
        
    #Another way: Just return bool value
    #return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap
    
if __name__ == '__main__':
    year = int(input())
    print(leap_year(year))
