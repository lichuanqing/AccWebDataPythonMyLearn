# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
grads=list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    str1=str(tag)
    grad=re.findall('>([0-9]+)<',str1)
    grads.append(grad[0])

sum1=0
for grad in grads:
        sum1=sum1+int(grad)
print "Count",len(grads)
print "Sum",sum1
