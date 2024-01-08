def printRev(lista,dim):
    if dim == 0: return
    
    print(lista[dim-1],end='')
    printRev(lista,dim-1)

N = int(input())

lista = [ int(input()) for _ in range(N)]

printRev(lista,N)