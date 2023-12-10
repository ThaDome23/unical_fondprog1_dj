def printPavimento(pavimento,dim=20):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j]==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def valid(x,y):
    return x>=0 and y>=0 and x<20 and y<20

penna = True
x = 0
y = 0
pav =[]

def askAndMove(dir:int): #dir is 3 4 5 6 so -3 is 0 1 2 3 
    global penna,x,y,pav

    passi = int(input("passi?"))
    print()

    m = [[0,1],[0,-1],[1,0],[-1,0]] # est,ovest,sud,nord
    k,z = m[dir-3]
    for u in range(passi):
        
        if valid(x+k,y+z):
            x=x+k
            y=y+z
            if penna:
                pav[x][y]=1
        else:
            break

for i in range(20):
    pav.append([0]*20)

c = int(input())
commands=[]
while c != 9:
    commands.append(c)
    c = int(input())

for c in commands:
    if c == 1:
        penna = False
    elif c ==2:
        penna = True
    elif c == 7:
        printPavimento(pav)
    elif c >2 and c <7:
        askAndMove(c)
    #print()
