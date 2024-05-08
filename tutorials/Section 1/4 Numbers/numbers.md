You’ll learn about Python numbers and how to use them in programs.

## Python Numbers

Numbers in Python refer to the  **numeric data types in Python programming** . Python supports three kinds of numeric data types:

* `int`
* `float`
* `complex`

  ```
  x = 1    # int
  y = 2.8  # float
  z = 1j   # complex
  ```

As we previously (in variables part) learned about how to verify the type of any object or variable in Python, by using the `type()` function: we can get the type of any object by this.

```
print(type(x))
print(type(y))
print(type(z))
```

Variables of numeric types are created when you assign a value to them:

## ****Integer (int)****

****Python int is**** the whole number, including negative numbers but not fractions and without decimals, of unlimited length. In Python, there is no limit to how long an integer value can be.

The integers are numbers such as -1, 0, 1, 2, and 3, .. and they have type `int`.

```
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
```

You can use Math operators like +, -, *, and / to form expressions that include integers. For example:

```
print(20 + 10) # output will 30
print(20 - 10) # output will 10
print(20 * 10) # output will 200
print(20 / 10) # output will 2.0

```

To calculate exponents, you use two multiplication symbols (`**`). For example:

```
print(3**3) # output will 27
```

To modify the order of operations, you use the parentheses `()`. For example:

```
print(20 / (10 + 10)) # output will 1.0
```

## ****Floats (float)****

This is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation. . Some examples of numbers that are represented as floats are 0.5 and -7.823457.

They can be created directly by entering a number with a decimal point, or by using operations such as division on integers.

```
x = 1.10
y = 1.0
z = -35.59print(type(x))
print(type(y))
print(type(z))
```

Float can also be scientific numbers with an "e" to indicate the power of 10.

```
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
```

In general, you can use floats like integers. For example:

```
print(0.5 + 0.5) # output 1.0
print(0.5 - 0.5) # output 0.0
print(0.5 / 0.5) # output 1.0
print(0.5 * 0.5) # output 0.25
```

The division of two integers always returns a float:

```
print(20 / 10) # output 2.0
```

If you mix an integer and a float in any arithmetic operation, the result is a float:

```
print(1 + 2.0) # output 3.0
```

Due to the internal representation of floats, Python will try to represent the result as precisely as possible. However, you may get the result that you would not expect. For example:

```
print(0.1 + 0.2) # output 0.30000000000000004
```

## Complex

Not only real numbers, Python can also handle complex numbers and its associated functions using the file “cmath”. Complex numbers have their uses in many applications related to mathematics and python provides useful tools to handle and manipulate them. ****Converting real numbers to complex number**** An complex number is represented by “**** x + yi**** “. Python converts the real numbers x and y into complex using the function  ****complex(x,y)**** . The real part can be accessed using the function**** real()**** and imaginary part can be represented by  ****imag()**** .

```
import cmath

# Initializing real numbers
x = 5
y = 3

# converting x and y into complex number
z = complex(x, y)

# printing real and imaginary part of complex number
print("The real part of complex number is:", z.real)
print("The imaginary part of complex number is:", z.imag)

Output
The real part of complex number is: 5.0
The imaginary part of complex number is: 3.0
```

An alternative way to initialize a complex number

Below is the implementation of how can we make complex no. without using complex() function.

Complex numbers are written with a "j" as the imaginary part.

```
x = 3+5j
y = 5j
z = -5jprint(type(x))
print(type(y))
print(type(z))
```

## Underscores in numbers

When a number is large, it’ll become difficult to read. For example:

```
count = 10000000000
```

To make the long numbers more readable, you can group digits using underscores, like this:

```
count = 10_000_000_000
```

When storing these values, Python just ignores the underscores. It does so when displaying the numbers with underscores on the screen:

```
count = 10_000_000_000
print(count)

Output:
10000000000
```

The underscores also work for both integers and floats.

## Type Conversion

You can convert from one type to another with the `int()`, `float()`, and `complex()` methods:

Convert from one type to another:

```
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

**Note:** You cannot convert complex numbers into another number type.

## Random Number

Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:

```
import random

print(random.randrange(1, 10))
```



That's It............... Now you can easily play with python number. Just go to numbers.py file and test and modify code as you want for experimenting what you have learned.

Happy coding..................................................................................................................................
