'''
Copying Files
'''

#Let's copy the file Example1.txt to the file Example2.txt:
with open('resources/data/Example1.txt','r') as readfile:
    with open('resources/data/Example2.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

with open('resources/data/Example2.txt','r') as testwritefile:
    print(testwritefile.read())
    
#After reading files, we can also write data into files and save them in different file formats like .txt, .csv, .xls (for excel files) etc.