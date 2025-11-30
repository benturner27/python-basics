#Input and Output

#Inputting and outputting file content is very useful, from working with .txt files, audio and video, as well as
#Excel spreadsheets.

#Opening a .txt file for usage

test = open('test.txt')

#There are multiple methods that can be used once the file has been opened

#The read method outputs the content of the file in its entirety
test.read()
print(test.read())

#The seek method resets the cursor that read the file to any point in the file as you please. For this example,
#The cursor is set at 0, which is the start of the file
test.seek(0)

#The readlines method outputs the content on the lines as it was originally formatted
test.readlines()
print(test.readlines())

#The close method closes the input file in order to use other files in the future
test.close()

#The with command can turn into a statement that can achieve multiple things in one block of code
with open('test.txt') as test:
    contents = test.read()
    print(contents)

#It is possible to append files using the mode parameter. In this example, the mode is set to 'a', which
#allows us to add content to the file without overwriting.
with open('test.txt', 'a') as test:
    contents = test.write("\nThis is the fourth line")

with open('test.txt', 'r') as test:
    contents = test.read()
    print(contents)

#It is also possible to overwrite the content of files by changing the mode parameter to 'w'. This can also be used
#to create new files that don't already exist.
with open('example.txt', 'w') as test:
    contents = test.write("suihdfisufqidfuvhwiuhfwdiovifjouiuhvdsvafppuihgef")

with open('example.txt', 'r') as example:
    contents = example.read()
    print(contents)
