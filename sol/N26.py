a = input()
if a =='*':
    print('NO',end='')
    exit()
 
b = input()
out = 'NO'

while b != '*':

    cond1 = a.isupper() and b.isupper()
    cond2 = a.islower() and a==b
    if cond1 or cond2:
        out = 'SI'
    a=b
    b=input()

print(out,end='')