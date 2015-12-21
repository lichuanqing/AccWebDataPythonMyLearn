# -*- coding: cp936 -*-
import json
import urllib
serviceURL='http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address=raw_input("Enter location:")
    if len(address) <1 :break

    url=serviceURL+urllib.urlencode({'sensor':'false','address':address})
    print 'Retrieving ', url
    data=urllib.urlopen(url).read()
    print 'Retrievd', len(data), 'characters'

    try:js=json.loads(data)
    except:js=None
    if 'status' not in js or js['status'] != 'OK':
        print '===== Failure Retrieved ====='
        continue

   # print json.dumps(js,indent=4)
    place_id=js['results'][0]['place_id']
    print 'Place ID: ',place_id
