# Strings

"""
Strings are sequences of characters wrapped with quotations
They are orded sequence meaning with can slice and splice them
The characters are zero indexed
We can also use negatived index to access the end of the string
we use the len() function to get length
"""

shiv = "Shiv Kumar"
print(shiv[0]) # S
print(shiv[-1]) # r

# print(shiv[-11]) # throws error

print(len(shiv)) # 10
# print(shiv.len) # does not work

"""
If a string contains a single quote, we can wrap it with double quotes
"""
# 'I'm going for run' # throws error
"I'm going for run"

"""
There are escape characters:
    \n - new line
"""

print("hello\nworld")


## Slicing and Indexing

myString = 'abcdefghijklmnopqrstuvxyz'

print(myString[1:]) # bcdefghijklmnopqrstuvxyz
print(myString[3:6]) # def

"""We can define steps with third parameter"""
print(myString[::]) # abcdefghijklmnopqrstuvxyz
print(myString[::2]) # acegikmoqsuxz

## String Properties and Methods

# Strings are immutable!
name = "Shiv"
# name[2] = "o" # TypeError: 'str' object does not support item assignment

newName = name[0:2] + "o" + name[-1]
print(newName) # shov

# multiplying letters
print("z"*10) # zzzzzzzzzz

## string attributes:
x = "Hello World";
print(x.upper()) # HELLO WORLD
print(x.lower()) # hello world
print(x.split()) # ['Hello', 'World']
print(x.split("o")) # ['Hell', ' W', 'rld']

####################################################################################

# Print Formatting With Strings

print("#######################################################")

"""
We shall explore the .format() method
The .format method lets you insert strings within another string
"""

print("The {} {} {}".format("fox", "brown", "quick")); # The fox brown quick

# we can specify the positions manually

print("The {1} {0} {2}".format("fox", "brown", "quick")); # The brown fox quick

# we can make variables for the parameters of the format() method

print("The {q} {b} {f}".format(f="fox",b="brown",q="quick")); # The quick brown fox


## formatting numbers:

result = 10/77
print(result) # 0.12987012987012986

print("The result is: {r}".format(r=result)) # The result is: 0.12987012987012986


print("The result is: {r:1.3f}".format(r=result)) # The result is: 0.130

# Float formatting follows "{value:width.precision f}"
# generally the precision number determines the number of decimal places

# theres a more up to date method
name = "Jose"
print(f'Hello. His name is: {name}') # Hello. His name is: Jose

