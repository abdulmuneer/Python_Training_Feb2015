'''pdb_eg1.py -- experiment with the Python debugger, pdb'''

import pdb

a1 = "aaa"
pdb.set_trace()
b1 = "bbb"
c1 = "ccc"
final = a1 + b1 + c1
print final
