#there are three types of numbers in python
# integer
# float
# complex
#lets practice what we have learned from numbers.md file.
#don't think too much to edit the code, you have learned a lot about numbers just try to change code according to you and try to play with the numbers.

# let's assign different type numbers to variable and print

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x, "is", type(x))
# you can see output for above line like --> 1 is <class 'int'> here we can see 1 has integer class that's why we can say 1 is integer type number
# similarly for float and complex
print(y, "is", type(y))
print(z, "is", type(z))


# you can use math operators like +, -, *, and / to perform calculations
print(20 + 10) # output will 30
print(20 - 10) # output will 10
print(20 * 10) # output will 200
print(20 / 10) # output will 2.0

# to calculate exponents
print(3**3) # output will 27

# to modify the order of operations
print(20 / (10 + 10)) # output will 1.0


# floats
print(0.5 + 0.5) # output 1.0
print(0.5 - 0.5) # output 0.0
print(0.5 / 0.5) # output 1.0
print(0.5 * 0.5) # output 0.25

# the division of two integers always returns a float:
print(20 / 10) # output 2.0

# if you mix an integer and a float in any arithmetic operation, the result is a float:
print(1 + 2.0) # output 3.0

# due to the internal representation of floats, Python will try to represent the result as precisely as possible. However, you may get the result that you would not expect. For example:

print(0.1 + 0.2) # output 0.30000000000000004