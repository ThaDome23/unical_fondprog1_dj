M = int(input())
N = int(input())

matx= []                            #lettura
for i in range(M):
    matx.append([])
    for j in range(N):
        matx[i].append(int(input()))

conta_5 = []
for i in range(M):
    conta = 0
    for j in range(N):
        conta+= 1 if matx[i][j] > 5 else 0
    conta_5.append(conta)

Max = conta_5[0]
idx = 0
for i in range(M):
    if conta_5[i]>= Max:
        idx = i
        Max = conta_5[i]

sums =[]

for j in range(N):
    sum = 0
    for i in range(M):
        sum+= matx[i][j]
    sums.append(sum)

Min = sums[0]
idx2 = 0
for i in range(N):
    if sums[i]<= Min:
        idx2 = i
        Min = sums[i]

print(idx,idx2,end='')

