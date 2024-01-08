def cerca(x, lista, N)->int:
    if x == 0: return 0
    conta =0
    for i in range(N):
        if lista[i] == x:
            lista[i] = 0
            conta+=1
    return conta + cerca(conta,lista,N)

X = int(input())
N = int(input())

lista = [ int(input()) for _ in range(N)]

print(cerca(X,lista,N),end='')