# -*- coding: cp936 -*-
import json
import urllib

url=raw_input('Enter location:')
print 'Retrieving ', url

try:data=urllib.urlopen(url).read()
except:data=None
js=json.loads(data)
comments=js['comments']
Count=len(comments)
print 'Count',Count
sum1=0
for comment in comments:
    sum1=sum1+int(comment['count'])
print 'Sum',sum1
