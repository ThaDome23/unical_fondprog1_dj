A = int(input())
B = int(input())
C = int(input())

res= ''

if A<B+C and B<A+C and C<B+A:
    if A==B and B == C:
        res = 'TRIANGOLO EQUILATERO'
    elif A==B or B==C or C== A:
        res= 'TRIANGOLO ISOSCELE'
    else:
        res = 'TRIANGOLO SCALENO'
else:
    res='NO'


print(res,end='')
    