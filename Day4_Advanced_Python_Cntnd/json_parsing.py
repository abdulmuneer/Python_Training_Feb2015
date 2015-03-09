# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
x = {1: 10, 2: range(10)}
y = json.dumps(x)
print y

z = json.loads(y)
print z
print type(z)
print type(z[u'1'])

# <codecell>

import csv
import glob
for files in glob.glob('/home/amuneer/Documents/TruepayDocs/temp/POS/*.csv'):
    with open(files) as f:
        print "checking file: ",files
        #print dir(csv)
        d = csv.DictReader(f)
        lines = 0
        for rows in d:
            lines += 1
            items = (rows['posTrxId'].strip(), rows['ReportedById'].strip(), rows['transactionDate'].strip())
            if not all(items):
                print lines, items
        else:
            print 'check complete'
        

# <codecell>

help(minidom)

# <codecell>

from xml.dom import minidom
help(minidom)

# <codecell>


# def test():
#     print "hello"
    
# x = "hello!!"
# print Ex.__doc__
# print str(Ex)

class Ex(object):
    '''test documentation for Ex'''
    def repr__(self):
        return "this is Ex object to show class behaviour"
    pass

ex = Ex()
print ex
print repr(ex)


for i in dir(Ex):
    print i, ',\t', 

# <codecell>

from collections import defaultdict

x = defaultdict(int)

x[1] = 2
print x

print x[10]



