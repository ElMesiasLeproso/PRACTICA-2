#requisito: inicio de programa
texto=input("Escribe un texto").lower()
#requisito: ingreso de 3 letras 1 x 1
letras=[]
for i in range(3):
    letra=input("Escribe una letra {i+1}").lower()
    letras.append(letra)
#requisito: conteo de letras
for letra in letras:
    contador=0
    for caracter in texto:
        if caracter==letra:
            contador+=1
    print(f"La letra {letra} se repite {contador} veces")
#requisito: conteo de palabras usando str
palabras=texto.split()
print(f"El texto tiene {len(palabras)} palabras")
#requisito: lentras de inicio y fin.
print(f"El texto inicia con {texto[0]} y termina con {texto[-1]}")
#requisito: texto invertido
print(f"El texto invertido es: {texto[::-1]}")
#requesito: busqueda de palabra "python"
if "python" in texto:
    print("La palabra 'python' se encuentra en el texto")
else:
    print("La palabra 'python' no se encuentra en el texto")

