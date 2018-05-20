'''
Writing Files

'''
#Mode 'r' will remove all file data and write after that

with open('resources/data/Example1.txt', 'w') as writefile: #Here mode is 'w' means write
    writefile.write("This is line A")

#Read file to check if it worked

with open('resources/data/Example1.txt', 'r') as testReadFile:
    print(testReadFile.read())
    
#Write multiple lines
with open('resources/data/Example1.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
#By setting the append mode 'a', we can append new line
with open('resources/data/Example1.txt', 'a') as writefile:
    writefile.write("This is line C\n")
    
#Write a list to a .txt file as follows
lines=["This is line P\n", "This is line Q\n", "This is line R\n"]

with open('resources/data/Example1.txt', 'w') as writefile:
    for line in lines:
        writefile.write(line)
        
#We can verify the file is written by reading it and printing out the values:
with open('resources/data/Example1.txt','r') as testwritefile:
    print(testwritefile.read())