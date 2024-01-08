out ='NO'

N = int(input())

num = [int(input()) for _ in range(N)]
den = [int(input()) for _ in range(N)]

for i in range(N-1):
    j=i+1
    #print(num[i]*num[j],(den[i]*den[j]),(num[i]*num[j]) / (den[i]*den[j]))
    if (num[i]*num[j]) == -(den[i]*den[j]):
        out = 'SI'

print(out,end='')