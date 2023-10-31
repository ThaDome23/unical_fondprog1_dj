from math import sqrt

def check_prime(n):

    if n==1 or n == 2:
        return True

    primo = True
    i = 2
    while i<sqrt(n)+1 and primo:
        if n % i == 0:
            primo = False
        i+=1    

    return primo

N1 = int(input())
N2 = int(input())

primo1 = check_prime(N1)
primo2 = check_prime(N2)

out ='' 
if not primo1 or not primo2:
    out = 'non entrambi primi'
elif abs(N1 - N2) == 2:
    out = 'gemelli'
else:
    out = 'non gemelli'

print(out,end='')