# hashtage is used to comment the line of code this line will ignored while execution.

#this is correct way to write the python code using proper indentation (white spaces of 4)
if 10 > 2:
    print("Ten is greater than two!")

#lets try to write the code without proper indentaiton
#uncomment bellow two lines to see the error
# if 10 > 2:
# print("Ten is greater than two!") 

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 10 > 2:
 print("Ten is greater than two!") # work fine but not recommended 

if 10 > 2:
      print("Ten is greater than two!") # work fine but not recommended 

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!") # raise an IndentationError: unexpected indent

# Pro Tip always use same number of spaces this will make your code more readable. 
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!") # work fine because we used same number of spaces