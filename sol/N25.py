gotZero = False
somma = 0

while True:
    n = int(input())
    if n == 0:
        if gotZero:
            break
        print(somma)
        somma=0
        gotZero = True
    else:
        gotZero=False
        somma += n
    

