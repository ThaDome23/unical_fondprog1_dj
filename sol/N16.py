X = int(input())
n = int(input())

zeri_cons = False
cont = 0

while n != -1:
    if n == 0:
        cont+=1
        if cont>=X:
            zeri_cons = True
    else:
        cont = 0

    n=int(input())
    
print('OK' if zeri_cons or X==0 else 'NO',end='')

