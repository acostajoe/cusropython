usuarios = [
    ["camello", 4],
    ["carro", 1],
    ["caballo", 3]
]

#nombres = []
#for usuarios in usuarios:
 #   nombres.append(usuarios[0])
#print(nombres)
#nombres = [usuario[0] for usuario in usuarios]

#nombres = [usuario for usuario in usuarios if usuario[1 > 2]]
nombres = [usuario[0] for usuario in usuarios if usuario[1 > 2]]

print(nombres)
