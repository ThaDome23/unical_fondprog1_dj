mese = int(input()) -1 #uso i mesi da 0 a 11 per comodità

if mese < 0 or mese >11:
    print('MESE NON VALIDO',end='')
    exit(0)

if mese in [2,5,8,11]: #caso mesi a cavallo
    giorno = int(input())
    if giorno < 1 or giorno >20:           
        mese = ((mese+1)%12)  # considero la stagione succ e nel caso di dicembre+1 vado a gennaio

stagioni = ['INVERNO','PRIMAVERA','ESTATE','AUTUNNO']

print(stagioni[mese//3], end= '')