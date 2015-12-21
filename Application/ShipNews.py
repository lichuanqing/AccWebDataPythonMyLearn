# -*- coding: cp936 -*-
import json
import urllib
import xml.etree.ElementTree as ET

##str.decode('utf-8').encode('gbk')
url=raw_input("请输入网址：")
data=urllib.urlopen(url).read()
print data

trees=ET.ElementTree(data)
lst=trees.findall('/div')
print lst
