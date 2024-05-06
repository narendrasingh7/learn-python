#lets try to practice what we have learned
print("-------------------creating variable-------------------")
message = 'Hello, World!' #creating a variable named message and asigning the value
print(message) #printing on screen, this will return the value of variable message


print("-------------------casting-------------------")
# casting : specifying data type using casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


print("-------------------getting type of variable-------------------")
# get type of variable : identifying which type of the this variable
# we can get the type of varaible using this type() method
x1 = 5
y1 = "Narendra"
print(type(x1))
print(type(y1))


print("-------------------single and double quotes-------------------")
# single and double quotes
name = "Narendra" #is the same as
name1 = 'Narendra' #this
print(name, name1)


print("-------------------case sensitive-------------------")
# case sensitive
a = 4
A = "Sally"
# a will not overwrite a and both are different variables lets see
print(a)
print(A)


print("-------------------legal variable names this are working fine-------------------")
# rules for variable names
# legal variable names
myvar = "Narendra"
my_var = "Narendra"
_my_var = "Narendra"
myVar = "Narendra"
MYVAR = "Narendra"
myvar2 = "Narendra"
print(my_var) #you can try to print all the variable to test


# print("-------------------illegal variable names-------------------")
# illegal variable names:
# 2myvar = "Narendra"
# my-var = "Narendra"
# my var = "Narendra"
# if we give names like above this will raise an SyntaxError: invalid syntax
# uncomment the above varaible to see the error


print("-------------------multiple words varaibles name casing-------------------")
# multilple words varaibles:
myVariableName = "Narendra singh" # camelCase
MyVariableName = "Narendra" # PascalCase
my_variable_name = "Narendra" #snake_case
print(myVariableName)


print("-------------------assigning values to multiple variables in one line-------------------")
# we can assign values to multiple variables in one line
# make sure the number of variables matches the number of values
f1, f2, f3 = "Orange", "Banana", "Cherry"
print(f1)
print(f2)
print(f3)


print("-------------------unpacking a collection-------------------")
# unpack a collection : this is very usefule when we have list of many values
# make sure the number of variables matches the number of values otherwise get error like --> ValueError: too many values to unpack (expected 2)
fruits = ["apple", "banana", "cherry"]
fruit1, fruit2, fruit3 = fruits
print(fruit1)
print(fruit2)
print(fruit3)


print("-------------------ways to output variables-------------------")
# ways to output variables
# python print() function is often used to output variables
# python allows outputing multiple variables by separating with comma lets see bellow
var1 = "Python"
var2 = "is"
var3 = "awesome"
print(var1, var2, var3)
# we can also use the + operator to output multiple variables
var4 = "Python "
var5 = "is "
var6 = "awesome"
print(var4 + var5 + var6)
#notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome". see output of bellow line in console
print(var1 + var2 + var3)
# for numbers, the + character works as a mathematical operator lets see
number1 = 5
number2 = 10
print(number1 + number2) # output will be addition of this tow numbers
# we can't combine two different data type variable using + operator if we do will get error like --> TypeError: unsupported operand type(s) for +: 'int' and 'str'
#uncomment bellow three line and run to see error
# int_type = 5
# string_type = "John"
# print(int_type + string_type)


print("-------------------global variables-------------------")
# global variables : global variables can be used by everyone, both inside of functions and outside.
# creating a variable outside of a function
global_var = "awesome"

def myfunc():
  print("Python is " + global_var)

myfunc()


print("-------------------using globle keyword-------------------")
# the global keyword : to create a global variable inside a function, you can use the global keyword.
def myfunc1():
  global global_var_inside_function
  global_var_inside_function = "fantastic"

myfunc1()

print("Python is " + global_var_inside_function)