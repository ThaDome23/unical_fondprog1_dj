s = input()
out = 'SI'

while s!= '.':
    if s.isalpha():
        out='NO'
    s = input()

print(out,end='')