#Strings
#Are a sequence of characters that are inside single or double quotation marks
a = 'hello'
b = "world"
c = "This is also a string"
print(a)
print(b)
print(c)

#When using apostrophes in strings, it's best to use double quotes. That way, there will be no syntax errors
d = "I'm going on a run"
print(d)

#You can print strings either directly in the parameter for the print function, or through inputting a variable
print("Hello, world!")

#You can print strings on different lines using the "\n" escape sequence
print("Hello,\nworld!")

#You can also indent different parts of a string using the "\t" escape sequence
print("Hello,\tworld!")

#You can use the len function to check the length of a string
print(len(c))

#You can fetch the index of a character in a string and output it to the print function.
print(c[3])

#This also works for reverse indexing
print(c[-3])

#You can also slice sections of a string using the colon symbol in the index brackets
print(c[5:])

#This also works for slicing at the start of the string
print(c[:5])

#This also works when you're tyring to slice a section of the string that doesn't include the start of end points
print(c[5:8])

#You can also grab the whole string using the double colon notation, though this is rarely used
print(c[::])

#Though, the double notation is more commonly used for step sizing, such as grabbing every other character in a string
print(c[::2])

#Step sizing can also be used to grab specific characters in a range from the string
print(c[3:13:3])