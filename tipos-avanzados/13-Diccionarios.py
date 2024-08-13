punto = {"x": 24, "y": 40}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
#print(punto, punto["lala"])
if "lala" in punto:
    print("encontre a lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala"))

del punto ["x"]
del (punto["y"])

print(punto)
punto["x"] = 25


for valor in punto:
    print(valor, punto[valor])

usuarios = [
    {"id" : 1, "nombre": "chanchito"},
    {"id" : 2, "nombre": "feliz"},
    {"id" : 3, "nombre": "nicolas"},
    {"id" : 4, "nombre": "felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])