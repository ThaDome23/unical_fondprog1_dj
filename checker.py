#!/usr/bin/env python3

import argparse,json,os,glob,shutil,subprocess

def get_ex_path()->str:
    p = get_path()
    arr = p.split('/')
    arr.pop(-1)
    return ('/'.join(arr)+'/Exercises')

def set_path(p):
    j = {'path':p}
    with open('path.json','w') as file:
        file.write(json.dumps(j))

def get_path()->str:
    with open('path.json','r') as file:
        x = json.loads(file.read())['path']
    return x

def create_parser():

    parser = argparse.ArgumentParser(description='check problem using kozajudge')

    parser.add_argument('--kozajudge_path',help='sets the path to koza')
    parser.add_argument('filename', help='name of the file to check', nargs='?', default=None)
    parser.add_argument('problem_name', help='name of the problem to check', nargs='?', default=None)
    return parser.parse_args()

args = create_parser()

if args.kozajudge_path != None:
    set_path(args.kozajudge_path)

if args.problem_name != None:
    path = get_ex_path()
    files = glob.glob(path+'/*')
    for f in files:
        os.remove(f)
   
    shutil.copy(args.filename,path+'/'+args.problem_name+'.py')

    a = subprocess.run(['python3',get_path(),args.problem_name])

    if a.returncode != 0:
        exit(1)
