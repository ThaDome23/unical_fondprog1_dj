decrescente = False 

prec = int(input())

if prec == 0: a = 0
else: a = int(input())

if prec >= a: 
    print('NO',end='') #caso in cui la stringa inizia in modo decrescente o uguale
    exit()
while a != 0:
    
    if prec > a and not decrescente:
        decrescente = True
    
    if a == prec or (a>prec and decrescente): # se trovo due elementi uguali nella sequenza 
        print('NO',end='')                    # oppure trovo due elementi crescenti quando 
        exit()                                # la stringa è iniziata a decrescere

    prec = a
    a= int(input())

if decrescente:
    print('SI',end='')
else:
    print('NO',end='')