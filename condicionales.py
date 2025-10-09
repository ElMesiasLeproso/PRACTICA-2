#if else elif
edad = 25   #int (input("dime tu edad"))

if edad >= 10 and edad < 18:
    print("eres un adolecente.")
elif edad >= 18:
    print("eres un adulto")
    print("tienes que trabajar")
else:
    print("todavia eres un niño")

    #match



 opcion = int (input("""
                      1. Agregar
2. Editar
3. Elimnar 
4. Leer
5. Finalizar                                                                    
"""))
    
match opcion :
    case 1:
        print("se ha agregado correctamente")
    case 2:
        print("Se ha modificado correctamente")    
    case 3:
        print("Se ha eliminado correctamente")
    case 4:
        print("El usuario se llama Alejandro")
    case 5:
        print("Se finalizara el programa")

    