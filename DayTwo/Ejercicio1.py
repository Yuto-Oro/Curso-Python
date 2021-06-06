"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es 
cada una de las asignaturas de la lista. """

##Lista, For

asignaturas = ["Matemáticas","Física","Química","Historia","Lemgua"]
for asignatura in asignaturas:
    print("Yo estudio " + asignatura)


"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
## Forma 1
numeros = []
print("Forma 1")
for i in range(1, 11):
    numeros.append(i)
numeros.reverse()
print(numeros)


## Forma 2
numeros1 = []
print("Forma 2")
for i in range(1, 11):
    numeros1.append(i)
numeros1.reverse()
for n in numeros1:
    print(n, end=", ")
print("Forma 2")

## Forma 3
print("Forma 3")
numeros2 = []
for i in range(1, 11):
    numeros2.append(i)

for i in range(1, 11):
    print(numeros2[-i], end=", ")
print("Forma 3")
