def euler(a,b): #calcolo MCD ricorsivo
    if a%b == 0:
        return b
    return euler(b,a%b)

a = int(input())
b = int(input())

if b>a: 
    a,b=b,a
print(euler(a,b),end='')