import tkinter as tk
from tkinter import ttk #themed Tkinter

#4 DEFINIR FUNCIONES DE EVENTOS (SI LAS HAY)
def saludar():
    etiqueta2.config(text=f"Hola {entrada_texto.get()}") #cambiar el texto de la etiqueta



#1 creamos la ventana
root = tk.Tk()
root.title("Mi primera ventana (RAIZ) con Tkinter")
root.geometry("400x300") #ancho x alto

#2. creamos los windgets
#ponemos los windgets dentro de la ventana
# ttk.Label
# ttk.Button
# ttk.entry
#crear un widgets widget=ttk.Widget(tipo de widget, parametros)
#importante insertar gestor de layouts:
#pack()apila uno sobre otro, 
#grid()organiza en cuadricula, 
#place()control sobre las coordenadas
etiqueta = tk.Label(root, text="Hola, soy una etiqueta", font="Arial 24") #etiqueta de texto que no interactua

etiqueta.grid(row=0, column=1, padx=10, pady=20) #empaquetar el widget en la ventana0, 

entrada_texto = ttk.Entry(root,font="Arial 20") #campo de texto para entrada de datos

entrada_texto.grid(row=1, column=1, padx=10, pady=20) #empaquetar el widget en la ventana

boton = ttk.Button(root, text="esto es un boton", command=saludar) #boton interactivo
#tambien se puede boton.config(command=funcion) para asignar la funcion despues

etiqueta2=ttk.Button(root) #boton interactivo
etiqueta2.grid(row=4, column=1, padx=10, pady=20)

boton.grid(row=2, column=1, padx=10, pady=20) #empaquetar el widget en la ventana

check=ttk.Checkbutton(root, text="Aceptar terminos y condiciones") #checkbox
check.grid(row=3, column=0, padx=10, pady=20) #empaquetar el widget en la ventana
opcion= tk.StringVar() #variable para radiobutton
opcion.set("Rojo")
r1=ttk.Radiobutton(root, text="Rojo",variable=opcion, value="Rojo" )#radiobutton
r2=ttk.Radiobutton(root, text="Azul",variable=opcion, value="Azul" ) #radiobutton
r3=ttk.Radiobutton(root, text="Verde",variable=opcion,value="Verde" ) #radiobutton
r1.grid(row=3, column=1, padx=10, pady=20) #empaquetar el widget en la ventana
r2.grid(row=3, column=2, padx=10, pady=20) #empaquetar el widget en la ventana
r3.grid(row=3, column=3, padx=10, pady=20) #empaquetar el widget en la ventana

#3. al final ordenamos mantener la ventana
root.mainloop() #mantener activa y escuchando la ventana hasta que se cierre , simepre va al final
