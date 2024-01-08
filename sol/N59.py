N = int(input())

matrix = []

for i in range(N):
    matrix.append([])
    for j in range(N):
        matrix[i].append(int(input()))

mid = N//2
sommaCroce = matrix[mid][mid]
sommaResto = 0
for i in range(N):
    for j in range(N):
        if i == mid or j == mid:
            if i!=j:
                sommaCroce+=matrix[i][j]
        else:
            sommaResto += matrix[i][j]

print('OK' if sommaCroce > sommaResto else 'NO',end='')
#print(sommaCroce,sommaResto)