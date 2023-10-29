paga_oraria = 40
minimo = 100

cost_mat= int(input())
ore = int(input())

spesa = cost_mat+ ore*paga_oraria

if spesa<100: print(100,end='')
else: print(spesa,end='')
