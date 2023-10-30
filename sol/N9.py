n = int(input())
c = 0
while n != 0:

    if n % 2 != 0 and n % 3 == 0:
        c+=1 

    n = int(input())

print(c,end='')