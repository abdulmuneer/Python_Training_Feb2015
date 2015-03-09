# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Parsing
# 1. ConfigParser
# 2. HTML Parser
# 3. XML Parser
# 4. JSON

# <markdowncell>

# ###Config Parser
# 
# * A sample configuration file with section “bug_tracker” and three options would look like:
# ```
# [bug_tracker]
# url = http://localhost:8080/bugs/
# username = dhellmann
# password = SECRET
# ```
# 
# * e.g.: Backup all MySQL databases, one in each file with a timestamp on the end.
# 
# ```python
# #Importing the modules
# import os
# import ConfigParser
# import time
# 
# # On Debian, /etc/mysql/debian.cnf contains 'root' a like login and password.
# config = ConfigParser.ConfigParser()
# config.read("/etc/mysql/debian.cnf")
# username = config.get('client', 'user')
# password = config.get('client', 'password')
# hostname = config.get('client', 'host')
# filestamp = time.strftime('%Y-%m-%d')
# 
# # Get a list of databases with :
# database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
# for database in os.popen(database_list_command).readlines():
#     database = database.strip()
#     if database == 'information_schema':
#         continue
#     if database == 'performance_schema':
#         continue
#     filename = "/backups/mysql/%s-%s.sql" % (database, filestamp)
#     os.popen("mysqldump --single-transaction -u %s -p%s -h %s -d %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))
#   
# ```
# 

# <codecell>

import ConfigParser
cfg = ConfigParser.ConfigParser()
cfg.read('config.cfg')
print cfg

print dir(cfg)

# <codecell>

print cfg.sections()

# <codecell>

print cfg.has_section('test')

# <codecell>

print cfg.get('section1', 'bb')

# <markdowncell>

# ###HTML Parsing

# <codecell>

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_doc)

print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link2">
#     Tillie
#    </a>
#    ; and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

# <codecell>

soup.title
# <title>The Dormouse's story</title>

# <codecell>


soup.title.name
# u'title'

# <codecell>


soup.title.string
# u'The Dormouse's story'

# <codecell>

print soup.title.parent.name
# u'head'

# <codecell>

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# <codecell>

soup.p['class']
# u'title'

# <codecell>

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# <codecell>

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_doc)
print [x for x in dir(soup) if 'find' in x]
print soup.findAll('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# <codecell>

soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# <codecell>

#  extracting all the URLs found within a page’s <a> tags:
for link in soup.find_all('a'):
    print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

# <codecell>

#Another common task is extracting all the text from a page:
from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_doc)
print  [x for x in dir(soup) if 'text' in x]
print(soup.text)

# <markdowncell>

# ### XML Parsing

# <markdowncell>

# ```xml
# <data>
#     <items>
#         <item name="item1"></item>
#         <item name="item2"></item>
#         <item name="item3"></item>
#         <item name="item4"></item>
#     </items>
# </data>
# ```

# <codecell>

from xml.dom import minidom
xmldoc = minidom.parse('sample.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)

# <markdowncell>

# __lxml__ is another library.
# 
# New libraries keep coming.
# 
# E.g.: __untangle__
# * untangle is a simple library which takes an XML document and returns a Python object which mirrors the nodes and attributes in its structure.
# 
# * xmltodict is another simple library that aims at making XML feel like working with JSON.

# <codecell>

import untangle
obj = untangle.parse('sample.xml')
obj.root.child['name']

# <markdowncell>

# ```xml
# <mydocument has="an attribute">
#   <and>
#     <many>elements</many>
#     <many>more elements</many>
#   </and>
#   <plus a="complex">
#     element as well
#   </plus>
# </mydocument>
# ```

# <codecell>

import xmltodict

with open('sample2.xml') as fd:
    obj = xmltodict.parse(fd.read())
    
#and then you can access elements, attributes and values like this:

doc['mydocument']['@has'] # == u'an attribute'
doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
doc['mydocument']['plus']['@a'] # == u'complex'
doc['mydocument']['plus']['#text'] # == u'element as well'


# <codecell>

import simplejson

# <codecell>

cmp(1,0)

# <markdowncell>

# ```python
#     >>> import simplejson as json
#     >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#     '["foo", {"bar": ["baz", null, 1.0, 2]}]'
#     >>> print(json.dumps("\"foo\bar"))
#     "\"foo\bar"
#     >>> print(json.dumps(u'\u1234'))
#     "\u1234"
#     >>> print(json.dumps('\\'))
#     "\\"
#     >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
#     {"a": 0, "b": 0, "c": 0}
# 
# ```

