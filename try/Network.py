# -*- coding: cp936 -*-
import socket  ##Lib
import urllib
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data=mysock.recv(512)
    if  (len(data)<1):
        break
    print data
mysock.close()


fhand=urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts=dict() ##定义一个字典
for line in fhand:
        words=line.split()
        for word in words:
            counts[word]=counts.get(word,0)+1
print counts,len(counts)
