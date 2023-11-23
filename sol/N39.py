n = int(input())

pot_due=True

while n!= 0:

    for i in range(3,n//2 +3,2):
        if n%i == 0:
            pot_due=False
    n = int(input())

print('SI' if pot_due else 'NO',end='')