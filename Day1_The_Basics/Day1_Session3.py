# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ___Basic Programming constructs:___
# 
# * Conditions : If, else, elif
# * Loops: while, break, continue, for
# * Interactive mode, file mode, dir, help, type
# * Advanced Data Structures: Containers – list, tuple, dictionary, set, Frozenset

# <headingcell level=4>

# Conditions:

# <markdowncell>

# __if:__
# 
# ```python
# if (condition):
#     do something
# ```
# 
# * The if block is executed when `condition` evavulates to True
# * The block after `if` starts with an indentation

# <markdowncell>

# __Python `Truthiness`__ :
# 
# * 0, 0.0, None, '' (empty string) all evaluates to False
# * Any non-zero number and string evaluates to True
# 
# * Any empty container types will evaluate to False (covered later)

# <markdowncell>

# __Boolean Operators__:
# 
# ```python
# and
# or
# not
# ```

# <markdowncell>

# __The `else` condition__:
# 
# ```python
# if (condition):
#     do something
# else:
#     do this
# ```
# * The `else` keyword does not take any conditions.
# * Executes when the previous conditions are evaluated to false
# 
# e.g.:
# 
# ```python
# if (10%2):
#     print "Number is odd"
# else:
#     print "Number is even"
# ```

# <markdowncell>

# __The `elif` condition__:
# 
# ```python
# if (weekdays):
#     work
# elif (saturday):
#     play
# else:
#     rest
# ```
# * The `elif` keyword takes conditions similar to `if`.
# * useful for handling different cases
# 
# e.g.:
# 
# ```python
# x = 108
# if not (x%15):
#     print "Number is perfectly divisible by 3 and 5"
# elif not(x%5):
#     print "Number is perfectly divisible by 5 but not by 3"
# elif not(x%3):
#     print "Number is perfectly divisible by 3 but not by 5"
# else:
#     print "Number is not perfectly divisible by 3 or 5"
# ```

# <codecell>

x = 108
if not (x%15):
    print "Number is perfectly divisible by 3 and 5"
elif not(x%5):
    print "Number is perfectly divisible by 5 but not by 3"
elif not(x%3):
    print "Number is perfectly divisible by 3 but not by 5"
else:
    print "Number is not perfectly divisible by 3 or 5"

# <markdowncell>

# __while loop:__
# 
# * syntax:
# ```python
# while weekday:
#     keep working
# ```
# 
# * similar to `if` in checking a condtion.
# * But continues to execute the code block while the condition is True.
# * So this will run forever:
# 
# ```python
# while True:
#     print "I am running for ever"
# ```
# 
# * so we typically need to alter the `condition` in the code block 
# 

# <markdowncell>

# __for:__
# 
# ```python
# for temp_variable in collection:
#     do something
# ```
# 
# * e.g.:
# 
# ```python
# for num in (1,2,3,4,5,6,7,8,9,10):
#     if num%2:
#         print num, "is Odd"
#     else:
#         print num, "is Even"
# ```
# 
# * The `for` loop goes through each item one by one.
# * in the above example `num` takes new value each time.

# <markdowncell>

# __break and continue:__
# 
# ```python
# break
# ```
# 
# * this statement makes the program to exit from the loop it is executing
# ```python
# for num in (1,2,3,4,5,6,7,8,9,10):
#     if num%5:
#         print "I am okay with the number ", 5
#     else:
#         print "I hate multiples of 5. I am quitting this loop"
#         break
# ```        
# =======================
# 
# ```python
# continue
# ```
# 
# * this statement makes the program to skip the rest of the loop and go to next cycle
# 
# ```python
# #medical checks for a health insurance scheme
# for age in (20, 30, 40, 50, 60, 70):
#     if age<=30: #no test needed. skip through
#         continue
#         
#     #prileimenary tests are needed
#     do preliminery test
#     
#     if 30<age<=50:#skip through further tests
#         continue
#     
#     do advanced tests
#        
#        
#         
# ```
# 
# * break and continue statements are applicable in both for and while loops.
# 

# <codecell>

for num in (1,2,3,4,5,6,7,8,9,10):
    if num%5:
        print "I am okay with the number ", num
    else:
        print "I hate multiples of 5. I am quitting this loop"
        break

# <markdowncell>

# __Interactive mode, dir, help, type__
# 
# * invoking a python file with a '-i' flag starts in interactive mode
# * e.g.:  python -i test.py
# * It will execute the program in the file test.py and the console will not exit
# * All the variables declared in the file will be available in the console
# 
# ```python
# dir
# ```
# 
# * This is a special method to see all variables and menthods available in the object
# * We will revisit this later
# 
# ```python
# help
# ```
# 
# * Help function shows available help for methods
# * let us try :)
# ```
# help(dir)
# ```
# 
# ```python
# type
# ```
# 
# * type shows, well, the type of the object
# * let us try:
# 
# ```python
# type(1)
# type(2.2)
# type('examples')
# ```

# <markdowncell>

# __Advanced Data Structures:__ 
# tuple
# list
# dictionary
# set
# Frozenset
# 
# * They are container datatypes in the sense it contains primitive datatypes
# * containers can contain multiple datatypes in them
# 
# ```python
# tuple
# 
# x = (1,2,3)
# y = (3.14, 'pi')
# 
# ```
# 
# * tuples cannot be modified later (immutable)
# * len will show the length
# * each element can be addressed by index
# * slice operations are allowed like strings
# 
# ```python
# length = len(x)
# 
# ```
# 

# <markdowncell>

# ```python
# list
# 
# x = [1,2,3]
# y = [3.14, 'pi']
# 
# ```
# 
# * list is like tuple, but mutable
# * supports all operations of tuple
# * possible operations: len, access by index, assign by index, slice, extend, append
# * list and tuples can be typecasted.
# 
# 

# <markdowncell>

# ```python
# dict
# 
# # key value pair
# x = {'name': 'Bob', 'age': 28}
# #access by key instead of index
# x['name']
# #assignments possible
# x['name'] = 'Alice'
# #additional entries can be added
# x['country'] = 'India'
# #elements can be removed
# del(x['age'])
# 
# #additional operations: keys(), values(), items(), update()
# 
# ```

# <markdowncell>

# ```python
# set
# 
# #contains onlyt unique elements
# 
# x = set([1, 2, 3, 2, 5])
# 
# # unordered collection of immutable values.
# # can be created from tuple or lists
# # all mathematical set operations are possible.
# # add, remove, union, subset, intersection, add etc.
# # unlike lists and tuples, sets cannot be accessed by index
# 
# frozenset
# 
# #frozenset is the immutable version of set.
# #operations like add, remove are not allowed.
# 
# ```

# <markdowncell>

# __Sorting__
# 
# ```python
# list.sort()
# sorted(list)
# 
# # try with other datatypes
# ```

