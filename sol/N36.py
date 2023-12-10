lista = [int(input()) for _ in range(10)]

x = int(input())
out='OK'

for ele in lista:
    if ele % x == 0:
        out = 'NO'

print(out,end='')
