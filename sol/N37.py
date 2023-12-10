cont = 0
lista = [input() for _ in range(100)]

for c in ['a','e','i','o','u']:
    cont+= min(lista.count(c),1)

print('OK' if cont<=1 else 'ERRORE',end='')