n = int(input())
totale = 0

if n == -1:
    print('VUOTO',end='')
    exit()

while n != -1:

    if not 0<=n<=9:
        print('ERRORE',end='')
        exit()

    totale = (totale*10 + n)
    n=int(input())
    
print(totale)
if totale % 3 == 0:
    print('SI',end='')
else:
    print('NO',end='')
    