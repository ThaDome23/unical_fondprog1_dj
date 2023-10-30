from time import sleep
import json
import requests as req
import sys

file = json.load(open("credentials.json"))

req.packages.urllib3.disable_warnings() 

if len(sys.argv) < 2:
    print('devi inserire il nome del file')
    exit(1)

name = './sol/'+sys.argv[1]

user = file['user']
passwd = file['password']

sess = req.Session()

x = sess.post("https://prototypes.mat.unical.it/fondprog1/team/index.php",data={"cmd":"login","login":user,"passwd":passwd},verify=False)

print(x.text)
multipart_data = {

    'code[]':(name[6:],open(name,'rb').read().decode()),
    'probid': (None, name[6:].split('.')[0]),
    'langid':(None,'py3'),
    'submit':(None,'submit')
}


r = sess.post("https://prototypes.mat.unical.it/fondprog1/team/upload.php",files=multipart_data)

