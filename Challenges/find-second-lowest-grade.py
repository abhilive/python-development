"""
Problem Statement:

Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Source: https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':

    #1 Another Way to get inputs
    '''
    n = int(input())
    scores = [[input(), float(input())] for _ in range(n)]
    '''

    #2 Another Way to get inputs
    '''
    scores = []
    for _ in range(0, int(input())):
        scores.append([input(), float(input())])
    '''
    
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name,score])
        
    second_low = sorted(set([marks for name,marks in scores]))[1];

    print('\n'.join(sorted(name for name,marks in scores if marks==second_low)))
    
