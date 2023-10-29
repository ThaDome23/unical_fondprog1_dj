costo = float(input())
tipo = int(input())

sconti = [0,10,15,25]

print(round(costo- costo*sconti[tipo]/100,3) ,end='')