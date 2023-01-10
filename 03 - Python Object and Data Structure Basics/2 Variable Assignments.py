## Variable Assignment
"""
Rules for variable name:
- cannot start with a number
- cannot use :'"<>/?|\()!@#$%%&*~-+
- use numbers and letters!
"""

## Dynamic Typing
"""
Python lets you reassign the datatype of a variable
    Pros:
        - Very easy and fast
    Cons:
        - May yield bugs, you should be aware of the type

We can use the type() function to determine type of variable

"""

my_dogs = 2;
my_dogs = "Sammy";
print(my_dogs); # Sammy

### Example

a = 5;
print ( a+ a) # 10

a = a + a; # 10
print(type(a)); # <class 'int'>

### Example:

my_income = 100
tax_rate = 0.1
my_taxed = my_income * tax_rate
print(my_taxed) # 10.0
