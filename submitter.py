#!/usr/bin/env python3

from time import sleep
import json
import requests as req
import sys,argparse
from termcolor import colored

def change_credentials(u,p):
    j = {'user':u,'password':p}
    file = open('credentials.json','w')
    file.write(json.dumps(j))

req.packages.urllib3.disable_warnings() 

parser = argparse.ArgumentParser(description='Makes a python submission to domjudge hosted at unical')

parser.add_argument('--username',help='sets the username')
parser.add_argument('--password',help='sets the password')

parser.add_argument('filename', help='name of the file to submit', nargs='?', default=None)
parser.add_argument('problem_name', help='name of the problem', nargs='?', default=None)

args = parser.parse_args()

if args.username != None:
    change_credentials(args.username, args.password)
    print('credentials changed')

file = json.load(open("credentials.json"))

user = file['user']
passwd = file['password']

dj_url= 'https://prototypes.mat.unical.it/fondprog1/team/'

sess = req.Session()

sess.post(dj_url+"index.php",data={"cmd":"login","login":user,"passwd":passwd},verify=False)

if args.filename != None and args.problem_name !=None:

    multipart_data = {
        'code[]':(args.filename,open(args.filename,'rb').read().decode()),
        'probid': (None, args.problem_name),
        'langid':(None,'py3'),
        'submit':(None,'submit')
    }

    sess.post(dj_url+"upload.php",files=multipart_data)

while True:
    sleep(1)
    r = sess.get(dj_url)

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(r.text,'html.parser')
    try:
        result_url = soup.find(id='submitlist').find('tbody').find('tr').findAll('td')[3].find('a')['href']
    except:
        print('pending')
        continue
    r = sess.get(dj_url+result_url)

    soup = BeautifulSoup(r.text,'html.parser')

    compilation = soup.findAll('p')[2].text
    status = soup.findAll('p')[0].text

    s = status.split(' ')
    print(compilation)
    print(s[0],end=' ')

    if 'error' in s[1] or 'wrong' in s[1] or 'no-output' in s[1]:
        print(colored(s[1],'red'))
    else:
        print(colored(s[1],'green'))

    break  #exits the program