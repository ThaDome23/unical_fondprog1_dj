n1 = int(input())
n2 = int(input())
n3 = int(input())
conta = 0

while n1 != 9 or n2!= 9 or n3!= 9:
    
    if n1==n2 and n2==n3:
        conta+=1
    
    n1 = n2
    n2 = n3
    n3 = int(input())

print(conta,end='')