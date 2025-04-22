precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

#1) Dado el diccionario precios_frutas 
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas[Naranja] = 1200
precios_frutas[Manzana] = 1500
precios_frutas[Pera] = 2300

print("Despues de agregarle las nuevas frutas:")
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Despues de actualizar las nuevas frutas:")
print(precios_frutas) 

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
nombres_frutas = []
for fruta in precios_frutas:
    nombres_frutas.append(fruta)

print(nombres_frutas)

#4) Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."

class Persona:
    def __init__(self, nombre, pais, edad):
        # Asignamos atributos al objeto
        self.nombre = nombre
        self.pais   = pais
        self.edad   = edad

    def saludar(self):
        # Método que imprime el saludo formateado
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

#5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. Ayuda: el módulo math puede ser de utilidad para usar la constante �
class Circulo:
    def __init_ (self, radio)
    self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

#6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente balanceados usando una pila.

def balanceado(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    
    return len(pila) == 0


#7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
#● Agregar clientes (encolar).
#● Atender clientes (desencolar).
#● Mostrar el siguiente cliente en la fila.
class ColaBanco:
    def __init__(self):
        self.cola = []
    def agregar_cliente(self, nuevoturno):
        self.cola.append(nuevo_turno)
    def atender_client(self):
        if self.cola:
            return self.cola.pop(0)
        else:
            return "No hay clientes en la fila."
    def mostrar_siguiente(self):
        if self.cola:
            return self.cola[0]
        else: 
            return "No hay clientes en espera."

#8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados.

#Node
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

#Objeto Lista
class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo
    def recorrer(self):
        actual = self.inicio
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente

#9) Dada una lista enlazada, implementa una función para invertirla.

def invertir(self):
    prev = None
    actual = self.inicio
    while actual:
        sig = actual.siguiente
        actual.siguiente = prev
        prev = actual
        actual = sig
        self.inicio = prev