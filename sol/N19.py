s = input()

digit = False
while s != '*':
    if s.isdigit():
        digit = True
    s=input()

print('ALMENO UNA' if digit else 'NESSUNA',end='')