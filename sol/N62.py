def valid(i, j, N, M, matrix) -> bool:
    return i >= 0 and j >= 0 and i < N and j < M and matrix[i][j] == -1

def stampaMatrix(matrix, N, M):
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end='')
        print()

def main():
    K = int(input())
    A = [int(input()) for _ in range(K)]
    N = int(input())
    M = int(input())

    matrix = [[-1]*M for _ in range(N)]

    idx = 0
    idxMove = 0
    clockRot = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # refers to i,j variations
    i, j = [0, 0]

    while valid(i, j, N, M, matrix):
        matrix[i][j] = A[idx]

        di, dj = clockRot[idxMove]
        if not valid(i+di, j+dj, N, M, matrix):
            idxMove = (idxMove+1) % 4
            di, dj = clockRot[idxMove]

        i += di
        j += dj

        idx = (idx+1) % K
    stampaMatrix(matrix, N, M)

main()