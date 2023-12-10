memo = [-1]*200

def f(n:int)->int:
    global memo

    if memo[n] != -1:
        return memo[n]
    res = 0

    if n == 0:
        return 2
    else:
        memo[n] = 3* (n+1) * f(n-1)
        return memo[n]


n = int(input())

print(f(n),end='')