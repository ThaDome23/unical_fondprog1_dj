#somma diagonale secondaria

def sommaNonRec(matx,N):
    somma=0
    for i in range(N):
        somma+=matx[i][N-i-1]

    return somma

def sommaRec(matx,N,i):
    if i>=N: return 0
    return matx[i][N-i-1] + sommaRec(matx,N,i+1)


N = int(input()) 

matx = []
for i in range(N):
    matx.append([])
    for j in range(N):
        matx[i].append(int(input()))

print(sommaRec(matx,N,0),';',sommaNonRec(matx,N),sep='',end='')