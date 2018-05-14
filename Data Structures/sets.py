"""
Sets

 A set is a unique collection of objects in Python. You can denote a set with a curly bracket {}.
 Python will remove duplicate items.
"""

#Sample set
set1={"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

#Create set from a list
album_list =[ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]

album_set = set(album_list)             
print(album_set)

#Example create set of generes
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)

#Get Sum
A=[1,2,2,1]
B=set(A)
print("Sum of list A: %d"%sum(A))
print("Sum of Set B: %d"%sum(B))

#Operations
A = set(["Thriller","Back in Black", "AC/DC"] )
A.add("NSYNC") #To add an element
A.remove("NSYNC") #To remove an element
"AC/DC" in A #To verify if element in set returns boolean True or False

album_set1 = set(["Thriller",'AC/DC', 'Back in Black'] )
album_set2 = set([ "AC/DC","Back in Black", "The Dark Side of the Moon"] )

album_set_3=album_set1 & album_set2 #Find intersection Or common elements
album_set1.intersection(album_set2) #Another way find intersection 

album_set1.difference(album_set2) #Find all elements that are only contained in set album_set1
album_set2.difference(album_set1) #Similarly the difference of album_set2 and album_set1

album_set1.union(album_set2) #Find union of two sets

album_set1.issuperset(album_set2) #Check whether set is set is a superset of another set
album_set2.issubset(album_set1) #Check whether set is a subset of another set
