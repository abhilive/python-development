"""
Dictionaries

 A dictionary are a type of collections, it consists of keys and values.
 It is helpful to compare a dictionary to a list. Instead of the numerical indexes such as a list, dictionaries have keys. These keys are labels that are used to access values within a dictionary.
 
"""


#Sample dictionary
Dict={"key1":1,"key2":"2","key3":[3,3,3],"key4":(4,4,4),('key5'):5,(0,1):6}
print(Dict)

Dict["key1"] #Keys can be string

Dict[(0,1)] #Keys can also be any immutable object such as a tuple

print(Dict["key1"]) #Retieve value based on key

Dict.keys() #Retrieve the keys of the dictionary
Dict.values() #Retrieve the values of the dictionary

del(Dict['key1']) #Delete any entry

'key1' in Dict #verify if element is in dictionary returns boolean
