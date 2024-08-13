usuarios = [
    ["camello", 4],
    ["carro", 1],
    ["caballo", 3]
]

#nombres = []
#for usuarios in usuarios:
 #   nombres.append(usuarios[0])
#print(nombres)
#map
#nombres = [usuario[0] for usuario in usuarios]
#filter
#nombres = [usuario for usuario in usuarios if usuario[1 > 2]]
#nombres = [usuario[0] for usuario in usuarios if usuario[1 > 2]]

#nombres = list(map(lambda usuario: usuario[0], usuarios))

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)