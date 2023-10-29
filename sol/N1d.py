conto = 500
canone = 5 
interessi = 0.02

print("PRIMO MESE:",conto)

conto -= canone
conto = conto + conto*interessi

print("SECONDO MESE:",round(conto))

conto -= canone
conto = conto + conto*interessi

print("TERZO MESE:",round(conto),end='')