import random
listaNomi = ["Aldo", "Giovanni", "Giacomo"]
voti = {}
for nome in listaNomi:
    voti[nome]= random.randint(18, 30)
print(voti)