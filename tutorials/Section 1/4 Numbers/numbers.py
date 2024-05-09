# there are three types of numbers in python
# integer
# float
# complex
# lets practice what we have learned from numbers.md file.
# don't think too much to edit the code, you have learned a lot about numbers just try to change code according to you and try to play with the numbers.

# let's assign different type numbers to variable and print
print("-------------------Integer numbers-------------------")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x, "is", type(x))
# you can see output for above line like --> 1 is <class 'int'> here we can see 1 has integer class that's why we can say 1 is integer type number
# similarly for float and complex
print(y, "is", type(y))
print(z, "is", type(z))


print("-------------------Using math operators-------------------")
# you can use math operators like +, -, *, and / to perform calculations
print(20 + 10) # output will 30
print(20 - 10) # output will 10
print(20 * 10) # output will 200
print(20 / 10) # output will 2.0

print("-------------------Calculating exponents-------------------")
# to calculate exponents
print(3**3) # output will 27

print("-------------------Modify the order of operations-------------------")
# to modify the order of operations
print(20 / (10 + 10)) # output will 1.0


print("-------------------Floating numbers-------------------")
# floats
print(0.5 + 0.5) # output 1.0
print(0.5 - 0.5) # output 0.0
print(0.5 / 0.5) # output 1.0
print(0.5 * 0.5) # output 0.25

print("-------------------Division of two integers-------------------")
# the division of two integers always returns a float:
print(20 / 10) # output 2.0

print("-------------------Mixing integer and float-------------------")
# if you mix an integer and a float in any arithmetic operation, the result is a float:
print(1 + 2.0) # output 3.0

print("-------------------Internal representation of floats-------------------")
# due to the internal representation of floats, Python will try to represent the result as precisely as possible. However, you may get the result that you would not expect. For example:
print(0.1 + 0.2) # output 0.30000000000000004


print("-------------------Complex numbers-------------------\n")
# Complex number
# complex numbers are written with a "j" as the imaginary part.
num = 3+5j
num1 = 5j
num3 = -5j
# printing real and imaginary part of complex number
print("The real part of complex number is:", num.real)
print("The imaginary part of complex number is:", num.imag, "\n") #"\n" just used for new line
print("The real part of complex number is:", num1.real)
print("The imaginary part of complex number is:", num1.imag, "\n")
print("The real part of complex number is:", num3.real)
print("The imaginary part of complex number is:", num3.imag, "\n")
# we already learn how to get check if number is complex just
print("Type on", num, "is", type(num),"\n")


print("-------------------Underscores in numbers-------------------\n")
# Underscores in numbers
# to make the long numbers more readable, you can group digits using underscores
#let's see
count = 10_000_000_000
print(count) # output 10000000000 because python just ignores the underscores while storing the number


print("-------------------Type Conversion-------------------\n")
# Type Conversion
# you can convert from one type to another with the `int()`, `float()`, and `complex()` methods:
# let's see
integer_number = 1    # int
floating_number = 2.8  # float
complex_number = 1j   # complex

#convert from int to float:
a = float(integer_number)
#convert from float to int:
b = int(floating_number)
#convert from int to complex:
c = complex(integer_number)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Note: you cannot convert complex numbers into another number type.
# can_not = float(complex_number) # will get error like: TypeError: can't convert complex to float

print("-------------------Random Number-------------------\n")
# Random Number
# python does not have a random() but Python has a built-in module called `random` that can be used to make random numbers:
import random # if you not import tht module will get error : NameError: name 'random' is not defined
print(random.randrange(1, 100)) # output may be any number between 1 to 100

# that's it you have practiced a lot now you are able to do any type of operation using python numbers
# please keep practice otherwise you may forgot some syntax or concept.

print("\nHappy coding....'Remember: Practice is the Best Practice to Understand and Learn Coding Practically'....")