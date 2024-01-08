def checkMat(matx,j)->bool: #controlla se la somma della L i-esima è multipla dell'elemento
                            #all'angolino della L stessa risorsivamente per tutte le L
    dim = len(matx)

    if j == dim-1: return True

    ele = matx[dim-1-j][j]

    somma = 0

    for i in range(dim-j):
        somma+= matx[i][j]          #verticale
        somma+= matx[dim-1-j][j+i]  #orizziontale

    somma-=ele

    return (somma%ele == 0) and checkMat(matx,j+1) 

N = int(input()) 

matx = [  [ int(input()) for _ in range(N) ]  for _ in range(N) ]

print('SI' if checkMat(matx,0) else 'NO',end='')
