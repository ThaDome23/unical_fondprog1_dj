#!/usr/bin/env python3

from time import sleep
import json
import requests as req
import argparse
from bs4 import BeautifulSoup

from rich.progress import (Progress,SpinnerColumn,TextColumn)

step_progress = Progress(
    TextColumn('Pending: '),
    SpinnerColumn("aesthetic")
)

req.packages.urllib3.disable_warnings() 

def change_credentials(u,p):
    j = {'user':u,'password':p}
    file = open('credentials.json','w')
    file.write(json.dumps(j))

def create_parser():

    parser = argparse.ArgumentParser(description='Makes a python submission to domjudge hosted at unical')

    parser.add_argument('--username',help='sets the username')
    parser.add_argument('--password',help='sets the password')

    parser.add_argument('filename', help='name of the file to submit', nargs='?', default=None)
    parser.add_argument('problem_name', help='name of the problem', nargs='?', default=None)

    return parser.parse_args()

args = create_parser()

if args.username != None:
    change_credentials(args.username, args.password)
    print('credentials changed')
    exit()

user,passwd= json.load(open("credentials.json")).values() #unpacking directly the whole dictionary

dj_url= 'https://prototypes.mat.unical.it/fondprog1/team/'
id = step_progress.add_task('')
sess = req.Session()

sess.post(dj_url+"index.php", data={"cmd":"login","login":user,"passwd":passwd}, verify=False)

if args.filename != None and args.problem_name !=None:
    step_progress.start()
    multipart_data = {
        'code[]':(args.filename,open(args.filename,'rb').read().decode()),
        'probid': (None, args.problem_name),
        'langid':(None,'py3'),
        'submit':(None,'submit')
    }

    sess.post(dj_url+"upload.php",files=multipart_data)

while True:

    soup = BeautifulSoup(  sess.get(dj_url).text  , 'html.parser')
    try: #got from analyzing the website
        result_url = soup.find(id='submitlist').find('tbody').find('tr').findAll('td')[3].find('a')['href']
    except: #case when the submission is still pending
        sleep(0.5)
        continue

    #because we need to enter in the specific submission url
    soup = BeautifulSoup(  sess.get(dj_url+result_url).text  , 'html.parser')

    status = soup.findAll('p')[0].text
    s = status.split(' ')

    step_progress.stop()
    step_progress.console.print('[green]DONE')
    
    color='green'
    if 'error' in s[1] or 'wrong' in s[1] or 'no-output' in s[1]:
        color = 'red'

    step_progress.console.print(s[0]+' ['+color+']'+s[1])
    break  #exits the program