
cont = 0
lista = []
for i in range(100):
    lista.append(input())

for c in ['a','e','i','o','u']:
    cont+= min(lista.count(c),1)

print('OK' if cont<=1 else 'ERRORE',end='')