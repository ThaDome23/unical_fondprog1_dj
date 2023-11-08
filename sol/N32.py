status = 'none' ## status none->cresc->decresc altrimenti no

a = int(input())
prec = 0
while a != 0:
    prec = a
    a= int(input())

    if a== 0:
        break

    if a == prec:
        print('NO',end='')
        exit()

    if status == 'none' and a>prec :
        status = 'cresc'
    elif status == 'none' and a<prec :
        print('NO',end='')
        exit()

    if a<prec and status == 'cresc':
        status ='decresc'
    
    if a>prec and status=='decresc':
        print('NO',end='')
        exit()

if status == 'decresc':
    print('SI',end='')
else:
    print('NO',end='')