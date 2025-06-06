# A Operaciónes con DNI
#1
dni_1 = input("Ingrese el DNI 1: ")
dni_2 = input("Ingrese el DNI 2: ")

#2
conjunto_1 = set(dni_1)
conjunto_2 = set(dni_2)


#3
union_1_2 = conjunto_1.union(conjunto_2)
inserccion_1_2 = conjunto_1.intersection(conjunto_2)
diferencia_1_2 = conjunto_1.diffence(conjunto_2)
diferencia_simetrica_1_2 = conjunto_1.symetric_difference(conjunto_2)

#4-Medir la frecuentacia
for dni in [dni_1, dni_2]:
  print(f"Frecuencia de dígitos en {dni}")
  for d in set(dni):
    print(f"{d}:{dni.count(d)} veces")

#5-Sumar todos los digitos
for dni in [dni_1, dni_2]:
  suma = sum(int(d) for  in dni)
    print(f"Suma de digitos del DNI {dni}:{suma}")

#6-Evaluar las condiciónes lógicas
if '0' not in conjunto_1 and '0' not in conjunto_2 :
  print("Grupo sin ceros")

comun = conjunto_1 & conjunto_2 
 if comun: print(f"Digitos compartidos: {comun}")

#B Operaciónes con años de nacimiento
#Array global (se va a usar en cada punto)
anios = [1978, 1986, 2022]

#1 Diferencia de par e inpar
pares = 0
impares = 0
for anio in anios:
  if anio %2 == 0:
    pares += 1
  else:
    impares += 1

#2 Verificación de el año es mayor a 200
if all(anio > 2000 for anio in anios):
  print("Grupo Z")


#3 Función para ver si el año es bisiento
def es_bisiesto(anio):
  return (anio %4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
#la función va hacer las operaciónes matematicas y nos va a devolver un true o false


if any(es_bisiesto(anio) for anio in anios):
  print("Tenemos un especial")
#Aca realziamos una desturtración de cada año del array y hacermos uso de lafunción y según eso envaimos el msj

#obtenemso el año actual
anios_actuales = [date.today().year - anio for anio in anios]

#segun el año actual que tenemos hacemos una destructración ya de losaños de nuestro array
producto_cartesiano = [(a, e) for a in anios for e in anios_actuales]
print("Producto cartesiano (año, edad):", producto_cartesiano)
#devovlemos los productos cartesianos.
