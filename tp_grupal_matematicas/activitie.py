#Conversión de Números:
#Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
#Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

"""Me parece que la forma mas sencilla de hacer un proyecto que tenga que ver con lo visto hasta el momento es realizar una calculadora, en principio en la cual el usuario
1)ingrese de que tipo de base tiene el numero que quiere ingresar.
    (1)2= Binario
    (2)10= Decimal
    (3)8= Octal
    (4)16= Hexadecimal

2) una vez determinada la base el programa debe mostrar el resultado de todas las conversiones

"""
# FUNCIONES NECESARIAS PARA LA CONVERSIÓN DE NÚMEROS A OTRAS BASES
#función para pasar de binario a decimal
def bin_a_dec(binario):
    decimal = 0   #se crea la variable "decimal" y se le da el valor 0
    for i, bit in enumerate(reversed(binario)):
        # aca se enumera el numero ingresado en la variable binario y se lo da vuelta ... luego use "enumerate", que lo que hace es recorrer el String , el numero ingresado por el usuario es un string, y va separando cada valor y lo coloca en un indice. es decir que en la posición i se le va colocando el indice del valor bit, el valor de cada bit es el binario dado vuelta
        if bit == "1":# mientras que el valor de bit sea 1 se suma su valor posicional algo asi como la regla de los dedos para sumar bits
            decimal += 2 ** i # calcula el valor haciendo 2 elevado a la posición que se le dio anteriormente i y lo suma al resultado
    return decimal #retorna el decimal


# función para pasar de binario a octal
def bin_a_oct(binario):
    decimal = bin_a_dec(binario)
    return dec_a_oct(decimal)

# función para pasar de binario a hexadecimal
def bin_a_hex(binario):
    decimal = bin_a_dec(binario)
    return dec_a_hex(decimal)

# función para pasar de decimal a binario
def dec_a_bin(decimal):
    if decimal == 0: #si el valor decimal es 0 retorna 0  sin mas
        return '0'
    binario = ''#se inicializa binario que es donde se guardara finalmente el resultado
    while decimal > 0:#mientras decimal es mayor a 0 el ciclo se repite cada vez hasta llegar a 0
        binario = str(decimal % 2) + binario #se calcula el resto y se convierte e string y se agrega un bit
        decimal = decimal // 2 # a decimal se lo divide por dos y se descarta el resto
    return binario #retorna el valor de binario

# función para pasar de decimal a octal
def dec_a_oct(decimal): #Convierte decimal  a octal, los pasos son iguales que de decimal a binario pero solo el valor de la ecuación cambia a 8
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

# función para pasar de decimal a hexadecimal
def dec_a_hex(decimal):#Convierte decimal a hexadecimal
    if decimal == 0:
        return '0'
    hex_digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F') #valores unitarios posibles dentro de ese sistema dentro de una lista de tipo tupla
    hexadecimal = '' #esta es la variable que se va a devolver o llenar
    while decimal > 0:
        hexadecimal = hex_digitos[decimal % 16] + hexadecimal #se iguala el valor ingresado con su ubicación el la tupla
        decimal = decimal // 16
    return hexadecimal

# función para pasar de octal a decimal
def oct_a_dec(octal):#Convierte octal a decimal
    decimal = 0
    for i, digito in enumerate(reversed(octal)):#recorre octal pero en forma invertida y asigna un valor a cada ubicación de i
        decimal += int(digito) * (8 ** i)# formula para convertir de base 8 a 10, a sabiendas que digito primero debe ser convertido a int ya que ingresa como string
    return decimal#retorna el valor decimal

# función para pasar de octal a binario
def oct_a_bin(octal):#Convierte de octal a binario utilizando las funciones anteriores
    decimal = oct_a_dec(octal)#primero lo transforma en decimal
    return dec_a_bin(decimal)#aca toma el decimal anterior y lo transforma a bin

# función para pasar octal a hexadecimal
def oct_a_hex(octal):#convierte de octal a hexadecimal
    decimal = oct_a_dec(octal)# utiliza la función para transformar de octal a decimal y guardarlo en la variable octal
    return dec_a_hex(decimal)#utiliza el decimal anterior y lo transforma en hexadecimal

# función para pasar de hexadecimal a decimal
def hex_a_dec(hexadecimal):#Convierte hexadecimal (string) a decimal
    hex_digitos = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15} #aca tuve que hacer un diccionario con los valores
    decimal = 0
    for i, digito in enumerate(reversed(hexadecimal.upper())):#aca se agrega la el método upper que lo que hace es transformar las letras ingresadas en mayúscula asi no se tiene que crear un diccionario tan grande
        decimal += hex_digitos[digito] * (16 ** i)  #la conversion es similar a todas las anteriores
    return decimal

# función para pasar de hexadecimal a binario
def hex_a_bin(hexadecimal):#Convierte de hexadecimal a binario
    decimal = hex_a_dec(hexadecimal)# utiliza la función para transformar de hexadecimal a decimal y guardarlo en la variable hexadecimal
    return dec_a_bin(decimal) #solo toma el numero convertido a decimal para transformarlo a binario

# función para pasar de hexadecimal a octal
def hex_a_oct(hexadecimal):##Convierte de hexadecimal a octal
    decimal = hex_a_dec(hexadecimal)# utiliza la función para transformar de hexadecimal a decimal y guardarlo en la variable hexadecimal
    return dec_a_oct (decimal)#toma el numero convertido a decimal para transformarlo a octal

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////Funciones que encontradas para poder validar la entrada de datos ////////////////////////////////////////////////////////////////"""
# FUNCIONES NECESARIAS PARA VALIDAR LAS BASES DE LOS NÚMEROS INGRESADOS
# función para validar números binarios
def es_binario(n):
    return all(c in "01" for c in n)

# función para validar números decimales
def es_decimal(n):
    return n.isdigit()

# función para validar números octales
def es_octal(n):
    return all(c in "01234567" for c in n)

# función para validar números hexadecimales
def es_hexadecimal(n):
    return all(c.upper() in "0123456789ABCDEF" for c in n)

# FUNCIONES NECESARIAS PARA REALIZAR LOS CALCULOS ENTRE LOS NÚMEROS BINARIOS
# funcion para pedir dos numeros y controlar que sean binarios
def pedir_dos_binarios():
  num_bin_1 = input("Ingrese el primer número binario: ")
  while not es_binario(num_bin_1):
    num_bin_1 = input("No es binario. Intente de nuevo: ")

  num_bin_2 = input("Ingrese el segundo número binario: ")
  while not es_binario(num_bin_2):
    num_bin_2 = input("No es binario. Intente de nuevo: ")

  return num_bin_1, num_bin_2

# función para sumar dos numeros binarios
def suma_binarios():
  num_bin_1, num_bin_2 = pedir_dos_binarios()
  resultado_suma = bin_a_dec(num_bin_1) + bin_a_dec(num_bin_2)
  print(f"La suma binaria de {num_bin_1} + {num_bin_2} es: {dec_a_bin(resultado_suma)}")

# función para multiplicar dos numeros binarios
def multiplicacion_binarios():
  num_bin_1, num_bin_2 = pedir_dos_binarios()
  resultado_multiplicacion = bin_a_dec(num_bin_1) * bin_a_dec(num_bin_2)
  print(f"La multiplicación binaria de {num_bin_1} + {num_bin_2} es: {dec_a_bin(resultado_multiplicacion)}")

# función para restar dos numeros binarios
def resta_binarios():
  num_bin_1, num_bin_2 = pedir_dos_binarios()
  resultado_resta = bin_a_dec(num_bin_1) - bin_a_dec(num_bin_2)
  if resultado_resta < 0:
    print("La resta dio un número negativo. No se puede representar en binario con este método, requiere el uso de complemento a 2")
  else:
    print(f"La resta binaria de {num_bin_1} - {num_bin_2} es: {dec_a_bin(resultado_resta)}")

"""/////////////////////////////////////////////////////Menu y opciones principales///////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# FUNCIONES NECESARIAS PARA SEPARAR EL PROGRAMA EN SECCIONES
# utilizamos funciones que contengan esas secciones para llamarlas cuando
# el usuario decida ingresar en ellas
# FUNCIONES PARA GESTIONAR EL INGRESO Y SALIDA DE LAS SECCIONES
# función para el menú principal del programa
def menu_principal():
  opcion_elegida = " "
  while opcion_elegida not in ("1", "2", "3"):
    print("\nBienvenid@ al programa! \n¿Quieres usar el Conversor o la Calculadora Binaria?: \n1) Conversor \n2) Calculadora \n3) Salir del programa")
    opcion_elegida = input("Ingrese una opción para continuar: ")

    if opcion_elegida == "1":
      conversor()
    elif opcion_elegida == "2":
      calculadora()
    elif opcion_elegida == "3":
      print("¡Gracias por usar el programa!")
    else:
      print("Opción inválida. Intente nuevamente: ")
#SECCION CONVERSOR
#funcion para contener la seccion conversor
def conversor():
  #se le pide al usuario que ingrese una de las opciones
  print("\nBienvenid@ al conversor")
  opcion=input("Ingrese la opcion correspondiente al numero que desea convertir \n 1) Si es un números Binarios \n 2) Si es un números Decimales \n 3) Si es un números Octales \n 4) Si es un números Hexadecimales \n 5) Volver al menú principal \n ...  ")

  # en este bucle lo que se hace es contrastar las opcion, si es valida o no, si no lo es se repite hasta que lo sea
  while opcion not in ("1", "2", "3", "4", "5"):# aca uso una tupla.y el not in seria como decir: no esta ... es una negación
      opcion=input("Recuerde que debe ingresar la opcion correspondiente al numero que desea convertir \n 1) Si es un números Binarios \n 2) Si es un números Decimales \n 3) Si es un números Octales \n 4) Si es un números Hexadecimales \n 5) Volver al menú principal \n ...  ")
      if opcion not in ("1", "2", "3", "4", "5"):
          print ("Intente nuevamente ")
  #ahora si se pide al usuario el numero que desea convertir
  #numero=input("ingrese un numero: ")

  #esto es solo a modo de ejemplo, pero aca dependiendo de la primer opcion se muestra un cartel
  if opcion in ("1","2","3","4", "5"):# aca uso una tupla.
          if opcion == "1"  :
              numero=input("ingrese un numero Binario: ")
              while not es_binario(numero):
                  print("Dato incorrecto. Vuelva a intentar.")
                  numero = input("Ingrese un número Binario: ")
              binario= numero
              print(f"El Numero {numero} es Binario")
              print(f"El Numero en Decimal es: {bin_a_dec(binario)}")
              print(f"El Numero en Octal es: {bin_a_oct(binario)}")
              print(f"El Numero en Hexadecimal es: {bin_a_hex(binario)}")
              continuar("Conversor")
          elif opcion ==  "2"  :
              numero=input("ingrese un numero Decimal: ")
              while not es_decimal(numero):
                  print("Dato incorrecto. Vuelva a intentar.")
                  numero = input("Ingrese un número Decimal: ")
              decimal= int(numero)
              print(f"El Numero {numero} es decimal")
              print(f"El Numero en Binario es: {dec_a_bin(decimal)}")
              print(f"El Numero en Octal es: {dec_a_oct(decimal)}")
              print(f"El Numero en Hexadecimal es: {dec_a_hex(decimal)}")
              continuar("Conversor")
          elif opcion ==  "3"  :
              numero=input("ingrese un numero Octal: ")
              while not es_octal(numero):
                  print("Dato incorrecto. Vuelva a intentar.")
                  numero = input("Ingrese un número Octal: ")
              octal=numero
              print(f"El Numero {numero} es octal")
              print(f"El Numero en Binario es: {oct_a_bin(octal)}")
              print(f"El Numero en Decimal es: {oct_a_dec(octal)}")
              print(f"El Numero en Hexadecimal es: {oct_a_hex(octal)}")
              continuar("Conversor")
          elif opcion ==  "4"  :
              numero=input("ingrese un numero Hexadecimal: ")
              while not es_hexadecimal(numero):
                  print("Dato incorrecto. Vuelva a intentar.")
                  numero = input("Ingrese un número Hexadecimal: ")
              hexadecimal= numero
              print(f"El Numero {numero} es hexadecimal")
              print(f"El Numero en Binario es: {hex_a_bin(hexadecimal)}")
              print(f"El Numero en Decimal es: {hex_a_dec(hexadecimal)}")
              print(f"El Numero en Octal es: {hex_a_oct(hexadecimal)}")
              continuar("Conversor")
          elif opcion == "5":
              menu_principal()
  else :
          print("ingrese una opcion valida ")
#SECCION CALCULADORA
# función para contener la seccion Calculadora
def calculadora():
  operacion_elegida = " "
  # le ofrecemos al usuario la posibilidad de realizar otras operaciones
  while operacion_elegida not in ("1", "2", "3", "4"):
    print("\nBienvenid@ a la Calculadora Binaria: \n¿Qué operación binaria quieres realizar? \n1) Suma \n2) Resta \n3) Multiplicación \n4) Volver al menú principal")

    operacion_elegida = input("Por favor, elija una opción para continuar: ")

    # llamamos a la funcion que corresponda segun la eleccion del usuario
    if operacion_elegida == "1":
      suma_binarios()
      continuar("Calculadora")
    elif operacion_elegida == "2":
      resta_binarios()
      continuar("Calculadora")
    elif operacion_elegida == "3":
      multiplicacion_binarios()
      continuar("Calculadora")
    elif operacion_elegida == "4":
      menu_principal()
    else:
      print("La opción ingresada no es válida. Intente de nuevo: ")

"""////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

# función para preguntar al usuario como continuar
def continuar(seccion_actual):
  print(f"\n¿Quieres seguir trabajando en la sección actual: {seccion_actual}? \n1) Continuar en {seccion_actual} \n2) Volver al menú principal \n3) Salir del programa")
  opcion = input("Elige una opcion: ")

  while opcion not in ("1", "2", "3"):
    print(f"\n¿Quieres seguir trabajando en la sección actual: {seccion_actual}? \n1) Continuar en {seccion_actual} \n2) Volver al menú principal \n3) Salir del programa")
    opcion = input("Elige una opcion: ")

  if opcion == "1":
    if seccion_actual == "Conversor":
      conversor()
    elif seccion_actual == "Calculadora":
      calculadora()
  elif opcion == "2":
    menu_principal()
  elif opcion == "3":
    print("¡Gracias por usar el programa!")
  else:
      print("Opción inválida. Intente nuevamente: ")
# EJECUCIÓN DEL PROGRAMA
# llamamos a la funcion menu_principal para comenzar la ejecución del programa
menu_principal()