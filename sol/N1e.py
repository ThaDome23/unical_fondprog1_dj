conto = int(input())
canone = int(input())
interessi = int(input())/100

print("PRIMO MESE:",conto)

conto -= canone
conto = conto + conto*interessi

print("SECONDO MESE:",round(conto))

conto -= canone
conto = conto + conto*interessi

print("TERZO MESE:",round(conto),end='')