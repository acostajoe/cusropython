from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
fila.append(6)
fila.append(7)
fila.append(8)
print(fila)
fila.popleft()
print(fila)
if not fila:
    print("fila vacia")

    