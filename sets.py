#Sets
#Are unordered collections of unique elements
#Meaning that there can only be one representative of an objects in a set at any given time.
#For example, the litter "b" cannot show up twice in the same set

first_set = set()
print(first_set)

#You can add items into the set by using the add method
first_set.add(1)
print(first_set)

first_set.add(2)
print(first_set)

#When trying to add another values that already exists in the set, it will not show up a second time because it is
#already being represented.
#For example, the code below will not do anything.
first_set.add(2)
print(first_set)

#Even when converting lists into sets, any duplicate values will be removed for a singular representative
my_list = [1,1,1,1,2,2,2,2,3,3,3,3]
my_list = set(my_list)
print(my_list)