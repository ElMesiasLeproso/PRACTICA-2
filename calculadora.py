def  sumar  ( n1, n2 ):
    return n1+n2
def resta (n1,n2):
    return n1-n2
def multiplicar (n1,n2):
    return n1*n2
def dividir (n1,n2):
    return n1/n2
while True:
    print ("Selecciona operacion")
    print ("1. sumar +")
    print ("2. resta -")
    print ("3. multiplicar *")
    print ("4. dividir /")
    print ("5. Salir")
    opcion= input ("Ingresa opcion (1/2/3/4/5): ")
    if opcion == "5":
        break
    try:
        n1=float(input("Ingresa primer numero: "))
        n2=float(input("Ingresa segundo numero: "))
    except ValueError:
        print("Entrada invalida. Por favor ingresa numeros.")
        continue
    if opcion == "1":
        print(n1,"+",n2,"=",sumar(n1,n2))
    elif opcion == "2":
        print(n1,"-",n2,"=",resta(n1,n2))
    elif opcion == "3":
        print(n1,"*",n2,"=",multiplicar(n1,n2))
    elif opcion == "4":
        if n2 == 0:
            print("Error: Division por cero no es permitida.")
        else:
            print(n1,"/",n2,"=",dividir(n1,n2)) 
