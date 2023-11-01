N = int(input())
Ncopy = N
Ninv = 0

while N>0:
    cifra = N%10
    N = N//10
    Ninv = Ninv*10 + cifra
    

print(Ncopy- Ninv,end='')