N = int(input())

out = 'SI'
lastpari = -400
for i in range(N):
    x = int(input())
    if i %2== 0:
        if x<= lastpari:
            out = 'NO'
        lastpari = x
    else:
        if x %2 == 0:
            out = 'NO'

print(out,end='')