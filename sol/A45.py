M = input()

flag = True

if M[0].isdigit():
    flag=False

for i in M:
    if not i.isalnum() and i != '_':
        flag=False

print('SI' if flag else 'NO',end='')