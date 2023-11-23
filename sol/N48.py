n = int(input())
if n<0:
    print('Empty',end='')
    exit()

prec = -1
sequenze= []

w = []
while n >= 0:
    
    if n<prec:
        sequenze.append(w)
        w = []
    w.append(n)
    prec = n
    n = int(input())
sequenze.append(w)
m = 0
mseq = []
for i in sequenze:
    if len(i)>m:
        m = len(i)
        mseq = i

for i in mseq:
    print(i,end='')
print()
print(m,end='')
