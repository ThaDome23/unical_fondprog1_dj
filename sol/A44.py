n = input()
s1 = 0
s2 = 0
for i in range(len(n)//2):
    s1+=int(n[i])
    s2+=int(n[i+len(n)//2])

if s1==s2:
    print('FORTUNATO',end='')
else:
    print('SFORTUNATO',end='')
     