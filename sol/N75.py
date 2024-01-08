string = input()

lista = [0]*26

for l in string:
    if l.isalpha():
        lista[ord(l)-ord('a')]+=1

out = 'SI'

for i in range(26):
    if lista[i] == 0:
        out = 'NO'

print(out,end='')