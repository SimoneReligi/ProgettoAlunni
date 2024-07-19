studenti_voti = {"Aldo" : [],
                 "Giovanni" : [23, 18, 28],
                 "Giacomo" : [30, 22, 22, 24]}
media_voti = {}
for studente, voti in studenti_voti.items():
    if len(voti) != 0:
        media_voti[studente] = round(sum(voti) / len(voti), 2)
print(media_voti)