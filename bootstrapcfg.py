#!/usr/bin/python
######
# Author: Peter Gervase
# pgervase@redhat.com
# This script will be for configuring a bootstrap script for a sat 6 client
# This can be used for https://bugzilla.redhat.com/show_bug.cgi?id=1413130
######
import re
import sys
import shutil

from optparse import OptionParser
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--new","-n", dest="new", help="Use this to save the output to a file other than bootstrap.py")
parser.add_argument("--old","-O", dest="old", help="Use this if the file you're going to modify isn't bootstrap.py")
parser.add_argument("--server","-s", dest="server", help="FQDN of Foreman OR Capsule - omit https://")
parser.add_argument("--activationkey","-a", dest="activationkey", help="Activation Key to register the system")
parser.add_argument("--hostgroup","-g", dest="hostgroup", help="Title of the Hostgroup in Foreman that the host is to be associated with")
parser.add_argument("--location","-l", dest="location", help="Title of the Location in Foreman that the host is to be associated with")
parser.add_argument("--organization","-o", dest="organization", help="Name of the Organization inForeman that the host is to be associated with")
args, leftovers = parser.parse_known_args()

oldfile = "bootstrap.py"
newfile = "bootstrap.py"

if args.old is not None:
    oldfile = args.old
    print oldfile
#    shutil.copyfile(args.old,oldfile)
    oldfile = args.old
else:
    pass

if args.new is not None:
    newfile = args.new
    print newfile
    shutil.copyfile(oldfile,newfile)
    oldfile = newfile
else:
    pass



if args.server is not None:
    print "server is " + args.server + "\n"
    serverstarter = '^    parser.add_option\(\"-s\",.*'
    serverupdated = "    parser.add_option(\"-s\", \"--server\", default=\"" + args.server + "\", dest=\"foreman_fqdn\", help=\"FQDN of Foreman OR Capsule - omit https://\", metavar=\"foreman_fqdn\")"
    #print serverupdated
    with open(oldfile, 'r') as sources:
        lines = sources.readlines()
    with open(newfile, 'w') as sources:
        for line in lines:
            sources.write(re.sub(serverstarter, serverupdated, line))
else:
    pass
#    print "server is blank\n"

if args.activationkey is not None:
    print "act key is " + args.activationkey + "\n"
    actstarter = '^    parser.add_option\(\"-a\",.*'
    actupdated = "    parser.add_option(\"-a\", \"--activationkey\", default=\"" + args.activationkey + "\", dest=\"activationkey\", help=\"Activation Key to register the system\", metavar=\"ACTIVATIONKEY\")"
    with open(oldfile, 'r') as sources:
        lines = sources.readlines()
    with open(newfile, 'w') as sources:
        for line in lines:
            sources.write(re.sub(actstarter, actupdated, line))
else:
    pass
#    print "act key is blank\n"

if args.hostgroup is not None:
    print "hostgroup is " + args.hostgroup + "\n"
    hgstarter = '^    parser.add_option\(\"-g\",.*'
    hgupdated = "    parser.add_option(\"-g\", \"--hostgroup\", default=\"" + args.hostgroup + "\", dest=\"hostgroup\", help=\"Title of the Hostgroup in Foreman that the host is to be associated with\", metavar=\"HOSTGROUP\")"
    with open(oldfile, 'r') as sources:
        lines = sources.readlines()
    with open(newfile, 'w') as sources:
        for line in lines:
            sources.write(re.sub(hgstarter, hgupdated, line))
else:
    pass
#    print "hostgroup is blank\n"

if args.location is not None:
    print "location is " + args.location + "\n"
    locstarter = '^    parser.add_option\(\"-L\",.*'
    locupdated = "    parser.add_option(\"-L\", \"--location\", default=\"" + args.location + "\", dest=\"location\", help=\"Title of the Location in Foreman that the host is to be associated with\", metavar=\"LOCATION\")"
    with open(oldfile, 'r') as sources:
        lines = sources.readlines()
    with open(newfile, 'w') as sources:
        for line in lines:
            sources.write(re.sub(locstarter, locupdated, line))
else:
    pass
#    print "hostgroup is blank\n"

if args.organization is not None:
    print "organization is " + args.organization + "\n"
    orgstarter = '^    parser.add_option\(\"-o\",.*'
    orgupdated = "    parser.add_option(\"-o\", \"--organization\", default=\"" + args.organization + "\", dest=\"org\", help=\"Name of the Organization in Foreman that the host is to be associated with\", metavar=\"ORG\")"
    #print serverupdated
    with open(oldfile, 'r') as sources:
        lines = sources.readlines()
    with open(newfile, 'w') as sources:
        for line in lines:
            sources.write(re.sub(orgstarter, orgupdated, line))
else:
    pass
#    print "organization is blank\n"
'''
checkargs = ['server', 'activationkey', 'hostgroup', 'location', 'organization']
myargs = vars(args)
print myargs
print "args.activationkey = " + str(args.activationkey) + "\n"

for myarg in myargs:
    print "myarg is " + myarg
    print str(args.myarg)
    if args.myarg is not None:
        print myarg + " is " + args.myarg + "\n"
    else:
        print myarg + " is blank\n"
'''

numargs = len(sys.argv)
if numargs < 2:
    ### no args passed in, so prompt the user
    pass
