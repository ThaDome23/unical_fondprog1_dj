n = int(input())

i = 2
primo = True

while i < (n//2+1):
    if n%i== 0: 
        primo =False
    i+=1

print("SI" if primo else "NO",end='')