#Lists
#Are ordered sequences that can hold multiple object types using squared brackets and separated by commas
my_list = [1, 2, 3]
print(my_list)

#You can check how long a list is by using the len function
print(len(my_list))

#You can also use indexing and slicing on a list
my_list = ["one", "two", "three"]
print(my_list[0])
print(my_list[1:])

#You can also concatenate two lists together
second_list = ["four", "five"]
print(second_list)
third_list = my_list + second_list
print(third_list)

#You can also insert new values into a list by re-assigning an indexed object
third_list[0] = "ONE ALL CAPS"
print(third_list)

#You can also append new elements to a list using the append method
third_list.append("six")
print(third_list)

#And you can remove elements off at the end of a list using the pop method
third_list.pop()
print(third_list)

#You can also sort lists by chronological order if they are not listed in that format. This method returns nothing
new_list = ["a", "f", "v", "p", "l"]
new_list.sort()
print(new_list)

#You can also sort lists by the reverse chronological order. This method also does not return a value
new_list.reverse()
print(new_list)