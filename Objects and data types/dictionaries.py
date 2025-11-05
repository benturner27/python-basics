#Dictionaries
#Are unordered mappings for storing objects.
#They use a key-value paring in order to retrieve objects without indexing
#Dictionaries use curly brackets and colons to signify keys and values
#The keys should always be formatted as a string, the values can be almost any data type
#For example, {"key1":"value1"}

my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)
print(my_dict["key1"])

#You can search up the value of a kay pairing by requesting it in the square brackets
prince_lookup = {"apple": 0.99, "orange": 1.29, "pear": 1.49}
print(prince_lookup["orange"])

#Dictionaries can hold different object types in it, including strings, integers, floats, lists and other dictionaries
second_dict = {"k1":200, "k2":24.587, "k3":[1, 3, 6], "k4":{"insideKey":100}}
print(second_dict["k2"])
print(second_dict["k4"]["insideKey"])

#It is possible to stack calls from dictionaries to manipulate the object in any way you want
#For example, capitalising the list entry at position 1
third_dict = {"k1": ["a", "b", "c"]}
print(third_dict["k1"][1].upper())

#You can also input new key-value pairings into dictionaries, as well as update existing pairings
fourth_dict = {"k1": "value1", "k2": "value2"}
fourth_dict["k3"] = "value3"
print(fourth_dict)
fourth_dict["k1"] = "NEW VALUE"
print(fourth_dict)

#You can also view of the the keys and values of a dictionary using the keys, values and items methods
print(fourth_dict.keys())
print(fourth_dict.values())
print(fourth_dict.items())
