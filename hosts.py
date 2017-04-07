#!/usr/bin/python
import base64
import urllib2
import json
import ssl

username = "admin"
password = "xxxxxx"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

myid = 'spaceman.redhat.com'
URL = "https://satellite.redhat.com/api/v2/hosts/" + myid
req = urllib2.Request(URL)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(req, context=ctx)
myresult = result.read()
parsed_json = json.loads(myresult)
print 'created_at is %s' % (parsed_json['created_at'])
print 'name is %s' % (parsed_json['name'])
sfa = (parsed_json['subscription_facet_attributes'])
last_checkin = sfa['last_checkin']
print last_checkin
print 'subscription_status_label is %s' % (parsed_json['subscription_status_label'])
