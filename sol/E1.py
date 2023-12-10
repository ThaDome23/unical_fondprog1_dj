def validName(s:str)->bool:

    if len(s)==0 or s[0].isdigit():
        return False
    for ele in s[1:]:
        if not ele.isalnum() and ele != '_':
            return False
    
    return True

stato = 'def'
check = False
inp = ''
prec=''
while inp != ':':
    inp = input()

    if stato == 'def':
        if inp != 'def':
            break
        else:
            stato = 'nome_funz'

    elif stato == 'nome_funz':
        if not validName(inp):
            break
        else:
            stato = 'parAp'
    
    elif stato == 'parAp':
        if not (inp) == '(':
            break
        else:
            stato = 'param'

    elif stato == 'param':
        if prec == '(' and inp == ')':
            stato = 'due_punti'
        elif not validName(inp):
            break
        else:
            stato = 'comma'
    elif stato == 'comma':
        if inp == ')':
            stato = 'due_punti'
        elif not (inp)==',':
            break
        else:
            stato = 'param'
    
    elif stato == 'due_punti':
        
        if not (inp)==':':
            break
        else:
            check=True
        
    prec = inp

print('SI' if check else 'NO',end='')