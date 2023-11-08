s = input()
out = 'NO'

while s != '.':
    if s.isalpha():
        out='SI'
    s = input()

print(out,end='')