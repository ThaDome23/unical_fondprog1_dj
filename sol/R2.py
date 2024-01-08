def check_lista(lista,dim,i)->bool:
    if i>=dim//2: return True
    
    return lista[i] == lista[i+N//2] and check_lista(lista,dim,i+1)

N = int(input())

if N % 2 == 1:
    print('NO',end='')
    exit()

lista = [ int(input()) for _ in range(N)]

print('SI' if check_lista(lista,N,0) else 'NO',end='')
