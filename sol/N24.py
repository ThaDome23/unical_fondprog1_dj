def isVocale(c):
    return c in ['a','e','i','o','u']

a = input()

if a == '.':
    print(0,end='')
    exit()

b= input()

conta = 1
while b!= '.':
    if isVocale(a) and isVocale(b) or (not isVocale(a) and not isVocale(b)) :
        conta+=1
    a = b
    b = input()

print(conta,end='')



