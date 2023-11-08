N = int(input())

x = int(input())
cont = 0
out = 'NO'

while x != -1:
    if x<=N:
        cont+=1
        if cont>=N:
            out = 'OK'
    else:
        cont= 0
    x = int(input())

if N == 0:
    out= 'OK'

print(out,end='')