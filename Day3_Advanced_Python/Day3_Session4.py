# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ###Testing Your Code
# 
# ####Testing your code is very important.
# 
# 
# * Some general rules of testing:
# 
#  * A testing unit should focus on one tiny bit of functionality and prove it correct.
#  * Each test unit must be fully independent. 
#  * Each of them must be able to run alone, and also within the test suite, regardless of the order they are called.
#  * The implication of this rule is that each test must be loaded with a fresh dataset and may have to do some cleanup afterwards. 
#  * This is usually handled by setUp() and tearDown() methods.

# <markdowncell>

# ##Unittest
#  
#  * Python standard library provides a library called unittest.
#  
#  Consider example:
#  `unittest_example1.py`
#  
#  
# ```python
# import unittest
# from calculator import multiply
# 
# class TestUM(unittest.TestCase):
# 
#     def setUp(self):
#         pass
# 
#     def test_numbers_3_4(self):
#         self.assertEqual( multiply(3,4), 12)
# 
#     def test_strings_a_3(self):
#         self.assertEqual( multiply('a',3), 'aaa')
# 
# if __name__ == '__main__':
#     unittest.main()
# ```
# 
# -------------------------
# 
# ```python
# #calculator.py
# def multiply(a, b):
#     return a * b
# 
# 
# ```
# 
# Method 	Checks
# 
# -------------------------------------
# 
# * assertEqual(a, b) 	 	------------>  a == b 	 
# * assertNotEqual(a, b) ------------> a != b 	 
# * assertTrue(x) 	------------>  bool(x) is True 	 
# * assertFalse(x) 	------------>  bool(x) is False 	 
# * assertIs(a, b) 	------------>  a is b 	2.7
# * assertIsNot(a, b) 	------------>  a is not b 
# * assertIsNone(x) 	------------>  x is None
# * assertIsNotNone(x) 	------------>  x is not None
# * assertIn(a, b) 	------------>  a in b 
# * assertNotIn(a, b) 	------------>  a not in b 
# * assertIsInstance(a, b) 	------------>  isinstance(a, b)
# * assertNotIsInstance(a, b) 	------------>  not isinstance(a, b)

# <markdowncell>

# 
# * executing the test will show up results like:
# 
# ```python
# 
# > python unittest_example1.py
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# 
# OK
# > python test_um_unittest.py -v
# test_numbers_3_4 (__main__.TestUM) ... ok
# test_strings_a_3 (__main__.TestUM) ... ok
# 
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# 
# OK
# 
# ```

# <markdowncell>

# ###Doctest
# 
# * e.g.
# 
# ```python
# #doctest_example1.py
# def square(x):
#     """Squares x.
# 
#     >>> square(2)
#     4
#     >>> square(-2)
#     4
#     """
# 
#     return x * x
# 
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#     #or python -m doctest <file>
# ```

# <markdowncell>

# ###Other tools
# 
# 
# ####py.test
# 
# * py.test is a no-boilerplate alternative to Python’s standard unittest module.
# 
# `$ pip install pytest`
# 
# * Despite being a fully-featured and extensible test tool, it boasts a simple syntax. Creating a test suite is as easy as writing a module with a couple of functions:
# 
# ```python
# # content of test_sample.py
# def func(x):
#     return x + 1
# 
# def test_answer():
#     assert func(3) == 5
# ```
# 
# and then running the py.test command
# 
# ```python
# 
# $ py.test
# =========================== test session starts ============================
# platform darwin -- Python 2.7.1 -- pytest-2.2.1
# collecting ... collected 1 items
# 
# test_sample.py F
# 
# ================================= FAILURES =================================
# _______________________________ test_answer ________________________________
# 
#     def test_answer():
# >       assert func(3) == 5
# E       assert 4 == 5
# E        +  where 4 = func(3)
# 
# test_sample.py:5: AssertionError
# ========================= 1 failed in 0.02 seconds =========================
# ```
# 
# 
# 
# ###Nose
# 
# * nose extends unittest to make testing easier.
# 
# `$ pip install nose`
# 
# nose provides automatic test discovery to save you the hassle of manually creating test suites. It also provides numerous plugins for features such as xUnit-compatible test output, coverage reporting, and test selection.
# 
# 
# 
# ###tox
# 
# * tox is a tool for automating test environment management and testing against multiple interpreter configurations
# 
# `$ pip install tox`
# 
# tox allows you to configure complicated multi-parameter test matrices via a simple ini-style configuration file.
# 
# ###Unittest2
# 
# * unittest2 is a backport of Python 2.7’s unittest module which has an improved API and better assertions over the one available in previous versions of Python.
# 
# * If you’re using Python 2.6 or below, you can install it with pip
# 
# `$ pip install unittest2`
# 
# * You may want to import the module under the name unittest to make porting code to newer versions of the module easier in the future
# 
# ```python
# import unittest2 as unittest
# 
# class MyTest(unittest.TestCase):
#     ...
# ```
# 
# * This way if you ever switch to a newer Python version and no longer need the unittest2 module, you can simply change the import in your test module without the need to change any other code.
# 
# 
# ###mock
# 
# * unittest.mock is a library for testing in Python. As of Python 3.3, it is available in the standard library.
# 
# For older versions of Python:
# 
# `$ pip install mock`
# 
# * It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
# 
#  * For example, you can monkey-patch a method:
# 
# ```python
# 
# from mock import MagicMock
# thing = ProductionClass()
# thing.method = MagicMock(return_value=3)
# thing.method(3, 4, 5, key='value')
# 
# thing.method.assert_called_with(3, 4, 5, key='value')\
# ```
# 
# 
# * To mock classes or objects in a module under test, use the patch decorator. 
# * In the example below, an external search system is replaced with a mock that always returns the same result (but only for the duration of the test).
# 
# ```python
# 
# def mock_search(self):
#     class MockSearchQuerySet(SearchQuerySet):
#         def __iter__(self):
#             return iter(["foo", "bar", "baz"])
#     return MockSearchQuerySet()
# 
# # SearchForm here refers to the imported class reference in myapp,
# # not where the SearchForm class itself is imported from
# @mock.patch('myapp.SearchForm.search', mock_search)
# def test_new_watchlist_activities(self):
#     # get_search_results runs a search and iterates over the result
#     self.assertEqual(len(myapp.get_search_results(q="fish")), 3)
# ```
# 
# Mock has many other ways you can configure it and control its behavior.

# <markdowncell>

# ##Regular Expressions
# 
# * Regular expressions are text matching patterns described with a formal syntax. 
# * The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original.
# 
# ###Finding Patterns in Text

# <codecell>

import re

patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text),

    if re.search(pattern,  text):
        print 'found a match!'
    else:
        print 'no match'

# <markdowncell>

# * __search()__ takes the __pattern__ and text to scan, and returns a __Match__ object when the pattern is found. If the pattern is not found, __search()__ returns __None__.
# 
# * The __Match__ object returned by __search()__ holds information about the nature of the match including
#  * the original input string
#  * the regular expression used
#  * the location within the original string where the pattern occurs.
#  
#  

# <codecell>

import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print 'Found "%s" in "%s" from %d to %d ("%s")' %(
        match.re.pattern, match.string, s, e, text[s:e])

# <markdowncell>

# ###Compiling Expressions
# 
# * The __compile()__ function converts an expression string into a RegexObject.

# <codecell>

import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this','that',] ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),

    if regex.search(text):
        print 'found a match!'
    else:
        print 'no match'


# <markdowncell>

# ###Multiple Matches
# 
# * __search()__ looks for single instances of literal text strings. 
# * The findall() function returns all of the substrings of the input that match the pattern without overlapping.

# <codecell>

import re

text = 'abbaaabbbbaaaaab'

pattern = 'ab'

for match in re.findall(pattern, text):
    print 'Found "%s"' % match

# <markdowncell>

# * __finditer()__ returns an iterator that produces Match instances instead of the strings returned by __findall()__.

# <codecell>

import re

text = 'abbaaabbbbaaaaab'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e], s, e)

# <markdowncell>

# ###Pattern Syntax
# * Regular expressions support more powerful patterns than simple literal text strings. 
# * Patterns can:
#  * repeat
#  * be anchored to different logical locations within the input
#  * be expressed in compact forms that don’t require every literal character be present in the pattern. 
# * All of these features are used by combining literal text values with metacharacters that are part of the regular expression pattern syntax implemented by `re`

# <codecell>

import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Show the character positions and input text
    print
    print ''.join(str(i/10 or ' ') for i in range(len(text)))
    print ''.join(str(i%10) for i in range(len(text)))
    print text

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e])
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa', ['ab'])

# <markdowncell>

# ####Repetition

# <codecell>

test_patterns('abbaaabbbbaaaaa',
              [ 'ab*',     # a followed by zero or more b
                'ab+',     # a followed by one or more b
                'ab?',     # a followed by zero or one b
                'ab{3}',   # a followed by three b
                'ab{2,3}', # a followed by two to three b
                ])

# <markdowncell>

# * The normal processing for a repetition instruction is to consume as much of the input as possible while matching the pattern. 
# * This so-called greedy behavior may result in:
#  * fewer individual matches, or 
#  * the matches may include more of the input text than intended. 
# * Greediness can be turned off by following the repetition instruction with __?__.

# <codecell>

test_patterns('abbaaabbbbaaaaa',
              [ 'ab*?',     # a followed by zero or more b
                'ab+?',     # a followed by one or more b
                'ab??',     # a followed by zero or one b
                'ab{3}?',   # a followed by three b
                'ab{2,3}?', # a followed by two to three b
                ])

# <markdowncell>

# ####Character Sets
# * A character set is a group of characters, any one of which can match at that point in the pattern. 
# * For example, [ab] would match either a or b.

# <codecell>

#from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ '[ab]',    # either a or b
                'a[ab]+',  # a followed by one or more a or b
                'a[ab]+?', # a followed by one or more a or b, not greedy
                ])

# <markdowncell>

# * A character set can also be used to exclude specific characters. 
# * The special marker ^ means to look for characters not in the set following.

# <codecell>

test_patterns('This is some text -- with punctuation.',
              [ '[^-. ]+',  # sequences without -, ., or space
                ])

# <markdowncell>

# As character sets grow larger, typing every character that should (or should not) match becomes tedious. A more compact format using character ranges lets you define a character set to include all of the contiguous characters between a start and stop point.

# <codecell>

test_patterns('This is some text -- with punctuation.',
              [ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one upper case letter followed by lower case letters
                ])

# <markdowncell>

# * The metacharacter __dot__, or __period__ (__.__), indicates that the pattern should match any single character in that position.

# <codecell>

test_patterns('abbaaabbbbaaaaa',
              [ 'a.',   # a followed by any one character
                'b.',   # b followed by any one character
                'a.*b', # a followed by anything, ending in b
                'a.*?b', # a followed by anything, ending in b
                ])

# <markdowncell>

# ###Escape Codes
# 
# An even more compact representation uses escape codes for several pre-defined character sets. The escape codes recognized by re are:
# 
# * __Code  ->	Meaning__
# * \d 	a digit
# * \D 	a non-digit
# * \s 	whitespace (tab, space, newline, etc.)
# * \S 	non-whitespace 
# 
# * \w   alphanumeric 
# * \W 	 non-alphanumeric 
# 
# Prefer raw strings to maintain readability (double backslash problem)

# <codecell>

test_patterns('This is a prime #1 example!',
              [ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ])

# <markdowncell>

# ###Anchoring
# Anchoring
# 
# In addition to describing the content of a pattern to match, you can also specify the relative location in the input text where the pattern should appear using anchoring instructions.
# 
# Code 	Meaning
# 
# * ^ 	start of string, or line
# * $ 	end of string, or line
# * \A 	start of string
# * \Z 	end of string
# * \b 	empty string at the beginning or end of a word
# * \B 	empty string not at the beginning or end of a word
# 

# <codecell>

test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word
                ])

# <markdowncell>

# ###Dissecting Matches with Groups
# 
# * Adding groups to a pattern lets you isolate parts of the matching text, expanding those capabilities to create a parser. 
# * Groups are defined by enclosing patterns in parentheses ('__(__' and '__)__').

# <codecell>

test_patterns('abbaaabbbbaaaaa',
              [ 'a(ab)',    # 'a' followed by literal 'ab'
                'a(a*b*)',  # 'a' followed by 0-n 'a' and 0-n 'b'
                'a(ab)*',   # 'a' followed by 0-n 'ab'
                'a(ab)+',   # 'a' followed by 1-n 'ab'
                ])

# <markdowncell>

# To access the substrings matched by the individual groups within a pattern, use the groups() method of the Match object.

# <codecell>

import re

text = 'This is some text -- with punctuation.'

print text
print

for pattern in [ r'^(\w+)',           # word at start of string
                 r'(\w+)\S*$',        # word at end of string, with optional punctuation
                 r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
                 r'(\w+t)\b',         # word ending with 't'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print

# <markdowncell>

# ###Search Options
# * You can change the way the matching engine processes an expression using option flags. 
# * The flags can be combined using a bitwise or operation, and passed to __compile()__, __search()__, __match()__, and other functions that accept a pattern for searching.
# ####Case-insensitive Matching
# * __IGNORECASE__ causes literal characters and character ranges in the pattern to match both upper and lower case characters.

# <codecell>

import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print 'Text            :', text
print 'Pattern         :', pattern
print 'Case-sensitive  :', with_case.findall(text)
print 'Case-insensitive:', without_case.findall(text)

# <markdowncell>

# Since the pattern includes the literal T, without setting IGNORECASE the only match is the word This. When case is ignored, text also matches.

# <markdowncell>

# ####Input with Multiple Lines
# * There are two flags that effect how searching in multi-line input works. 
# * The MULTILINE flag controls how the pattern matching code processes anchoring instructions for text containing newline characters. 
# * When multiline mode is turned on, the anchor rules for ^ and $ apply at the beginning and end of each line, in addition to the entire string.
# 
# * DOTALL is the other flag related to multiline text. Normally the dot character __.__ matches everything in the input text except a newline character. The flag allows dot to match newlines as well.

# <codecell>

import re

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'(^\w+)|(\w+\S*$)'
single_line = re.compile(pattern)
multiline = re.compile(pattern, re.MULTILINE)

print 'Text        :', repr(text)
print 'Pattern     :', pattern
print 'Single Line :', single_line.findall(text)
print 'Multline    :', multiline.findall(text)

# <codecell>

import re

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print 'Text        :', repr(text)
print 'Pattern     :', pattern
print 'No newlines :', no_newlines.findall(text)
print 'Dotall      :', dotall.findall(text)

# <markdowncell>

# ####Verbose Expression Syntax

# <codecell>

import re

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)', re.UNICODE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Matches'
    else:
        print '  No match'
    

# <codecell>

import re

address = re.compile(
    '''
    [\w\d.+-]+       # username
    @
    ([\w\d.]+\.)+    # domain name prefix
    (com|org|edu)    # we should support more top-level domains
    ''',
    re.UNICODE | re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = address.search(candidate)
    if match:
        print '  Matches'
    else:
        print '  No match'
    

# <markdowncell>

# ###Splitting with Patterns

# <codecell>

import re

text = 'Paragraph one\non two lines.\n\nParagraph two.\n\n\nParagraph three.'

print 'With findall:'
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)', text, flags=re.DOTALL)):
    print num, repr(para)
    print

print
print 'With split:'
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print num, repr(para)
    print

