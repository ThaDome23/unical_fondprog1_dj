#!/usr/bin/env python3

import webbrowser
import sys

if len(sys.argv) != 2:
    print('errore')

url = 'https://prototypes.mat.unical.it/fondprog1/team/problem.php?id='+sys.argv[1]

webbrowser.open_new_tab(url)