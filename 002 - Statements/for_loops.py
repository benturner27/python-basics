#For Loops

"""
For loop statements are a type of iteration statement that executes a block of code until a condition is met. For loop
statements can be iterated with any data type that is iterable.
"""

#An example of a for loop statement
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in mylist:
    print(item)

#Because this is an iterate statement, you can print strings for each time the statement interates
for item in mylist:
    print("No era penal!")

#You can add different type of statements in a block as well, which allows for more complex code
for item in mylist:
    #Checks each item in the list for even numbers
    if item % 2 == 0:
        print(item)
    else:
        print(f"Odd number: {item}")

#Another for loop example
mylist_sum = 0
for item in mylist:
    mylist_sum += item
    print(mylist_sum)

#This example adds the values of the list together, and adds them to a variable until the list is iterated
#The indentation makes a different for the print function, in case you just wanted to see the total sum at the end

#Another example, using a string instead of a list
mystring = "Hello World!"
for item in mystring:
    print(item)

#For the above example The for loop prints out every index of the string