
def oraculo_iniciado():
    while True:
        opcion=input("Desea conocer su destino?(si/no)").lower()
        if opcion=="no":
            print ("Adios")
            break
        nombre=input("Escribe tu nombre")
        año=int(input("Escribe tu año de nacimiento")) 
        num_Suerte=int(input("Escribe un numero del 1 al 4"))
        edad=2025-año
        elemento=calcul_elemet(año)
        prediccion=generar_prediccion(nombre, elemento, num_Suerte)
        decorador="*"*5
        for i in range(5):
            print(decorador)
        print("EL ORACULO DE PYTHON")
        print(prediccion)
def calcul_elemet(año):
    match (año%10):
        case 0 | 1: return "Tu color de la suerte es azul" 
        case 2 | 3:return   "Tu color de la suerte es rojo"
        case 4 | 5:return   "Tu color de la suerte es verde"
        case 6 | 7:return   "Tu color de la suerte es blanco"
        case  8| 9:return   "Tu color de la suerte es cafe"
def generar_prediccion(nombre, elemento, num_Suerte):
    match num_Suerte:
        case 1: return f"{nombre}, este año tendras mucho exito en el trabajo. {elemento}"
        case 2: return f"{nombre}, este año encontraras el amor de tu vida. {elemento}"
        case 3: return f"{nombre}, este año viajaras a lugares increibles.  {elemento}"
        case 4: return f"{nombre}, este año tendras buena salud. {elemento}"
        case _: return "Numero de la suerte invalido. Debe ser entre 1 y 4."    
        
oraculo_iniciado()





