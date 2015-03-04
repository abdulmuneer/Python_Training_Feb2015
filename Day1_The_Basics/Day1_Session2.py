# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Basic Data Structures : 
# * int, float, str
# * Possible operations on above datatypes
# * Variables
# * Dynamic typing

# <codecell>

x = 10

y = 10.1

# <markdowncell>

# __Numbers__:
# 
# * int 
# 
# ```python
# x = 10
# y = -1
# z = 1000
# ```
# * float
# 
# ```python
# x = 10.1
# y = -1.1
# z = 3.14
# ```
# * complex
# 
# ```python
# x = 10 + 2j
# y = -1j
# ```

# <markdowncell>

# __Boolean and None__
# 
# ```python
# True
# False
# None
# ```

# <markdowncell>

# Arithmetic Operations:
# * Assignment: =
# * Addition: +
# * Subtraction: -
# * Division: /
# * Multiplication: *
# 
# * Power: `**`
# * Modulo: %
# * Floor division: //
# 
# * precedence `*, /, %, //` takes precedence over `+, -`
# 
# ```python
# 2+3*2-5 = 3
# ```
# * reference: https://docs.python.org/2/reference/expressions.html#operator-precedence
# * We can force precedence by enclosing them in parantheses. 
# 
# ```python
# (2+3)*2-5 = 5
# ```

# <markdowncell>

# __Strings__
# 
# ```python
# p = 'a'
# q = "b"
# x = 'this is a single quoted String'
# y = "this is a double quoted String"
# z = """This is a triple 
# quoted string"""
# note = '''Triple quoted strings can contain multi line strings'''
# ```

# <markdowncell>

# __String Operations__:
# 
# * Once a string is created, it cannot be modified (immutability).
# * Any operation that modifies a string will in fact create a new string
# 
# ___operations___:
# 
# * addition
# * slicing
# * replacing
# * comparison
# * substring check
# * find
# * split
# * join
# * upper/lower

# <markdowncell>

# __Type Conversion__
# 
# * converting string to a number
# * converting number to a string
# * converting between numbers
# * implicit conversion

