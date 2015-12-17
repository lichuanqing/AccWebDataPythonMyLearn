# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


url = raw_input('Enter URL: ')
readin= raw_input('Enter count: ')
count=int(readin)
readin= raw_input('Enter position: ')
posi=int(readin)
print"Retrieving:",url
k=0
while  k<count:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        # Retrieve all of the anchor tags
        tags = soup('a')
        tag=tags[posi-1]
        url=tag.get('href',None)
        print "Retrieving:",url
        k=k+1
