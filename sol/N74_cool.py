n = int(input())

n -=1

width = 2*n+1

for i in range(n):
    l = 2*i+1
    space = (width - l)//2
    print(space*' '+l*'*'+space*' ')

print(width*'*')

for i in range(n-1,-1,-1):
    l = 2*i+1
    space = (width - l)//2
    print(space*' '+l*'*'+space*' ')