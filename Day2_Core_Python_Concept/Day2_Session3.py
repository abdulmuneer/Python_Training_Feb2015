# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Modules

# <markdowncell>

# ```python
# >>> #import module
# ... 
# >>> #from module import class
# ... 
# >>> #from package import module
# ... 
# >>> #from package import module1, module2
# ... 
# >>> #from module import class1, class2
# ... 
# >>> #from package import *
# ... 
# >>> #from module import *
# ```

# <codecell>

1/0

# <codecell>

x = (1,2,3)
x.upper()

# <codecell>

print xyz

# <codecell>

try:
    print xyz
    y = 1/0
    x = (1,2,3)
    x.upper()
    
except ZeroDivisionError:
    print "please don't divide by 0"
except AttributeError:
    print "no such attribute"
except NameError:
    print "No such name.."

#import traceback

# try:
#     1/0
# except :
#     print tarceback.formate_exec(3)



class custom_error(Exception):
    pass

try:
    1/0
except:
    raise NameError
else:
    pass
finally:
    pass

