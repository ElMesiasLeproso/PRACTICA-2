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
