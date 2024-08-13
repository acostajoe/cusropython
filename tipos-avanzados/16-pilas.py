pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)
pila.append(6)
print(pila)
ultimoElemento = pila.pop()
print(ultimoElemento)
print(pila)
print(pila[-1])
if not pila:
    print("pila vacia")