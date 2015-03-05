# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# __ List Comprehensions, Dictionary Comprehensions__
# 
#  - syntax of LC
#  - examples
#  - Syntax of DC, SC
#  - Examples,
#  - compatibility of python versions

# <codecell>

x = range(10)
print x
new_list = []
for element in x:
    new_list.append(element*element)
print new_list

squares = [element*element for element in x]
print "squares: ", squares

multiples_3 = [element for element in x if element%3==0]
print "multiples_3, ", multiples_3

# <codecell>

x = [(1, 1000),(2, 2000), (3, 3000)]

y = {key:value for key, value in x if key%3==0}
print y
print dict(x)

#SC
x = range(10) + range(5)
print x

s = {element for element in x}
print s

# <markdowncell>

# __Functional Programming Concepts: __
# 
# (The following is adapted from material by David Mertz in IBM developerworks library)
#  - Functions are first class (objects). That is, everything you can do with "data" can be done with functions themselves (such as passing a function to another function). 
#  - Recursion is used as a primary control structure. 
#  - With Python 2.0, a very nice bit of "syntactic sugar" was added with list comprehensions.
#  - While list comprehensions add no new capability, they make a lot of the old capabilities look a lot nicer. 
#  - The basic elements of FP in Python are the functions map(), reduce(), and filter(), and the operator lambda.
#  - These very few functions (and the basic operators) are almost sufficient to write any Python program.
#  - specifically, the flow control statements (if, elif, else, assert, try, except, finally, for, break, continue, while, def) can all be handled in a functional style using exclusively the FP functions and operators.

# <markdowncell>

# __ Eliminating flow control statements__
# 
# - key point: "Python "short circuits" evaluation of Boolean expressions."
# - This provides an expression version of if/ elif/ else blocks (assuming each block calls one function, which is always possible to arrange):
# 
# ```python
# # Normal statement-based flow control
# if <cond1>:   func1()
# elif <cond2>: func2()
# else:         func3()
# 
# # Equivalent "short circuit" expression
# (<cond1> and func1()) or (<cond2> and func2()) or (func3())
# 
# # Example "short circuit" expression
# >>> x = 3
# >>> def pr(s): return s
# >>> (x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))
# 'other'
# >>> x = 2
# >>> (x==1 and pr('one')) or (x==2 and pr('two')) or (pr('other'))
# 'two'
# ```

# <markdowncell>

# __ Lambda with short-circuiting in Python__
# 
# ```python
# >>> pr = lambda s:s
# >>> namenum = lambda x: (x==1 and pr("one")) \
# ....                  or (x==2 and pr("two")) \
# ....                  or (pr("other"))
# >>> namenum(1)
# 'one'
# >>> namenum(2)
# 'two'
# >>> namenum(3)
# 'other'
# ```

# <markdowncell>

# __Functions as first class objects__
# 
# We were able to bind our objects to the names "pr" and "namenum", in exactly the same way we might have bound the number 23 or the string "spam" to those names. 
# 
# The main thing we do with our first class objects, is pass them to our FP built-in functions map(), reduce(), and filter(). Each of these functions accepts a function object as its first argument. 

# <markdowncell>

# __Map__
# 
# map() performs the passed function on each corresponding item in the specified list(s), and returns a list of results. 
# 
# 
# __Reduce__
# 
# reduce() performs the passed function on each subsequent item and an internal accumulator of a final result; for example, reduce(lambda n,m:n*m, range(1,10)) means "factorial of 10" (in other words, multiply each item by the product of previous multiplications). 
# 
# __Filter__
# 
# filter() uses the passed function to "evaluate" each item in a list, and return a winnowed list of the items that pass the function test. 

# <markdowncell>

# __Functional looping in Python__
# 
# Replacing loops is as simple as was replacing conditional blocks. `for` can be directly translated to `map()`. 
# ```python
# for e in lst:
#     func(e)      # statement-based loop
# map(func,lst)           # map()-based loop
# ```

# <codecell>

def fun_square(x):
    return x*x

lst = range(4, 20, 3)
print lst

#mapped_list = map(fun_square, lst)
#print mapped_list

def divisible_by_4(x):
    return not x%4

filtered_list = filter(divisible_by_4, lst)

#print filtered_list

def adder(x, y):
    return x+y

total = reduce(adder, lst)
print total

def mul(x, y):
    return x*y

factorial = reduce(mul, range(1,10))
print factorial



# <codecell>

# uses of lambda
x = range(15, 20)
y = [str(a*a)[1:] for a in x]
print x
print y

z = zip(x, y)
print z

z.sort(key=lambda x: x[1])
print z



# <codecell>

x = range(100)
y = [a*a*a for a in x ]
z = (a*a*a for a in x )
print z
for a in z:
    print a, 

