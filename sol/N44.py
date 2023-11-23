cypher = [input() for i in range(26)]

N = int(input())

for i in range(N):
    x = int(input())
    if 0<=x< 26:
        print(cypher[x],end='')