
# -*- coding: utf-8 -*-
#!/usr/bin/python
import urllib
from BeautifulSoup import *


# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
s ="哈哈"
ss =u'哈哈'
print  repr(s)
print repr(ss)
print s.decode('utf-8').encode('gbk')
print ss.encode('gbk')
print s.decode('utf-8')
print ss

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
 # Retrieve all of the anchor tags
tags = soup()
for tag in tags:
        url2=tag.get('href',None)
       ##title=tag.get('href',None)
        print tag
        print '+++++++++++++++++++++++++++++++++'
