
N = int(input())

num = {int(input()) for _ in range(N)}
den = {int(input()) for _ in range(N)}


cont = 0
for i in num:
    for j in den:
        if i % j == 0:
            cont+=1

print('SI' if cont == N else 'NO',end='')