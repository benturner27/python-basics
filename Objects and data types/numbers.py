#Basic mathematical operators

#Addition
a = 1 + 1
print(a)

#Subtraction
b = 2 - 1
print(b)

#Multiplication
c = 2 * 2
print(c)

#Division
d = 4 / 2
print(d)

#Modulo
e = 7 % 3
print(e)

#Power multiplication
f = 2 ** 3
print(f)

#Order of operations
g = 2 + 5 * 10 + 4
print(g)

#Order of operations (Brackets taking precedent)
h = (2 + 5) * (10 + 4)
print(h)

#type assignment
print(type(h))

#Reassinging variable h as a floating point and re-checking the type
h = 27.6
print(type(h))

#basic assignment example
income = 10000
tax_rate = 0.1
taxed_income = income * tax_rate

print (taxed_income)

#You can also format floating point number to increase it's accuracy
result = 100/777
print(result)
print("The result was {r:1.3f}".format(r=result))

#The "r:1.3f" refers to the width and precision of the answer, where the 3f is referring to three positions after the
#decimal