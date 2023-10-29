X = int(input())
N = int(input())

while N >0:
    n =int(input())
    if n %2 == 0 and n<X:
        print(n,sep='',end='')
        
    N-=1