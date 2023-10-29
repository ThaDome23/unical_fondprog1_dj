voto = int(input())

if voto <0 or voto>30:
    print('VOTO NON VALIDO',end='')
elif voto>=18:
    print('ESAME SUPERATO',end='')
else:
    print('BOCCIATO',end='')