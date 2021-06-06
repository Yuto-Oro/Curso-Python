##Tupla -> Son inmutables y tienen metodos propios.
t = ("Cuenta Orlando", 987654321)

##Listas -> Las podemos modificar y tienen metodos propios
lista = ["Cuenta Orlando", 1234567]

#t[1] = 987654321

print("Antes de iterar", lista)
## For 
for elemento in lista:
    if elemento == 1234567:
        lista[1] = 987654321
        print("lista", lista)

print("Despues de iterar", lista)

##Diccionarios -> LLave:Valor, si se pueden modificar y tienen metodos propios.

diccionario = {"a":1, "b":2, "c":3, "d":4}

print(diccionario.items())