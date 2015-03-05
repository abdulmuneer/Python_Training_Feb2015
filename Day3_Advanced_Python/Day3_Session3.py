# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ###Python packages
# 
# 3rd party libraries are available in pypi
# https://pypi.python.org/pypi
# 
# * ways of installation
# 
#  * pip install package_name (recommended)
#  * easy_install package_name (older method)
#  
#   OR
#  * Download package from https://pypi.python.org/pypi 
# Unzip. python setup.py install
# 

# <markdowncell>

# ###Debugging 
# * Python has a debugger, which is available as a module called pdb
# 
# __Getting started — pdb.set_trace()__
# 
# * Let’s start with a simple program, pdb_eg1.py
# 
# ```python
# '''pdb_eg1.py -- experiment with the Python debugger, pdb'''
# a = "aaa"
# b = "bbb"
# c = "ccc"
# final = a + b + c
# print final
# 
# ```
# 
# * Insert the following statement at the beginning of your Python program. This statement imports the Python debugger module, pdb.
# 
# ```python
# import pdb
# ```
# 
# * Now find a spot where you would like tracing to begin, and insert the following code:
# 
# ```python
# pdb.set_trace()
# ```
# So now your program looks like this.
# ```python
# '''pdb_eg1.py -- experiment with the Python debugger, pdb'''
# import pdb
# a = "aaa"
# pdb.set_trace()
# b = "bbb"
# c = "ccc"
# final = a + b + c
# print final
# ```
# 
# * Now run your program from the command line as you usually do, which will probably look something like this:
# 
# ```shell
# PROMPT> python pdb_eg1.py
# ```
# 
# * When your program encounters the line with pdb.set_trace() it will start tracing. 
# 
# * That is, it will (1) stop, (2) display the “current statement” (that is, the line that will execute next) 
# * ..and (3) wait for your input. You will see the pdb prompt, which looks like this:
# 
# ```python
#     (Pdb)
# ```
# 
# __Execute the next statement… with “n” (next)__
# 
# 
# 
# .
# 
# 
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# 
# __Repeating the last debugging command… with ENTER__
# 
# 
# 
# .
# 
# 
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# __Quitting it all… with “q” (quit)__
# 
# 
# 
# 
# .
# 
# 
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# __Printing the value of variables… with “p” (print)__
# 
# * enter “p” (for “print”) followed by the name of the variable you want to print. 
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# * Note that you can print multiple variables, by separating their names with commas
# 
# ```python
# p a, b, c
# ```
# 
# 
# 
# .
# 
# 
# .
# 
# 
# __Turning off the (Pdb) prompt… with “c” (continue)__
# 
# * The “q” command got you out of pdb in a very crude way — basically, by crashing the program.
# 
# * The “c” (for “continue”) command at the (Pdb) prompt will cause your program to continue running normally, without pausing for debugging. 
# * It may run to completion. 
# * If the pdb.set_trace() statement was inside a loop, you will encounter it again
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# __Seeing where you are… with “l” (list)__
# 
# * “l” shows the general area of your program’s souce code that you are executing. 
# * By default, it lists 11 (eleven) lines of code.
# 
# 
# 
# .
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# 
# __Stepping into subroutines… with “s” (step into)__
# 
# * Sometimes the problem may lie buried in a subroutine.
# 
# ```python
# '''pdb_eg2.py -- experiment with the Python debugger, pdb'''
# import pdb
# 
# def combine(s1,s2):      # define subroutine combine, which...
#     s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
#     s3 = '"' + s3 +'"'   # encloses it in double quotes,...
#     return s3            # and returns it.
# 
# a = "aaa"
# pdb.set_trace()
# b = "bbb"
# c = "ccc"
# final = combine(a,b)
# print final
# ```
# 
# 
# * The statement ```the final = combine(a,b)``` statement — pdb treats it no differently than any other statement. That is, the statement is executed and you move on to the next statement — in this case, to print final.
# 
# * To step into the combine subroutine, and to continue your debugging inside it, use _"s"_
# 
# * For statements that do not involve function calls, “n” and “s” do the same thing
# * But when you execute statements that invoke functions, “s”, unlike “n”
#  * _"s"_ will step into the subroutine.
#  
#  
# .
#  
#  
#  
#  
# .
# 
# 
# 
# 
# __Continuing… but just to the end of the current subroutine… with “r” (return)__
# 
# 
# .
# 
# 
# 
# 
# .
# 
# 
# 
# 
# .
# 
# 
# 
# .
# 
# 
# 
# 
# __You can treat the (Pdb) prompt as a python prompt…__
# 
# * you can even reassign variables that were initialised earlier
#     
# 
# 
# 
# 
# 
# 

# <codecell>

def fib(n):
    if n in (0, 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


# def fib(n):
#     return 1 if n in (0, 1) else fib(n-1) + fib(n-2)

#print fib(30)

def cached_function(func):
    cached = dict()
    def wrapper(n):
        if n in cached:
            return cached[n]
        else:
            value = func(n)
            cached[n] = value
            return value
    return wrapper

@cached_function
def fib1(n):
    return 1 if n in (0, 1) else fib1(n-1) + fib1(n-2)

print fib1(50)
print fib(30)

import sys
print [ x for x in dir(sys) if 'recur' in x]
sys.getrecursionlimit()

