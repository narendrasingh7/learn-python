

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

## ****Python Integer (int)****

****Python int is**** the whole number, including negative numbers but not fractions and without decimals, of unlimited length. In Python, there is no limit to how long an integer value can be.

The integers are numbers such as -1, 0, 1, 2, and 3, .. and they have type `int`.

```
x = 1
y = 35656222554887711
z = -3255522print(type(x))
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

## ****Python Floats (float)****

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
z = -87.7e100print(type(x))
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
