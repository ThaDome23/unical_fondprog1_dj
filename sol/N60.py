S = input()
N= int(input())
lista = []
out =''

for _ in range(N):
    lista.append(input())

for i in range(N):
    for j in range(i+1,N):
        if lista[i]+lista[j] == S or lista[j]+lista[i] == S:
            out = 'OK'

if out == '':
    lista.sort()
    out = lista[-1]+lista[0]

print(out,end='')