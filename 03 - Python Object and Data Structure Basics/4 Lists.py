###########################################################################################

print("#"*40)

""" 
We can create lists of mixed types:
    my_list['STRING',100,23.2]

Elements can be accessed through indexing and splicing like strings:

my_list = ['one','two','three']
mylist[1:] is ['two', 'three']

We can merge lists using +

['one','two','three'] + ['four','five','six']
"""

# Lists are mutable:
my_list = ['one','two','three']+['four', 'five']
my_list[0] = "hello world"
print(my_list) # ['hello world', 'two', 'three', 'four', 'five']

"""
The .append() method is used to add to end of list
"""
my_list.append("six")
print(my_list) # ['hello world', 'two', 'three', 'four', 'five', 'six']


"""
The .pop() method removes last elementof list
"""
popped_item = my_list.pop() # 'six'
print(my_list) # ['hello world', 'two', 'three', 'four', 'five']

"""
The .sort() method sorts the list in place! It does not return anything!
"""
letters = ['x','e','c','i', 'd']
letters.sort()
print(letters) # ['c', 'd', 'e', 'i', 'x']

"""
reverse() reverse an array in place
"""