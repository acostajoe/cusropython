numeros = [2, 4, 1, 45, 75, 22, 15, 10]

#numeros.sort(reverse=False)
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

usuarios = [
    ["Chamaquito", 3],
    ["Felipe", 4],
    ["Alberto", 1],
    ["Amalia", 2],
    ["Coral", 5]
]

#funcion para el methodo sort
def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=False)
print(usuarios)