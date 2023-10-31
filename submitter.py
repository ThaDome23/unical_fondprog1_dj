#!/usr/bin/env python3

from time import sleep
import json
import requests as req
import sys,argparse

def change_credentials(u,p):
    j = {'user':u,'password':p}
    file = open('credentials.json','w')
    file.write(json.dumps(j))

req.packages.urllib3.disable_warnings() 

parser = argparse.ArgumentParser(description='Makes a python submission to domjudge hosted at unical')

parser.add_argument('--username',help='sets the username')
parser.add_argument('--password',help='sets the password')

parser.add_argument('filename', help='name of the file to submit')
parser.add_argument('problem_name', help='name of the problem')

args = parser.parse_args()

change_credentials(args.username, args.password)

file = json.load(open("credentials.json"))
user = file['user']
passwd = file['password']

sess = req.Session()

x = sess.post("https://prototypes.mat.unical.it/fondprog1/team/index.php",
                data={"cmd":"login","login":user,"passwd":passwd},verify=False)

multipart_data = {
    'code[]':(args.filename,open(args.filename,'rb').read().decode()),
    'probid': (None, args.problem_name),
    'langid':(None,'py3'),
    'submit':(None,'submit')
}

r = sess.post("https://prototypes.mat.unical.it/fondprog1/team/upload.php",files=multipart_data)
#print(r.text)
