You’ll learn about Python string and its basic operations.

# Python **Strings**

Python strings are sequences of characters, which can include letters, numbers, symbols, and spaces. They are immutable, meaning once created, you cannot change the contents of the string - you can only create new strings.

You can use either single or double quotes. For example:

double_quotes = "A string is a series of characters. In Python, anything inside quotes is a string."
single_quotes = 'A string is a series of characters. In Python, anything inside quotes is a string.'

both above are same and we can display with the `print()` function: like bellow

```
print(double_quotes)
print(single_quotes)
```

You can display a string literal with the `print()` function:

```
print("Hello")
print('Hello')
```

## Quotes Inside Quotes

You can use quotes inside a string, as long as they don't match the quotes surrounding the string.

If a string contains a single quote, you should place it in double-quotes like this:

```
message = "It's a string"
```

And when a string contains double quotes, you can use the single quotes:

```
message = '"Python is awesome". Said Narendra singh'
```

To escape the quotes, you use the backslash (`\`). For example:

```
message = 'It\'s also a valid string'
```

The Python interpreter will treat the backslash character (\) special. If you don’t want it to do so, you can use raw strings by adding the letter `r` before the first quote. For example:

```
message = r'C:\python\bin'
```

## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

```
a = "Hello"
print(a)
```

## Using variables in Python strings with the f-string

Sometimes, you want to use the values of variables in a string.

For example, you may want to use the value of the `name` variable inside the `message` string variable:

```
name = 'Narendra'
message = 'Hi'
```

To do it, you place the letter `f` before the opening quotation mark and put the brace around the variable name:

```
name = 'Narendra'
message = f'Hi {name}'
print(message)
```

Python will replace the `{name}` by the value of the `name` variable. The code will show the following on the screen:

```
Hi Narendra
```

The `message` is a format string, or f-string in short. Python introduced the f-string in version 3.6.

## Multiline Strings

You can assign a multiline string to a variable by using three (single or double) quotes.

Using three single quotes:

```
details ='''
Name: Narendra Singh
Age: 22+
Occupation: Helping people + Software engineer
GitHub: narendrasingh7
LeetCode: narendrasingh7
'''

print(details)
```

It’ll output the following if you execute the program:

```
Name: Narendra Singh
Age: 22+
Occupation: Helping people + Software engineer
GitHub: narendrasingh7
LeetCode: narendrasingh7
```

**Note:** in the result, the line breaks are inserted at the same position as in the code.

Similarly you can use double qoutes, result will be the same.

```
details ="""
Name: Narendra Singh
Age: 22+
Occupation: Helping people + Software engineer
GitHub: narendrasingh7
LeetCode: narendrasingh7
"""

print(details)
```

## Strings are Arrays

In Python, strings are arrays of bytes representing Unicode characters. Unlike some other languages, Python doesn't have a separate character data type; instead, a single character is just a string with a length of 1. You can use square brackets to access elements of the string.

Since a string is a sequence of characters, you can access its elements using an index. The first character in the string has an index of zero.

The following example shows how to access elements using an index:

```
str = "Python String"
print(str[0]) # output: P
print(str[1]) # output: y

```

If you use a negative index, Python returns the character starting from the end of the string.

```
str = "Python String"
print(str[-1])  # output: g
print(str[-2])  # output: n
```

The following illustrates the indexes of the string `"Python String"`:

```
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
```

## Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

Loop through the letters in the word "banana":

```
for x in "banana":
    print(x)
```

If you are reading about  loop first time don't worry for now just think loop is used to do same task again and again. We will cover  this in letter in "conditionals in python" tutorials.

Here for loop iterate through all the letters in the word "banana" and print each letters on the screen.

## Getting the length of a string

To get the length of a string, python has predefined len() function and you use the `len()` function to get the length of string.

```
str = "Python String"
str_len = len(str)
print(str_len) #output: 13
```

## Check character is present in String

To check if a certain phrase or character is present in a string, we can use the keyword `in`.

Check if "free" is present in the following text:

```
txt = "The best things in life are free!"
print("free" in txt)
```

## Check if character is NOT present in String

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

Check if "expensive" is NOT present in the following text:

```
txt = "The best things in life are free!"
print("expensive" not in txt)
```

## Python - **Slicing Strings**

Slicing allows you to get a substring from a string. For example:

```
str = "Python String"
print(str[0:2]) Output: Py
```

The `str[0:2]` returns a substring that includes the character from the index 0 (included) to 2 (excluded).

The syntax for slicing is as follows:

```
string[start:end]
```

The substring always includes the character at the `start` and excludes the string at the `end`.

The `start` and `end` are optional. If you omit the `start`, it defaults to zero. If you omit the `end`, it defaults to the string’s length.

## Slice From the Start

By leaving out the start index, the range will start at the first character:

Get the characters from the start to position 5 (not included):

```
b = "Hello, World!"
print(b[:5])
```

## Slice To the End

By leaving out the end index, the range will go to the end:

Get the characters from position 2, and all the way to the end:

```
b = "Hello, World!"
print(b[2:])
```

## Negative Indexing

Use negative indexes to start the slice from the end of the string:

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

```
b = "Hello, World!"
print(b[-5:-2])
```

## Python - **Modify Strings**

Python has a set of built-in methods that you can use on strings.

## Upper Case

The `upper()` method returns the string in upper case:

```
a = "Hello, World!"
print(a.upper())
```

## Lower Case

The `lower()` method returns the string in lower case:

```
a = "Hello, World!"
print(a.lower())
```

## Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The `strip()` method removes any whitespace from the beginning or the end:

```
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

## Replace String

The `replace()` method replaces a string with another string:

```
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Split String

The `split()` method returns a list where the text between the specified separator becomes the list items.

The `split()` method splits the string into substrings if it finds instances of the separator:

```
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
