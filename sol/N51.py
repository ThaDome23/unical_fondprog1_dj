n = input()
seq1 = []
seq2 = []
while n != '.':
    seq1.append(n)
    n= input()

n = input()
while n != '.':
    seq2.append(n)
    n= input()

for i in seq1:
    if i in seq2:
        print(i,end='')
        exit()

print('DISGIUNTE',end='')
