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
