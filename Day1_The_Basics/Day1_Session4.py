# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# 
# * range, xrange
# * sorting
# * Directory - python package
# * Python Standard Library (introduction):
# * os, sys module as examples 

# <markdowncell>

# ```python
# range
# # range(n) gives a list from 0 to n-1
# range(3)
# >>> [0, 1, 2]
# 
# #full form of range:
# range (start, stop, step)
# ```

# <markdowncell>

# xrange()
# 
# * xrange is a generator
# * return the next value on each call
# * this can save memory as it does not populate the entire list like range
# * a list can be generated from generator by passing it to list()

# <markdowncell>

# __Python package__
# 
# * a python package is folder/directory with a file named `__init__.py` in it

# <markdowncell>

# __Standard Library__
# 
# * Python standard library is a collection of modules and packages 
# * Standard library comes with installed python
# * Standard libraries contain tools to do most of the stuff
# * system and network interaction, threading, subprocess, date time calculation, database interaction etc..
# 
# * we will consider two such modules for now

# <markdowncell>

# __sys module__
# 
# * This module provides access to some objects used or maintained by the
#     interpreter and to functions that interact strongly with the interpreter.
#     
# * sys.version will give python version info
# 
# * sys.exit() will cause python to exit abruptly
# 
# * sys.argv contains all the arguments passed while invoking python interpreter.
# 
# 

# <markdowncell>

# __os module__
# 
# * contains libraries for os interaction
# * automatically takes care of the underlying operating system
# 
# * e.g: os.getcwd() prints current working directory
# * os.chdir('path') changes the directory to new location
# * os.name, os.cudir, os.listdir, os.mkdir
# * os.path contains utilities for path manipulation
# * os.path.abspath, os.path.basename, os.path.join, os.path.exists
# * os.path.isfile, os.path.isdir

# <markdowncell>

# __Exercise__
# 
# * print all files in home directory that starts with letter 'a' or 'B'

# <codecell>


