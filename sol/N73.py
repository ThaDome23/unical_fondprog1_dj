n = int(input())
N = str(n)
nuovo_numero = ''


conta = 1
for i in range(1,len(N)):
    if N[i] != N[i-1]:
        nuovo_numero+=str(conta)+N[i-1]
        conta=1
    else:
        conta+=1

nuovo_numero+= str(conta)+N[-1]

print(nuovo_numero,len(nuovo_numero),end='')