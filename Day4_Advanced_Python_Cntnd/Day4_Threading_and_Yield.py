# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Threading
# 
# * The threading module builds on the low-level features of thread to make working with threads even easier and more pythonic. 
# * Using threads allows a program to run multiple operations concurrently in the same process space.

# <markdowncell>

# ####Thread Objects
# 

# <codecell>

import threading

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# <codecell>

help(threading.Thread)

# <markdowncell>

# ####Determining the Current Thread
# 
# * Using arguments to identify or name the thread is cumbersome, and unnecessary. 
# * Each Thread instance has a name with a default value that can be changed as the thread is created. 
# * Naming threads is useful in server processes with multiple service threads handling different operations.
# 

# <codecell>


import threading
import time

def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(2)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(3)
    print threading.currentThread().getName(), 'Exiting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# <markdowncell>

# * Most programs do not use print to debug.
# * The __logging__ module supports embedding the thread name in every log message using the formatter code %(threadName)s. 
# * Including thread names in log messages makes it easier to trace those messages back to their source.

# <codecell>

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

# <markdowncell>

# * __logging__ is also thread-safe, so messages from different threads are kept distinct in the output.

# <markdowncell>

# ### Subclassing Thread
# 
# * At start-up, a Thread does some basic initialization and then calls its __run()__ method, which calls the target function passed to the constructor. 
# * To create a subclass of Thread, override __run()__ to do whatever is necessary
# 

# <codecell>

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):

    def run(self):
        logging.debug('running')
        return

for i in range(5):
    t = MyThread()
    t.start()
    

# <codecell>

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThreadWithArgs(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a':'A', 'b':'B'})
    t.start()

# <markdowncell>

# ##Yield

# <codecell>

def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append()

    return result_list

# or better yet...

def get_primes(input_list):
    return (element for element in input_list if is_prime(element))

# not germane to the example, but here's a possible implementation of
# is_prime...

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


# <codecell>

def string_generator():
    x = ['a', 'b', 'c']
    for i in x:
        yield(i)
        
        
strings = string_generator()
print strings

# <codecell>

print strings.next()

# <codecell>

for i in xrange(10):
    print i, 

# <codecell>

def string_generator():
    x = ['a', 'b', 'c']
    for i in x:
        yield(i)
    return "Done.. "
strings = string_generator()

for i in strings:
    print i, 

# <codecell>

def cat_function():
    x = 1
    y = 1
    while x:
        y = yield('1'*y)
        
#         if x == 'q':
#             break

cat = cat_function()

# print cat.next() 

# <codecell>

cat.next()

# <codecell>

cat.send(10)

# <codecell>

cat.send(5)

# <codecell>


def appender(num):
    li1 = []
    for i in xrange(num):
        li1.append(i)
    print "Appended"
    
def inserter(num):
    li1 = []
    for i in xrange(num):
        li1.insert(0, i)
    print "Inserted"    

# <codecell>

appender(100000)

# <codecell>

inserter(100000)

