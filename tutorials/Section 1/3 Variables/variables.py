#lets try to parctice what we have learned
message = 'Hello, World!' #creating a variable named message and asigning the value
print(message) #printing on screen, this will return the value of variable message

# casting : specifying data type using casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# get type of variable : identifying which type of the this variable
# we can get the type of varaible using this type() method
x1 = 5
y1 = "Narendra"
print(type(x1))
print(type(y1))

# single and double quotes
name = "Narendra" #is the same as
name1 = 'Narendra' #this
print(name, name1)

#case sensitive
a = 4
A = "Sally"
#A will not overwrite a and both are different variables lets see
print(a)
print(A)

# rules for variable names
# legal variable names
myvar = "Narendra"
my_var = "Narendra"
_my_var = "Narendra"
myVar = "Narendra"
MYVAR = "Narendra"
myvar2 = "Narendra"

# illegal variable names:
# 2myvar = "Narendra"
# my-var = "Narendra"
# my var = "Narendra"
# if we give names like above this will raise an SyntaxError: invalid syntax
# uncomment the above varaible to see the error

# multiline words varaibles:
myVariableName = "Narendra" # camelCase
MyVariableName = "Narendra" # PascalCase
my_variable_name = "Narendra" #snake_case

# many values to multiple variables
f1, f2, f3 = "Orange", "Banana", "Cherry"
print(f1)
print(f2)
print(f3)