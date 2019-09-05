#Get all Domains
import requests
import json
import sys

def get_help():
    help_description = '''\n\t\t----Get Domains----
    Usage:
    python get_domains.py <hostname> <username> <password>\n'''
    print help_description

def get_domains():
    arguments = sys.argv
    if(len(arguments) < 3):
        get_help()
        return
    hostname = 'https://'+arguments[1]
    username = arguments[2]
    password = arguments[3]
    headers = {'Content-Type': 'application/json'}
    url = hostname+'/v1/domains'
    response = requests.get(url, headers=headers,auth=(username, password))
    if(response.status_code == 200):
        response = json.loads(response.text)
        print json.dumps(response,indent=4, sort_keys=True)
    else:
        print "Error reaching the server."
        exit(1)
get_domains()
