# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

x = open('testing_file_opening.txt', 'w')
x.write("This is the first line")
x.write("\n")
x.write("second line")
x.close()

# <codecell>

y = open('testing_file_opening.txt', 'r')
lines = y.readlines()
print lines

# <codecell>

y = open('testing_file_opening.txt', 'r')
text = y.read()
print text

# <codecell>

dir(y)

# <codecell>

for lines in open('testing_file_opening.txt', 'r'):
    print lines

# <codecell>

def find_sum():
    x = open('numbers.txt', 'r')
    for line in x:
        total = 0
        numbers_as_strings = line.strip().split()
        for each_num_string in numbers_as_strings:
            total = total + int(each_num_string)
        print total

find_sum()

# <rawcell>

# # without context manager
# 
# try:
#     open(file)
#     do something
# except:
#     handle exception
# finally:
#     close file

# <codecell>

# with context manager
with open('numbers.txt', 'r') as my_file:
    #do something
    for lines in my_file:
        print lines
my_file.readlines()

# <codecell>

#OS, sys

import os

print os.name
os.system('lss')
dir(os)

# <codecell>

x = os.getcwd()
print os.getcwd()
os.chdir('/home/amuneer')
print os.getcwd()
os.chdir("/home/amuneer/workspace/notebook/Training_Feb2015/Day2_Core_Python_Concept")
print os.getcwd()
os.mkdir("TEST_DIR")

# <codecell>

for x, y, z in os.walk('.'):
    print x
    print "+++++++++++++++++++++++++++++++++"
    print y
    print "+++++++++++++++++++++++++++++++++"
    print z
    print "+++++++++++++++++++++++++++++++++"

# <codecell>

help(os.walk)

# <codecell>

x = os.getcwd()
print x

# <codecell>

print os.path.abspath("/home/amuneer/workspace/notebook/Training_Feb2015/Day2_Core_Python_Concept/numbers.txt")

# <codecell>

x = "/home/amuneer/workspace/notebook/Training_Feb2015/Day2_Core_Python_Concept/numbers.txt"

print os.path.basename(x)

print os.path.split(x)
help(os.path.split)

# <codecell>

path_list = x.split('/')
print path_list

# <codecell>

l = os.path.join('', 'home', 'amuneer', 'workspace', 'notebook', 'Training_Feb2015', 'Day2_Core_Python_Concept', 'numbers.txt')
print l

# <codecell>

print os.path.isdir('numbers.txt')
print os.path.exists('invalid')
print os.listdir('.')

