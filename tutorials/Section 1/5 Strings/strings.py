# lets practice, what we have learned from strings.md file

print("-------------------Python Strings-------------------")
# In Python, A string is a series of characters and anything inside quotes is a string.
# we use single or double quotes to create strings
# let's create a string and store in a valriable called name

name_double = "Narendra" # or we can use single quotes
name_single = 'Narendra'

# while practicing you can try with your name instead of Narendra
# lets print this string to the screeen

print(name_double)
print(name_single)

# both will output Narendra
# let's check the type of this variables

print(type(name_double)) # output : <class 'str'>
print(type(name_single)) # output : <class 'str'>



print("-------------------Quotes Inside Quotes-------------------")
# you might be thinking like if everything inside the single or double qoutes are strings in python 
# then if I need to print quotes as well then how I can?
# don't worry python has solution for it 
# let's try
# you can use quotes inside a string If a string contains a single quote, you should place it in double-quotes like this:

message = "It's a string"
print(message)

# and when a string contains double quotes, you can use the single quotes:

message1 = '"Python is awesome". Said Narendra Singh'
print(message1)

# you can see the output and found that both massege contains quotes into them
# how cool it was right?

# let's do this same without using another quotes
# for doing this you can escape the quotes by using the backslash (\). let's see

message_with_quotes = 'It\'s also a valid string'
print(message_with_quotes)

# the Python interpreter will treat the backslash character (\) special. If you don’t want it to do so,
# you can use raw strings by adding the letter `r` before the first quote. see bellow
path = r'C:\python\bin'
print(path)



print("-------------------Assign String to a Variable-------------------")
# assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello" # we already dit it in above practices
print(a)



print("-------------------Using variables in Python strings with the f-string-------------------")
# sometimes, you want to use the values of variables in a string.
# To do it, you need to place the letter `f` before the opening quotation mark and put the brace around the variable name 
# let's see

name = 'Narendra'
message = f'Hi {name}' # python will replace the `{name}` by the value of the `name` variable
print(message) # output --> Hi Narendra



print("-------------------Multiline Strings in Python-------------------")
# now you might be thinking like you need to display the details of a person and you can't write this into single line due to less readability
# and how can we assign multiline strings to a variable, for this python has Multiline Strings let's see
# You can assign a multiline string to a variable by using three (single or double) quotes. 

details ='''
  Name: Narendra Singh
  Age: 22+
  Occupation: Helping people + Software engineer
  GitHub: narendrasingh7
  LeetCode: narendrasingh7
'''
# now if you print this details variable it will display the string in same formate in which you written like it will contain all the spaces and line breaks you have added.

print(details)

# Note: in the result, the line breaks are inserted at the same position as in the code.
# similarly you can use double qoutes instead of single quotes, result will be same and this is task for you to do it. 