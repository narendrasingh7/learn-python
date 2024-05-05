

You’ll learn about Python variables and how to use them effectively.

# Variables Meaning in Programming

Technically, a variable in programming is a reserved memory location to store values. These values can change during the execution of a program. The name of the variable is used to access and manipulate its stored value in the computer's memory.

Simple words:-

Variables are containers for storing data values.

Let's use the analogy of a kitchen:
Imagine you have labeled containers in your kitchen pantry. Each container has a label indicating what it holds, such as "Flour," "Sugar," "Spices," and "Rice."

* **Container Label** : Just like each container in your kitchen has a label indicating its contents, variables in programming have names that describe the type of data they hold, like `flour`, `sugar`, `spices`, and `rice`.
* **Container Contents** : Each container holds different ingredients based on its label. For example, the "Flour" container might hold all-purpose flour, while the "Sugar" container might hold granulated sugar. Similarly, variables in programming can store different types of data, like text (string), numbers (integer or float), or lists.
* **Changing Contents** : You can change what's inside each container as needed. For instance, you might refill the "Spices" container with new spices or use up the contents of the "Rice" container and then refill it. Similarly, in programming, you can update the value stored in a variable during the program's execution.

So, just like you use labeled containers in your kitchen to organize and store different ingredients, variables in programming allow you to store and manipulate different kinds of data in your code.

# Python **Variables**

In Python, a variable is a label that you can assign a value to it. And a variable is always associated with a value. For example:

```
message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)
```

Output:

```
Hello, World!
Good Bye!
```

In this example, `message` is a variable. It holds the string `'Hello, World!'`. The `print()` function shows the message `Hello, World!` to the screen.

The next line assigns the string `'Good Bye!'` to the `message` variable and print its value to the screen.

The variable `message` can hold various values at different times. And its value can change throughout the program.

## Creating variables

To define a variable, you use the following syntax:

```
variable_name = value
```

The `=` is the assignment operator. In this syntax, you assign a value to the `variable_name`.

The value can be anything like a number a string, etc., that you assign to the variable.

## Casting

If you want to specify the data type of a variable, this can be done with casting.

```
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

## Get the Type

You can get the data type of a variable with the `type()` function.

```
x = 5
y = "Narendra"
print(type(x))
print(type(y))
```

## Single or Double Quotes?

String variables can be declared either by using single or double quotes:

```
x = "Narendra"
#is the same as
x = 'Narendra'
```

## Case-Sensitive

Variable names are case-sensitive.

This will create two variables:

```
a = 4
A = "Sally"
#A will not overwrite a
```

## Rules for Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)
* A variable name cannot be any of the Python Keywords.

Legal variable names:

```
myvar = "Narendra"
my_var = "Narendra"
_my_var = "Narendra"
myVar = "Narendra"
MYVAR = "Narendra"
myvar2 = "Narendra"
```

Illegal variable names:

```
2myvar = "Narendra"
my-var = "Narendra"
my var = "Narendra"
```

## Multi Words Variable Names

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

## Camel Case

Each word, except the first, starts with a capital letter:

```
myVariableName = "Narendra"
```

## Pascal Case

Each word starts with a capital letter:

```
MyVariableName = "Narendra"
```

## Snake Case

Each word is separated by an underscore character:

```
my_variable_name = "Narendra"
```

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:

```
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

**Note:** Make sure the number of variables matches the number of values, or else you will get an error.

## One Value to Multiple Variables

And you can assign the *same* value to multiple variables in one line:

```
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

## Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called  *unpacking* .

Unpack a list:

```
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

## Output Variables

The Python `print()` function is often used to output variables. As we used this earlier.

In the `print()` function, you output multiple variables, separated by a comma:

```
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```

You can also use the `+` operator to output multiple variables:

```
print(x + y + z)
```

For numbers, the `+` character works as a mathematical operator:

```
x = 5
y = 10
print(x + y)
```

In the `print()` function, when you try to combine a string and a number with the `+` operator, Python will give you an error:

```
x = 5
y = "Narendra	"
print(x + y) # this will raise error
```

Recommended: The best way to output multiple variables in the `print()` function is to separate them with commas, which even support different data types:

## Global Variables

Variables that are created outside of a function are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Create a variable outside of a function, and use it inside the function

```
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
```

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Create a variable inside a function, with the same name as the global variable

```
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)
```

## The global Keyword

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the `global` keyword.

If you use the `global` keyword, the variable belongs to the global scope:

```
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
```

Also, use the `global` keyword if you want to change a global variable inside a function.

To change the value of a global variable inside a function, refer to the variable by using the `global` keyword:

```
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
```

Now you have learned a lot about variables, and how to use them in Python.

Go to the variables.py file and test all of our Python Variable Exercises:
