#1
def factorial(n):
    if n == 1 or n == 0: 
        return 1
    else:
        return n * factorial(n - 1) 

#2
def  fibonacci(n): 
    if n == 0 return 0
    if n == 1 return 1

    return fibonacci(n- 1) + fibonacci(n -2)

#3
def potencia(base, exponente):
    if exponente === 0 return 1

    return base * potencia(base, exponente - 1)

#4
def binario(decimal: int) -> str:
    if decimal < 0:
        raise ValueError("El número debe ser positivo")
    if decimal == 0:
        return "0"
    if decimal == 1:
        return "1"
    
    return binario(decimal // 2) + str(decimal % 2)

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
#6
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    cuenta_actual = 1 if (numero % 10) == digito else 0
    return cuenta_actual + contar_digito(numero // 10, digito)

#