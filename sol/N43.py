stringa = input()
stack = ['vuota']

check2 = True


for char in stringa:
    if char in ['(',')']:
        if stack[-1] == '(' and char == ')':
            stack.pop()
        else:
            stack.append('(')

for i in range(len(stringa)-1):
    if stringa[i] == '(' and stringa[i+1] == ')' or stringa[i+1] == '(' and stringa[i] == ')':
        check2 = False

if stack == ['vuota']:
    print('ok1')
else:
    print('no1')

if check2:
    print('ok2')
else:
    print('no2')