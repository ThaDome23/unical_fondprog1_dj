s = input()

out = 'NESSUNA VOCALE'

while s != '*':
    if s in ['a','e','i','o','u']:
        out='ALMENO 1 VOCALE'
    s = input()

print(out,end='')