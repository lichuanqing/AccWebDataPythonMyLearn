# -*- coding: cp936 -*-
import json
input='''[
{"id":"001",
    "x":"2",
    "name":"Chuck"
},

{
    "id":"009",
        "x":"7",
    "name":"Chuck"
}

]'''

info=json.loads(input)
print type(info)
print info[0] #list
print "User count",len(info)
for item in info:
    print "name:",item['name']
    print "ID:",item['id']
    print "Attribute",item['x']

















##data='''
##{
##  "name" : "Chuck",
##  "phone" : {
##    "type" : "intl",
##    "number" : "+1 734 303 4456"
##   },
##   "email" : {
##     "hide" : "yes"
##   }
##}
##'''
##info=json.loads(data)
##print type(info)
##print info['phone']['number']
##print 'Name:',info["name"]
##print 'Hide:',info['email']['hide']
