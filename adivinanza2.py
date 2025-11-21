import tkinter as tk
from tkinter import messagebox

# Funciones matemáticas
def mcd_fuerza_bruta(a, b):
    min_ab = min(abs(a), abs(b))
    for i in range(min_ab, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def mcd_euclides(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def mcd_euclides_recursivo(a, b):
    if b == 0:
        return abs(a)
    return mcd_euclides_recursivo(b, a % b)

def mcm(a, b):
    return abs(a * b) // mcd_euclides(a, b)

# Función que se ejecuta al presionar el botón
def calcular():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        resultado = (
            f"MCD Fuerza Bruta: {mcd_fuerza_bruta(a, b)}\n"
            f"MCD Euclides Iterativo: {mcd_euclides(a, b)}\n"
            f"MCD Euclides Recursivo: {mcd_euclides_recursivo(a, b)}\n"
            f"MCM: {mcm(a, b)}"
        )
        resultado_label.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números enteros válidos.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de MCD y MCM")
ventana.geometry("400x300")

tk.Label(ventana, text="Primer número:").pack()
entry_a = tk.Entry(ventana)
entry_a.pack()

tk.Label(ventana, text="Segundo número:").pack()
entry_b = tk.Entry(ventana)
entry_b.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

resultado_label = tk.Label(ventana, text="", justify="left")
resultado_label.pack()

ventana.mainloop()

import tkinter as tk
from tkinter import messagebox
from random import randint

# Inicialización del juego

from random import choice

def primos_criba(hasta=100):
    es_primo = [True] * (hasta + 1)
    es_primo[0:2] = [False, False]  # 0 y 1 no son primos
    for i in range(2, int(hasta**0.5) + 1):
        if es_primo[i]:
            for j in range(i*i, hasta + 1, i):
                es_primo[j] = False
    return [i for i, primo in enumerate(es_primo) if primo]

def generar_primo_aleatorio(hasta=100):
    primos = primos_criba(hasta=100)
    return choice(primos)

# Inicialización del juego
secreto = generar_primo_aleatorio (100)
intentos = 0





def verificar():
    global intentos, secreto
    try:
        intento = int(entry_intento.get())
        intentos += 1
        if intento == secreto:
            messagebox.showinfo("¡Correcto!", f"¡Lo lograste en {intentos} intentos!")
            reiniciar()
        else:
            pista = "mayor" if intento < secreto else "menor"
            rango_min = max(1, secreto - (10 if secreto > 10 else secreto - 1))
            rango_max = min(100, secreto + (10 if secreto < 91 else 100 - secreto))
            pista_label.config(text=f"Incorrecto... prueba un número {pista}. Pista: entre {rango_min} y {rango_max}")
    except ValueError:
        messagebox.showerror("Error", "Introduce un número entero válido.")

def reiniciar():
    global secreto, intentos
    secreto = generar_primo_aleatorio(100)
    intentos = 0
    pista_label.config(text="Nuevo juego iniciado. ¡Adivina el número!")
    entry_intento.delete(0, tk.END)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Juego: Adivina el número")
ventana.geometry("400x200")

tk.Label(ventana, text="Adivina el número entre 1 y 100").pack(pady=5)

entry_intento = tk.Entry(ventana)
entry_intento.pack()

tk.Button(ventana, text="Verificar", command=verificar).pack(pady=5)

pista_label = tk.Label(ventana, text="¡Buena suerte!", wraplength=380)
pista_label.pack(pady=10)

ventana.mainloop()