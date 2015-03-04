# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Functions

# <codecell>

#Function declaration

# <codecell>

def adder(x, y):
    '''
    This is a function to add two numbers
    '''
    return x+y

# <codecell>

#calling a function 
adder(2,3)
help(adder)

# <codecell>

def adder(x, y, *arg ):
    print x, y, arg

# <codecell>

adder(1,2)

# <codecell>

adder(1, 2, 3)

# <codecell>

adder(1, 2, 3, 4, 5)

# <codecell>

def adder(*args, x, y):

# <codecell>

#pass by reference

# <codecell>

x = range(5)

def modify(y):
    y[0] = 1000
    x = ['abc']
    print "x", x

print x
modify(x)
print x
print y

# <codecell>

#Default arguments

# <codecell>

def adder(x=10, y=20):
    return(x+y)

print adder(1,3)
print adder()
print adder(1)

print adder(y=1)

#def get_student_info(name, age, class_, height=None):
    

# <codecell>

def divide(x=1, y=1):
    return x/y

divide(y=10, x=100)

# <codecell>

def get_student_info(name=None, age=None, **kwargs):
    print name, age, kwargs

# <codecell>

get_student_info('Bob', 20)
get_student_info('Alice', 25, country='India', state='KA')

# <codecell>

dict1 = {'name':'Alice', 'age':20}
print dict1
dict2 = dict(name='Alice', age=20)
print dict2

# <markdowncell>

# __Python scoping w.r.t. functions__
# 
# * scope is categorized as global and local
# 
#     

# <codecell>

name = 'Alice'

def student1():
    print 'within the function, name is: ', name
    
print "outside the function, name is: ", name 
student1()
print "outside the function, name now is: ", name

# <codecell>

def student2():
    name = 'bob'
    print 'within the function, name is: ', name
    
student2()
print "outside the function, name now is: ", name
    

# <codecell>

def student2():
    global name
    name = 'bob'
    print 'within the function, name is: ', name
    
student2()
print "outside the function, name now is: ", name

