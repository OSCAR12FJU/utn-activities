#1
listNum = []
for i in range(100):
    if i % 4 == 0:
        listNum.append(i)
print(listNum)
#2
listRandom = [1,2,3,4,5]
print(listRandom[-1])
#3
listNever = []

for i in range(3):
    listNever.append(i)
print(listNever)
#4
animales = ["perro", "gato", "conejo", "pez"]
nuevos_valores = {1: "loro", -1: "oso"}  

for indice, valor in nuevos_valores.items():
    animales[indice] = valor 

print(animales)
#5
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
#Esta función elimina el último elemento del array.
#6
listNumFive= []
for i = 10 range(30):
    if i %5 === 0:
        listNumFive.append(i)
print(listNumFive)
#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["nuevo1", "nuevo2"]  # Reemplaza índices 1 y 2
print(autos)
#8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)
#10
lista_anidada = [
    15,                          
    True,                        
    [25.5, 57.9, 30.6],          
    False                        
]
print(lista_anidada)