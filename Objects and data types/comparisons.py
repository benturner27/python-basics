#Comparison Operators

"""
Comparison operators can be used in Python statements and methods as a way to check for logic and return certain
results. There are 6 different operations that can be used for comparison:

- == is for checking if 2 operands are equal
- != is for checking if 2 operands are not equal
- > is for checking if an operand is greater than the other
- < is for checking if an operand is less than the other
- >= is for checking if an operand is greater than or equal to the other
- <= is for checking if an operand is less than or equal to the other

the return for any of these operators will be the booleans for true or false.
"""

#Equality operator
print(2 == 2)

#These operators can be used to check the value of any data type, not just numerical ones.
print("hello" == "goodbye")

#They also take Captialisation of strings, and strings of number into account when comparing operands
print("Hello" == "hello")
print("2" == 2)
print(2.0 == 2)

#Inequality operator
print(2 != 3)

#Greater than operator
print(3 > 2)

#Less than operator
print(2 < 3)

#Greater than or equal to operator
print(3 >= 2)

#Less than or equal to operator
print(2 <= 3)

"""
It is also possible to use logical operator for chaining comparisons for a boolean result. There are three main logical
operators used:
- 'and' checks if two comparisons are true
- 'or' checks if if either comparison is true
- 'not' checks if two comparisons are false
"""

#and logical operator
print(2 > 1 and 3 > 2)

#or logical operator
print(2 > 1 or 2 < 1)

#not logical operator
print(not(2 > 3 and 5 < 4))

#The 'not' logical operator returns false if both comparisons are true
print(not(3 > 2 and 4 > 3))