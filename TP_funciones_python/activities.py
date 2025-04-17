# Actividad 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# ------------------------------------------------------------------------

# Actividad 2
def saludar_usuario(nombre):

    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Por favor ingresa tu nombre: ")
print(saludar_usuario(nombre_usuario))

# ------------------------------------------------------------------------

# Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal para actividad 3
print("\nPor favor ingresa tus datos personales:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# ------------------------------------------------------------------------

# Actividad 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal para actividad 4
print("\nCálculo de área y perímetro de un círculo:")
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# ------------------------------------------------------------------------

# Actividad 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal para actividad 5
print("\nConversión de segundos a horas:")
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# ------------------------------------------------------------------------

# Actividad 6
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal para actividad 6
numero = int(input("\nIngresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# ------------------------------------------------------------------------

# Actividad 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito"
    return suma, resta, multiplicacion, division

# Programa principal para actividad 7
print("\nOperaciones básicas entre dos números:")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# ------------------------------------------------------------------------

# Actividad 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal para actividad 8
print("\nCálculo del Índice de Masa Corporal (IMC):")
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# ------------------------------------------------------------------------

# Actividad 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal para actividad 9
print("\nConversión de Celsius a Fahrenheit:")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# ------------------------------------------------------------------------

# Actividad 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal para actividad 10
print("\nCálculo del promedio de tres números:")
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
