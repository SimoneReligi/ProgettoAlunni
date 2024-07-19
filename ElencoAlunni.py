import random
studenti_voti = {"Aldo" : [23, 22, 27],
                 "Giovanni" : [23, 18, 28],
                 "Giacomo" : [30, 22, 22]}
media_voti = {}
for studente, voti in studenti_voti.items():
    media_voti[studente] = round(sum(voti) / len(voti), 2)
print(media_voti)