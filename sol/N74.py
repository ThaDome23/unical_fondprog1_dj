n = int(input())

n -=1
width = 2*n+1
sum = 0
for i in range(n):
    l = 2*i+1
    sum+=l*2

sum+=width

print(sum,end='')