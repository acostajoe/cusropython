#set grupo o conjunto
primero = {1, 1, 2, 2, 3, 4} #conjunto
segundo = [3, 4, 5]          #lista
segundo = set(segundo)       #funcion set, remueve los numeros duplicados...

#print(primero | segundo)      # operador | union
#print(primero & segundo)       #operador  & interception, retorna valor que se encuentre dentro de ambas variables
#print(primero - segundo)       #operador - diferente de
#print(primero  ^  segundo)      #operador ^ diferencia simetrica
if 5 in segundo:
    print("hola mundo")