n = int(input())
r = 'SI'
if n==0: r= 'NO'
while n>0:
    c = n%10
    n = n//10
    if c == 0:
        r = 'NO'

print(r,end='')