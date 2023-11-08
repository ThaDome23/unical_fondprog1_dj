a = input()

if a == '*':
    print('NO',end='')
    exit()

b = input()

out = 'NO'

while b!= '*':

    if a == b and a.isalpha():
        out='SI'
    a = b
    b= input()

print(out,end='')