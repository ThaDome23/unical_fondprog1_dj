lista = []

for i in range(10):
    lista.append(int(input()))

x = int(input())

out='OK'

for ele in lista:
    if ele %x == 0:
        out = 'NO'

print(out,end='')