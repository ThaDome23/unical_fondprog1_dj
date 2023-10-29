anno = int(input())

if anno % 100 == 0 and anno % 400 != 0:
    print('NON BISESTILE',end='')

else:

    if anno % 4 == 0:
        print('BISESTILE',end='')
    else:
        print('NON BISESTILE',end='')