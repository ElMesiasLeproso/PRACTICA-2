# MCD fuerza bruta
def mcd_fuerza_bruta(a, b):
    min_ab = min(abs(a), abs(b))
    for i in range(min_ab, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# MCD algoritmo de Euclides (iterativo)
def mcd_euclides(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

# MCD algoritmo de Euclides (recursivo)
def mcd_euclides_recursivo(a, b):
    if b == 0:
        return abs(a)
    return mcd_euclides_recursivo(b, a % b)

# MCM usando MCD (con round por si acaso)
def mcm(a, b):
    return abs(a * b) // mcd_euclides(a, b)

# Pequeño menú para probar los algoritmos
def menu():
    print("Calculadora de MCD y MCM")
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    
    print(f"MCD Fuerza Bruta: {mcd_fuerza_bruta(a, b)}")
    print(f"MCD Euclides Iterativo: {mcd_euclides(a, b)}")
    print(f"MCD Euclides Recursivo: {mcd_euclides_recursivo(a, b)}")
    print(f"MCM: {mcm(a, b)}")

# Juego ejemplo: adivina el número usando max, min y round para mostrar pistas
def juego_adivina():
    from random import randint
    secreto = randint(1, 100)
    intentos = 0
    print("Adivina el número entre 1 y 100")
    while True:
        intento = int(input("Tu intento: "))
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            break
        else:
            pista = "mayor" if intento < secreto else "menor"
            # Uso de max/min
            rango_min = max(1, secreto - (10 if secreto > 10 else secreto - 1))
            rango_max = min(100, secreto + (10 if secreto < 91 else 100 - secreto))
            print(f"Incorrecto... prueba un número {pista}. (Pista: está entre {rango_min} y {rango_max})")

# Puedes elegir probar el menú matemático o el juego
if __name__ == "__main__":
    print("1. Calcular MCD y MCM")
    print("2. Jugar a adivinar el número")
    opcion = input("Selecciona una opción (1/2): ")
    if opcion == "1":
        menu()
    elif opcion == "2":
        juego_adivina()
    else:
        print("Opción no válida.")
