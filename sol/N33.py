from random import randint,seed
seed(0)

giocFrasi = ['','hai giocato sasso','hai giocato carta','hai giocato forbice']
pcFrasi = ['','il PC ha giocato sasso','il PC ha giocato carta','il PC ha giocato forbice']

ptGioc = 0
ptPc = 0

while ptGioc<3 and ptPc<3:
    sGioc = 4
    while sGioc not in [1,2,3]:
        sGioc = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    
    print(giocFrasi[sGioc])
    sPC = randint(1,3)
    print(pcFrasi[sPC])

    if sGioc == sPC:
        print('Pari:')

    elif(sGioc == 1 and sPC == 3) or (sGioc>sPC and not(sGioc== 3 and sPC== 1)):
        print('Vinci tu:')
        ptGioc+=1
    else:
        print('Vince il PC:')
        ptPc+=1

    print(ptGioc,'-',ptPc,sep='')

if ptPc<ptGioc:
    print("Hai vinto la sfida!")
else:
    print("Il PC ha vinto la sfida!")
