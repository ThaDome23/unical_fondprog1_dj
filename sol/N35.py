calc = {'s':1,'m':60,'h':3600}

n = int(input())

tot= 0

while n!= 0:
    f = input()
    tot+=calc[f]*n
    n = int(input())

print(tot,end='')