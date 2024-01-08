def punteggio(a,b):
    pt = 0
    for i in range(20):  # because we have 20 questions
        if a[i] == b[i]:
            pt+=2
        elif b[i] != 'X':   # la risposta è sbagliata e non è in caso in cui è non data
            pt-=1
    return pt


N_STUDENTI = 90

esatte = input()

for _ in range(N_STUDENTI):
    matricola = input()
    risposte = input()

    punti = punteggio(esatte,risposte)

    print(matricola,punti)

    
