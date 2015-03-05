# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ###Decorators
# * Decorators dynamically alter the functionality of a function
# * They can also alter a method or class without having to directly use subclasses.
# * This is ideal when you need to extend the functionality of functions that you don't want to modify.
# 
# * Essentially, decorators work as wrappers
#   * modifying the behavior of the code before and after a target function execution
#   * without the need to modify the function itself, augmenting the original functionality
#   * Hence the name `decorator`.

# <markdowncell>

#  In Python, functions are first class citizens, they are objects and that means we can do a lot of useful stuff with them.
#  
# __ Assign functions to variables__

# <codecell>

def greet(name):
    return "Hi ", name

say_hi = greet
print say_hi("Alice")
numbers = range
print numbers(10)

# <markdowncell>

# __Define functions inside other functions__

# <codecell>

def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print greet("John")

# Outputs: Hello John

# <markdowncell>

# __Functions can be passed as parameters to other functions__

# <codecell>

def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "John"
    return func(other_name)  

print call_func(greet)

# Outputs: Hello John

# <markdowncell>

# __Functions can return other functions__
# 
# In other words, functions *generating* other functions.

# <codecell>

def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()

# Outputs: Hello there!

# <markdowncell>

# __Inner functions have access to the enclosing scope__
# 
# * More commonly known as a closure. 
# * A very powerful pattern that we will come across while building decorators. 
# 
# Another thing to note, Python only allows read access to the outer scope and not assignment.
# 
# 
# Notice how we modify the example above to read a "name" argument from the enclosing scope of the inner function and return the new function.
# 
# ```python
# def compose_greet_func(name):
#     def get_message():
#         return "Hello there "+name+"!"
# 
#     return get_message
# 
# greet = compose_greet_func("John")
# print greet()
# 
# # Outputs: Hello there John!
# ```

# <codecell>

def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("John")
print greet()

# <markdowncell>

# __Composition of Decorators__
# 
# * Function decorators are simply wrappers to existing functions. 

# <codecell>

#Putting the ideas mentioned above together, we can build a decorator. 
#In this example let's consider a function 
#   ..that wraps the string output of another function by p tags.

def get_text(name):
   return "Hello, {0} ".format(name)










def p_decorate(func):
   def func_wrapper(name):
       return "<p>" + func(name) + "</p>"
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("John")

# <p>Hello, John</p>

# <markdowncell>

# __That was our first decorator!!__
# 
# * A function that takes another function as an argument
# * generates a new function, augmenting the work of the original function
# * .. and returning the generated function so we can use it anywhere.

# <markdowncell>

# *To have get_text itself be decorated by p_decorate, we just have to assign get_text to the result of p_decorate!!!*

# <codecell>

get_text = p_decorate(get_text)

print get_text("John")

# <markdowncell>

# #Python's Decorator Syntax

# <markdowncell>

# Python makes creating and using decorators a bit cleaner and nicer for the programmer through some syntactic sugar.
# 
# * To decorate get_text we don't have to 
# ```python
# get_text = p_decorator(get_text)
# ```
# 
# * There is a neat shortcut for that..

# <codecell>

def p_decorate(func):
   def func_wrapper(name):
       return "<p>" +func(name) + "</p>"
   return func_wrapper

@p_decorate
def get_text(name):
   return "Hello " + name

print get_text("John")

# <markdowncell>

# ##Now let's do it again!!
# ### decorate our get_text function by 2 other functions to wrap a div and strong tag 

# <codecell>


def p_decorate(func):
   def func_wrapper(name):
       return "<p>"+func(name)+"</p>"
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>"+func(name)+"</strong>"
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>"+func(name)+"</div>"
    return func_wrapper

# <markdowncell>

# ```python
# get_text = div_decorate(p_decorate(strong_decorate(get_text)))
# ```

# <codecell>

@div_decorate
#@p_decorate
@strong_decorate
def get_text(name):
   return "Hello, {0}".format(name)

print get_text("John")

# <markdowncell>

# ###Decorating Methods
# * methods expect their first parameter to be a reference to the current object. 
# * We can build decorators while taking self into consideration in the wrapper function.

# <codecell>

def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
#print my_person.get_fullname()

# <markdowncell>

# __Let usmake our decorator useful for functions and methods alike..__
# 
# * Let us give *args and **kwargs as parameters for the wrapper

# <codecell>

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print my_person.get_fullname()

# <markdowncell>

# # Passing arguments to decorators
# 
# * 3 decorators(div_decorate, p_decorate, strong_decorate) 
# * each with the same functionality but wrapping the string with different tags.
# * Let us have a general implementation for one that takes the tag to wrap with as a string..

# <codecell>

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("strong")
@tags("p")
def get_text(name):
    return "Hello "+name

print get_text("John")

# Outputs <p>Hello John</p>

# <markdowncell>

# ####Debugging decorated functions
# 
# * At the end of the day decorators are just wrapping our functions..
# * in case of debugging that can be problematic: 
#   * the wrapper function does not carry the name, module and docstring of the original function. * Based on the example above if we do:
# 
# ```python
# print get_text.__name__
# # Outputs func_wrapper
# ```
# 
# * The output was expected to be `get_text` 
# * But the attributes __name__, __doc__, and __module__ of get_text got overridden
# * We can re-set them within func_wrapper manually
# * but Python provides a much nicer way.
# 
# ####Functools to the rescue
# 
# * Python includes the ```functools``` module which contains ```functools.wraps```. 
# * Wraps is a decorator for updating the attributes of the wrapping function(func_wrapper) to those of the original function(get_text). 
# * This is as simple as decorating func_wrapper by @wraps(func). 

# <codecell>


from functools import wraps

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """returns some text"""
    return "Hello "+name

print get_text.__name__ # get_text
print get_text.__doc__ # returns some text
print get_text.__module__ # __main__

