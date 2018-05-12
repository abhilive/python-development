"""
Problem Statement:

Consider a list (list = []). You can perform the following commands:

    1. insert i e: Insert integer e at position i.
    2. print: Print the list.
    3. remove e: Delete the first occurrence of integer e.
    4. append e: Insert integer e at the end of the list.
    5. sort: Sort the list.
    6. pop: Pop the last element from the list.
    7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Source: https://www.hackerrank.com/challenges/python-lists/problem
"""

if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd == 'append':
            list.append(int(args[0]))
        if cmd == 'print':
            print(list)
        if cmd == 'insert':
            list.insert(int(args[0]), int(args[1]))
        if cmd == 'reverse':
            list = list[::-1]
        if cmd == 'pop':
            list.pop()
        if cmd == 'sort':
            list = sorted(list)
        if cmd == 'remove':
            list.remove(int(args[0]))
        #Another Way using eval
        '''
        if cmd!='print' :
            cmd += "(" +",".join(args)+ ")"
            eval("list."+cmd)
        else:
            print(list)
        '''
        
