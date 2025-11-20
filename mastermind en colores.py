#el juego generara un codigo secreto de 4 colores. el jugador tiene 8 intentos para adivinar la secuencia
#posicion correcta verde: el jugador adivnino un color correcto y esta en posicion correcta
#color incorrecto amarillo: el jugador adivino un color correcto pero esta en posicion incorrecta
from colorama import init, Fore, Style
import random
#1.configuracion de los colores del juego
COLORES_POSIBLES={
    "R": Fore.RED + "Ω" + Style.RESET_ALL,
    "G": Fore.GREEN + "Ω" + Style.RESET_ALL,
    "B": Fore.BLUE + "Ω" + Style.RESET_ALL, 
    "Y": Fore.YELLOW + "Ω" + Style.RESET_ALL,
    "N": Fore.BLACK + "Ω" + Style.RESET_ALL,
    "C": Fore.CYAN + "Ω" + Style.RESET_ALL,
    "M": Fore.MAGENTA + "Ω"+ Style.RESET_ALL,
    "W": Fore.WHITE + "Ω" + Style.RESET_ALL,
    }
LONGITUD_CODIGO=4
INTENTOS_MAXIMOS=8
#EJEMPLO: coords=(10,20,100,200), desempaquetado de tubplas: x1,y1,x2,y2=coords
def generar_codigo_secreto():
    colores=list(COLORES_POSIBLES.keys())
    codigo_secreto=[]
    for _ in range(LONGITUD_CODIGO):
        codigo_secreto.append(random.choice(colores))
    return codigo_secreto
def mostrar_colores():
    print("Colores disponibles:")
    for letra, color_formato in COLORES_POSIBLES():
        print(f" (letra): {color_formato}{Style.RESET_ALL}", end=" ")

def obtener_intento_jugador():
    mostrar_colores
    while True:
        intento=input(f"Ingrese su intento de {LONGITUD_CODIGO} colores (letras sin espacios): \n").upper() .strip()
        if len(intento)!=LONGITUD_CODIGO:
            print(f"Debe ingresar exactamente {LONGITUD_CODIGO} letras.")
            continue
        valido = True
        for letra in intento:
            if letra not in COLORES_POSIBLES:
                print(f"La letra '{letra}' no es un color valido.")
                valido=False
                continue
        if valido:
            return list(intento)
def evaluar_intento(intento, codigo_secreto):
    #evalua el intento y devuelve las pistas
    posicion_correcta=0
    color_correcto=0
    #listas para no contar los colores 2 veces
    intento_copia= list(intento)
    secreto_copia= list(codigo_secreto)
    #posicion correcta  (color verde)
    for i in range (LONGITUD_CODIGO-1,-1,-1):
        if intento_copia[i]==secreto_copia[i]:
            posicion_correcta +=1
            intento_copia.pop(i)
            secreto_copia.pop(i)

    #buscar colores correctos(color amarillo)
    for letra in intento_copia:
        if letra in secreto_copia:
            color_correcto +=1 
            secreto_copia.remove(letra)

    return posicion_correcta,color_correcto #posicion correcta color correcto

   # """
    #[o]=[[0]=pc]

def mostrar_tablero (intentos_pasados,pistas_pasadas):
    """Mostrar el Hirtorial de intentos con sus pistas"""
    print("\n--- tablero del juego---")
    for i in range ( len(intentos_pasados)) :
        intento_str=""
        for letras in intentos_pasados [i]:
            intento_str += COLORES_POSIBLES[letra] + Style.RESET_ALL+""
        #pistas
        pistas_str=(Fore.GREEN +
                    f"{pistas_pasadas[i][0]}P "
                    + Fore.YELLOW
                    + f"{pistas_pasadas[i][1]}C"
                    + Style.RESET_ALL
                    )


    print (f"intento {i+1}:{intento_str} | {pistas_str}")
    print("-"*20) 
    print("\n")

def jugar():
    init(autoreset=true) 

    print(fore.CYAN+Style.BRIGHT+"-"*40)
    print (fore.CYAN+Style.BRIGHT+"Bienvenidos a Mastermind de colores") 
    Print(fore.CYAN+Style.BRIGHT+"-"*40 + "\n")

    codigo_secreto = generar_codigo_secreto()

    intentos_restantes = INTENTOS_MAXIMOS
    intentos_pasados = []
    pistas_pasadas = []

    while intentos_restantes > 0:
        print (f"Te quedan {Fore.YELLOW+Style.BRIGHT}{intentos_restantes + Style.RESET_ALL} intentos")

        intento_actual = obtener_intento_jugador()

        pc , cc = evaluar_intento(intento_actual,codigo_secreto)

       #guardar el historial
       intentos pasados.append(intento_actual)
       pistas_pasadas.append((pc,cc))


       mostrar_tablero_(intentos_pasados,pistas_pasadas)

       if pc == LONGITUD_CODIGO:
        print(Fore.GREEN+Style.BRIGHT+"Felicidades, decifraste el codigo")
        break

        intentos_restantes -= 1

    if intentos_restantes = 0 :
        print(Fore.Red+Style.BRIGHT+"\n ¡Oh no, te quedaste sin intentos!")
        secreto_str = "" .join(codigo_secreto)
        print (f"El codigo secreto era"+ secreto_str)

jugar ()
        









