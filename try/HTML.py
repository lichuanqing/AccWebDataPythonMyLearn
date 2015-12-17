# -*- coding: cp936 -*-
import re
import urllib
from BeautifulSoup import *

##str1='<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
##result=re.findall('href="(.+)"',str1)
##print result
x = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in x:
        print line.strip()
##url=raw_input('Enter URL-')
html=urllib.urlopen("http://www.py4inf.com/code/romeo.txt").read()
soup=BeautifulSoup(html)
print soup
##tags=soup('a')
##print tags
####for tag in tags:
####        print tag
##   ##     print tag.get('href',None)
