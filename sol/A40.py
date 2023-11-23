n = int(input())
if n == -50:
    print('VUOTA',end='')
else:
    somma = 0
    lista = []
    while n != -50:
        somma += n
        lista.append(n)

        n = int(input())

    media = somma//len(lista)

    m = 1001
    for i in lista:
        if i >= media and i < m:
            m = i

    print(m,end='')