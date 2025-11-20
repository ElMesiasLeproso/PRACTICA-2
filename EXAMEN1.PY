# examen_control_flujo.py
#Elaborado con apoyo de COPILOT9987
#Primero indicamos def para definir la primera funcion, mostrandonos en primer lugar las preguntas y opciones que definiremos mas adelante.
#Con for indicamos imprimir las opciones de respuesta sin usar print 4 veces
def mostrar_pregunta(pregunta, opciones):
    print(pregunta)
    for opcion in opciones:
        print(opcion)
#Luego indicamos la segunda funcione def para la respuesta valida, usando while true para indicar que la entrada de la respuesta sea valida. 
# if respuesta para indicar la respuesta dentro del rango a,b,c,d. Luego indicamos la devolucion de la respuesta con return. 
# Else para imprimir cuando la respuesta no es valida

def respuestavalida():
    while True:
        respuesta = input("Tu respuesta (A/B/C/D): ")
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        else:
            print("Respuesta inválida. Por favor ingresa A, B, C o D.")
#Con la tercera funcion def evaluar respuesta, comparamos la respuesta que el aplicante ingreso y la que registramos como correcta
#Si la respuesta del usuario es correcta, sumara uno, si no, sera cero.
''
def evaluar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario == respuesta_correcta:
        print(" ¡Correcto!\n")
        return 1
    else:
        print(f" Incorrecto. La respuesta correcta era: {respuesta_correcta}\n")
        return 0
# La cuarta funcion def establece el inicio del examen haciendo la cuenta de los puntos, iniciando en 0 y creando un contador i en cero
#mientras while recorre las preguntas mientras el numero de preguntas sea mayor de el contador
#se extrae la pregunta usando el indice i
#se muestra la pregunta y las opciones
#y evalua si la respuesta es valida, sumando uno si se da el acierto
def ejecutar_examen(preguntas):
    puntaje = 0
    i = 0
    while i < len(preguntas):
        pregunta = preguntas[i]
        mostrar_pregunta(pregunta["texto"], pregunta["opciones"])
        respuesta_usuario = respuestavalida()
        puntaje += evaluar_respuesta(respuesta_usuario, pregunta["respuesta_correcta"])
        i += 1
#al final impriminos la informacion del puntuaje optenido de las preguntas
#if evalua si el total de puntos es igual al total de preguntas, entonces felicita al aspirante por la exelencia
#elif mientras el puntuaje sea mayor de 7 nos imprime que pasamos el examen
#else queda para las otras opciones de resultado, dando un reprobatorio
    print(f"\nTu calificacion final es: {puntaje} de {len(preguntas)}")
    if puntaje == len(preguntas):
        print(" ¡Perfecto! Has respondido todo correctamente.")
    elif puntaje >= 7:
        print(" ¡Buen trabajo! Has aprobado el examen.")
    else:
        print(" No has aprobado. ¡Sigue practicando!")

# Lista de preguntas y respuestas 
preguntas = [
    {
        "texto": "1. ¿Qué estructura de control es más adecuada para iterar sobre una secuencia de elementos un número de veces conocido de antemano?",
        "opciones": ["A) Bucle “para”", "B) Sentencia condicional “Si”", "C) Bucle “repetir”", "D) Bucle “mientras”"],
        "respuesta_correcta": "A"
    },
    {
        "texto": "2. ¿Qué es un algoritmo?",
        "opciones": ["A) Un conjunto de instrucciones escritas en código binario.",
                     "B) Un lenguaje de programación específico.",
                     "C) El código fuente de un programa de computadora.",
                     "D) Una secuencia de pasos finitos y bien definidos para resolver un problema."],
        "respuesta_correcta": "D"
    },
    {
        "texto": "3. El lenguaje máquina está compuesto por:",
        "opciones": ["A) Símbolos lógicos y matemáticos", "B) Pseudocódigo", "C) Instrucciones en inglés abreviado", "D) Código binario"],
        "respuesta_correcta": "D"
    },
    {
        "texto": "4. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?",
        "opciones": ["A) Sistema de entrada/salida", "B) CPU", "C) Tarjeta gráfica", "D) Memoria principal"],
        "respuesta_correcta": "C"
    },
    {
        "texto": "5. Un lenguaje de programación de alto nivel se caracteriza por:",
        "opciones": ["A) Ser muy difícil de aprender y leer.",
                     "B) Ser el más rápido en tiempo de ejecución.",
                     "C) Tener un control directo y preciso sobre el hardware.",
                     "D) Ser independiente de la arquitectura de la computadora."],
        "respuesta_correcta": "D"
    },
    {
        "texto": "6. El lenguaje Java es considerado un lenguaje de nivel...",
        "opciones": ["A) Bajo", "B) Muy alto", "C) Medio", "D) Alto"],
        "respuesta_correcta": "D"
    },
    {
        "texto": "7. Un programa de computadora es esencialmente:",
        "opciones": ["A) Una colección de algoritmos.",
                     "B) El sistema operativo de una computadora.",
                     "C) Un dispositivo de hardware.",
                     "D) Una secuencia de instrucciones que la computadora ejecuta."],
        "respuesta_correcta": "D"
    },
    {
        "texto": "8. En pseudocódigo, ¿qué estructura de control se utiliza para ejecutar un bloque de código solo si se cumple una condición específica?",
        "opciones": ["A) Condicional o de selección", "B) Repetitiva “para”", "C) Secuencial", "D) Repetitiva “mientras”"],
        "respuesta_correcta": "A"
    },
    {
        "texto": "9. El propósito principal del pseudocódigo es:",
        "opciones": ["A) Traducir automáticamente código de alto nivel a lenguaje máquina.",
                     "B) Ejecutar programas de forma más eficiente que un lenguaje compilado.",
                     "C) Plantear y describir la lógica de un algoritmo de forma legible para los humanos.",
                     "D) Proporcionar un control directo sobre los registros del procesador."],
        "respuesta_correcta": "C"
    },
    {
        "texto": "10. ¿Cuál es la principal diferencia entre un bucle “mientras” (while) y un bucle “repetir” (do-while)?",
        "opciones": ["A) El bucle “mientras” puede no ejecutarse, mientras que el “repetir” se ejecuta al menos una vez.",
                     "B) No hay ninguna diferencia, son intercambiables.",
                     "C) El bucle “mientras” es más rápido que el “repetir”.",
                     "D) El bucle “repetir” solo usa números, mientras que el “mientras” puede usar cualquier condición."],
        "respuesta_correcta": "A"
    }
]

# Punto de entrada
if __name__ == "__main__":
    ejecutar_examen(preguntas)



