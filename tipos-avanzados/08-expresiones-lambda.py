#numeros.sort(reverse=False)
#numeros2 = sorted(numeros)
#print(numeros)
#print(numeros2)

usuarios = [
    ["Chamaquito", 3],
    ["Felipe", 4],
    ["Alberto", 1],
    ["Amalia", 2],
    ["Coral", 5]
]



usuarios.sort(key=lambda el: el[1])
print(usuarios)