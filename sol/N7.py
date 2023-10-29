n = int(input())
trovato = False

while n != 5:
    if n % 5 == 0:
        trovato=True
    
    n = int(input())

print('ALMENO 1' if trovato else 'NESSUNO',end='')