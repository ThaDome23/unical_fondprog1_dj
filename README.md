# Fondamenti di Programmazione I, Università della Calabria A.A. 2023/2024

Sono presenti i vari sorgenti delle soluzioni dei problemi caricati sul portale domjudge

#

## submitter.py

Intended for Linus os, it's a client script for auto-submitting the problems on the domjudge platform 
at [prototypes.mat.unical.it/fondprog1](https://prototypes.mat.unical.it/fondprog1)

It gives also a feedback on the correctness of the problem

For usage is needed to set username and password via the command line flags `--username` and `--password`

#

## wiew.py

It open a web-browser page of the problem pdf hosted on domjudge by specifing a problem name `python3 wiew.py YYY` where YYY is the name (es N1)

#

## checker.py 

(needs a working installation of kozajudge)

Intended for usage with kozajudge, it needs the kozajudge path on the command line flag `--kozajudge_path` then if run it places the problem in the correct kozajudge directory and executes kozajudge.py. It also redirects the kozajudge output on the terminal