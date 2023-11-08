s = input()

while s != '.':
    if not s.isalpha():
        print('NO',end='')
        exit()
    s= input()

print('SI',end='')