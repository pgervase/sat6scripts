#!/usr/bin/python
import base64
import urllib2
import json
import ssl
import getpass

username = raw_input("Satellite username: ")
password = getpass.getpass()
satellite = raw_input("Satellite hostname, no https:// : ")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

systemsurl = 'https://' + satellite + '/api/hosts'
systemsreq = urllib2.Request(systemsurl)
systemsbase64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
systemsreq.add_header("Authorization", "Basic %s" % systemsbase64string)   
systemsresult = urllib2.urlopen(systemsreq, context=ctx)
mysystems = systemsresult.read()
parsedsystems = json.loads(mysystems)

mysystems = (parsedsystems['results'])
for system in mysystems:
    print "%s, " % (system['name']),
    try:
        myvar = system['subscription_facet_attributes']
        print myvar['last_checkin']
    except:
        print ""
