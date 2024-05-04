# General Meaning of Comment

A comment is basically  **a text note that gives an explanation about the source code** . Furthermore, they act as documentation in the source code. We include comments to increase the readability of the program. Besides, comments make it easy for the programmer to remember the complex things added to the code.

# Python **Comments**

Sometimes, you want to document the python code that you write. For example, you may want to note why a piece of code works. To do it, you use the comments.

Typically, you use comments to explain formulas, algorithms, and complex business logic.

When executing a program, the Python interpreter ignores the comments and only interprets the code.

Python provides three kinds of comments including block comment, inline comment, and documentation string.

## Python block comments

A block comment explains the code that follows it. Typically, you indent a block comment at the same level as the code block.

To create a block comment, you start with a single hash sign (`#`) followed by a single space and a text string. For example:

```
# increase price by 5%
price = price * 1.05
```

## Python inline comments

When you place a comment on the same line as a statement, you’ll have an inline comment.

Similar to a block comment, an inline comment begins with a single hash sign (`#`) and is followed by a space and a text string.

The following example illustrates an inline comment:

```
salary = salary * 1.02   # increase salary by 2%
```

## Python docstrings

A docstring is a string placed at the beginning of a code block, like a function, to provide documentation. Unlike regular comments, docstrings can be accessed at runtime using `obj.__doc__`. They're used to generate code documentation.

Documentation strings is called docstrings.

Technically speaking, docstrings are not the comments. They create anonymous variables that reference the strings. Also, they’re not ignored by the Python interpreter.

Python provides two kinds of docstrings: one-line docstrings and multi-line docstrings.

### 1) One-line docstrings

As its name implies, a one-line docstring fits one line. A one-line docstring begins with triple quotes (`"""`) and also ends with triple quotes (`"""`). Also, there won’t be any blank line either before or after the one-line docstring.

The following example illustrates a one-line docstring in the `quicksort()` function:

```
def quicksort():
""" sort the list using quicksort algorithm """
...Code language: Python (python)
```

### 2) Multi-line docstrings

Unlike a one-line docstring, a multi-line docstring can span multiple lines. A multi-line docstring also starts with triple quotes (`"""`) and ends with triple quotes (`"""`).

The following example shows you how to use multi-line docstrings:

```
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """
```

## Python multiline comments

Python doesn’t support multiline comments.

However, you can use multi-line docstrings as multiline comments
