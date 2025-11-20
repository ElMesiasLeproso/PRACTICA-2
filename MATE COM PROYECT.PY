import secrets
import string

def generar_contraseña(longitud=12):
    letras = string.ascii_letters
    dígitos = string.digits
    especiales = string.punctuation
    alfabeto = letras + dígitos + especiales

    while True:
        contraseña = ''.join(secrets.choice(alfabeto) for i in range(longitud))
        if (any(c in string.ascii_lowercase for c in contraseña)
            and any(c in string.ascii_uppercase for c in contraseña)
            and any(c in dígitos for c in contraseña)
            and any(c in especiales for c in contraseña)):
            return contraseña

print(generar_contraseña(16))

def criba_eratostenes(n):
    if n < 2:
        print("No hay números primos menores que 2.")
        return
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False
    lista_primos = [i for i, es_primo in enumerate(primos) if es_primo]
    print(f"Números primos menores o iguales a {n}: {lista_primos}")

while True:
    opcion = input("¿Deseas generar la criba de Eratóstenes? (si/no): ").lower()
    if opcion == "no":
        print("Adiós")
        break
    elif opcion == "si":
        try:
            n = int(input("Ingresa un número entero positivo: "))
            criba_eratostenes(n)
        except ValueError:
            print("Por favor, ingresa un número válido.")




import math

def calcular_mcd(a, b):
    return math.gcd(a, b)

def calcular_mcm(a, b):
    return abs(a * b) // calcular_mcd(a, b)

a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))

#maximo común divisor
print(f"MCD({a}, {b}) = {calcular_mcd(a, b)}") 
#mínimo común múltiplo
print(f"MCM({a}, {b}) = {calcular_mcm(a, b)}") 
