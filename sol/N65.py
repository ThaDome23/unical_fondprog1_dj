N_STUDENTI = 70

pesi = [int(input()) for _ in range(8)]


voti = []
matricole = []

for _ in range(N_STUDENTI):

    matricole.append(input())
    media_pes = 0

    for i in range(8):
        media_pes+= pesi[i]*int(input())

    voti.append(media_pes)

cutoff = int(input())

conta = 0
idx_max = 0
idx_min = 0
Max = 0
Min = 99999999

for i in range(N_STUDENTI):
    if voti[i]>= cutoff:
        print(matricole[i],voti[i])
        conta+=1

        if voti[i]<Min:
            Min = voti[i]
            idx_min = i

        if voti[i]>Max:
            Max = voti[i]
            idx_max = i

print(conta,matricole[idx_max],matricole[idx_min],end='')