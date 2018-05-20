'''
Reading Files

We're downloading this file and will use the same for reading

!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt

/resources/data/Example1.txt
'''

example1="resources/data/Example1.txt"
file1 = open(example1,"r")

print('Name:', file1.name) #Get the name
print('Mode:', file1.mode) #Get the mode

FileContent=file1.read()
print(FileContent) #Get the file content

type(FileContent) #Type of file
file1.close() #Close the file

#Better way to open a file
'''
Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file object.
'''
with open(example1,"r") as file1:
    FileContent = file1.read() #file1.read(4) to read first four characters
    
print(FileContent)

with open(example1,"r") as file1:
    print(file1.read(4)) #Read first four charcter
    print(file1.read(4)) #Read next four character after above line
    print(file1.read(7))
    print(file1.read(15))
    
#Read one line at a time
with open(example1,"r") as file1:
    print("first line: " + file1.readline())
    
#loop to iterate through each line
with open(example1,"r") as file1:
    i=0;
    for line in file1:
        print("Iteration", str(i), ":",line)
        i=i+1;

#Retrieve text file as a list
with open(example1,"r") as file1:
    FileasList=file1.readlines()

print(FileasList[0])#line1
print(FileasList[1])#line2