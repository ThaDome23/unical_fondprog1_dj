def farfallizza(s)->str:
    s2 = ''
    for ele in s:
        s2+=ele
        if ele in ['a','e','i','o','u']:
            s2+='f'+ele

    return s2

stringa = input()


new_stringa = farfallizza(stringa)
N = len(new_stringa)
print(new_stringa[N//2:]+new_stringa[0:N//2],end='')