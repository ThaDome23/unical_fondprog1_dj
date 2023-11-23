
#lista_posti= [0,[0]*5,[0]*5]
x
n_posti = [0,0,0]  # n_posti[1] posti reparto fumatori, n_posti[2] reparto NON fumatori

frase = ['','Reparto fumatori, posto','Reparto NON fumatori, posto']

while n_posti[1] <5 or n_posti[2] <5:
    x = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    
    if n_posti[x] <5:
      #  lista_posti[x][n_posti[x]] = 1 
        print(frase[x],n_posti[x]+1 + (5 if x == 2 else 0))
        n_posti[x]+=1
    else:
        scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
        if scelta == 'S':
            x = (x)%2 +1
            #lista_posti[x][n_posti[x]] = 1 
            print(frase[x],n_posti[x]+1 +(5 if x == 2 else 0))
            n_posti[x]+=1
        else:
            print("Il prossimo volo parte tra 3 ore")

        
