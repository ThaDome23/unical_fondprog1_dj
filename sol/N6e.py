briscola,seme1,carta1,seme2,carta2 = [int(input()) for _ in range(5)]
valore = [0,11,2,10.5,4,5,6,7,8,9,10]
vincitore = 0

if seme1 == seme2:
    if valore[carta1]>valore[carta2]:
        vincitore = 1
    else:
        vincitore = 2
else:
    if seme1 == briscola:
        vincitore = 1
    elif seme2 == briscola:
        vincitore = 2
    else:
        vincitore = 1

print('VINCE GIOCATORE',vincitore,end='')
