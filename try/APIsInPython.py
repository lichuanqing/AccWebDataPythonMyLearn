# -*- coding: cp936 -*-

import urllib
import json

data='''
 {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "AnNaBao",
               "short_name" : "AnNaBao",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Wlshente",
               "short_name" : "Wlshente",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "Mixigen",
               "short_name" : "MI",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "USA",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            }
         ],
         "formatted_address" : "USA",
         "geometry" : {
            "bounds" : {
               "northeast" : {
                  "lat" : 42.3239728,
                  "lng" : -83.6758069
               },
               "southwest" : {
                  "lat" : 42.222668,
                  "lng" : -83.799572
               }
            },
            "location" : {
               "lat" : 42.2808256,
               "lng" : -83.7430378
            },
            "location_type" : "APPROXIMATE",
            "viewport" : {
               "northeast" : {
                  "lat" : 42.3239728,
                  "lng" : -83.6758069
               },
               "southwest" : {
                  "lat" : 42.222668,
                  "lng" : -83.799572
               }
            }
         },
         "place_id" : "ChIJMx9D1A2wPIgR4rXIhkb5Cds",
         "types" : [ "locality", "political" ]
      }
   ],
   "status" : "OK"
}


'''
print "Retrieved",len(data),'Characters'
try:js=json.loads(data)
except:js=None
if 'status' not in js or js['status'] != 'OK':
    print '=====  Failure To Retrieve ========='
    print " "
lat=js['results'][0]['geometry']['location']['lat']
lng=js['results'][0]['geometry']['location']['lng']
print 'lat',lat  ,'lng',lng
placeID=js['results'][0]['place_id']
print "placeID",placeID

