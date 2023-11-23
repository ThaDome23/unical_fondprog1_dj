cifre = [int(s) for s in input()]
cifre.sort()

n_min = 0
n_max = 0
for i in range(len(cifre)):
    j = len(cifre)-1-i
    n_min = n_min*10 +cifre[i]
    n_max = n_max*10 +cifre[j]

print(n_max-n_min,end='')