#!/usr/bin/env python3

import webbrowser
import sys,json,os
import requests as req

if len(sys.argv) != 2:
    print('errore')

req.packages.urllib3.disable_warnings() 

url = 'https://prototypes.mat.unical.it/fondprog1/team/problem.php?id='+sys.argv[1]

dj_url= 'https://prototypes.mat.unical.it/fondprog1/team/'

sess = req.Session()

user,passwd= json.load(open("credentials.json")).values() #unpacking directly the whole dictionary

sess.post(dj_url+"index.php", data={"cmd":"login","login":user,"passwd":passwd}, verify=False)

page = sess.get(url,verify=False)

if page.status_code == 200:
    f = open(f'prob_stat/{sys.argv[1]}.pdf','wb')
    f.write(page.content)
    f.close()

    webbrowser.open_new_tab(f'./prob_stat/{sys.argv[1]}.pdf')

else:
    print('bad request')