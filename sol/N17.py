n1 = int(input())

if n1 == 0:
    print('NO',end='')
    exit()

n2 = int(input())

if n2 == 0:
    print('NO',end='')
    exit()

while n2 != 0:

    if n1 %2 == 0 and n2%2== 0 or (n1+n2)%n1 == 0 or (n1+n2)%n2 == 0:
        print('SI',end='')
        exit()

    n1 = n2
    n2 = int(input())

print('NO',end='')
