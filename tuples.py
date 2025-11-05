#Tuples
#Are very similar to lists, however they are immutable, which means that cannot be changed
#Once an element has be assigned in a tuple, that element cannot be changed
#Tuples are inserted between brackets, separated by commas

first_tuple = (1, 2, 3)
print(first_tuple)

#You can have multiple data types withing the same tuple. Indexing and slicing also works on tuples like lists
second_tuple = ("one", 2.0, 3)
print(second_tuple[0])
print(second_tuple[1:])

#You can count how many times a value is in a tuple, as well as the first index it happens
third_tuple = (1, 1, 2, 3, 5)
print(third_tuple.count(1))
print(third_tuple.index(3))

