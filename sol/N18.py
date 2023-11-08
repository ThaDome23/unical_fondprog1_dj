s1 = input()
s2 = input()
c = 0

while s1 != 'o' or s2 != 'k':
    c+=1
    s1 = s2
    s2 = input()

print(c,end='')