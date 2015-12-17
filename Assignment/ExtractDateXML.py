# -*- coding: cp936 -*-
import xml.etree.ElementTree as ET
import urllib

url=raw_input('Enter location:')
print 'Retrieving',url
uh = urllib.urlopen(url)
data=uh.read()

tree=ET.fromstring(data)
lst=tree.findall('comments/comment')
print 'Retrieving',len(data),'characters'
print 'Count: ',len(lst)
numlst=list()
for item in lst:
    #print 'count',item.find('count').text
    numlst.append(item.find('count').text)

sum1=0
for num in numlst:
    sum1=sum1+int(num)
print 'Sum:',sum1
