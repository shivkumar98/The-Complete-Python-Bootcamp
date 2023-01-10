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