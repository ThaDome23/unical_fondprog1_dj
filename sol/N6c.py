chiamate=int(input())
costo = 5

chiamate -=80
chiamate = max(0,chiamate)

costo += min(60,chiamate)*0.10
chiamate-=60
chiamate = max(0,chiamate)

costo += min(50,chiamate)*0.07
chiamate-=50
chiamate = max(0,chiamate)

costo += chiamate*0.05
costo = round(costo,3)
if costo ==5:
    costo = 5

print(round(costo,3),end='')
