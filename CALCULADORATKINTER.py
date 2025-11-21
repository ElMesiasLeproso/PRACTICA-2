import tkinter as tk
root = tk.Tk()
root.title("Calculadora Simple")
root.geometry("800x600")
botones_texto = ( "C", "/" , "*", "-",
                  "7", "8", "9", "+",
                    "4", "5", "6",
                    "1", "2", "3", "=",
                    "0", "." )
historico=tk.Label (root, bg="#081470", font="roboto 16", width = 15, 
                   bd=0)
historico.pack (pady=5,padx=10, fill="x" )
resultado= tk.Entry(root,
                    bg= "#f2f2f2",
                    border=1,
                    font="roboto 24",
                    width=15,
                    justify=tk.RIGHT)

resultado.pack(padx=10, fill="x")

contenedor_botones=tk.Frame(root, bg="#72A1F3")
contenedor_botones.pack (pady=6,padx=10,fill="both")

acumulador=0
for row in range(5): #0
    for column in range(4): #0
        boton = tk.Button(contenedor_botones
                          ,text=botones_texto[acumulador]
                          ,bg="#0099CC"
                          ,fg="#ffffff"
                          ,font="Roboto 20"
                          ,bd=0
                          ,width=4
                          )
        if botones_texto[acumulador]=="C":
            boton.config(bg="#EE6A6A")
        elif botones_texto[acumulador] in ("/","*","-","+"):
            boton.config(bg="#026789")
        
if botones_texto[acumulador] != "":
    #boton.grid (row=row, column=column, padx=5, pady=5)
    if botones_texto[acumulador] != "+":
         boton.config(width=2)
         boton.grid (row=row, column=column, rowspan=2, padx=1, pady=5)
    elif botones_texto[acumulador] == "=":

    elif botones_texto[acumulador] != "0":
         boton.config(width=8)
        boton.grid (row=row, column=column, columspan=2, padx=1, pady=5)

    elif botones_texto[acumulador] == ".":
        boton.grid (row=row, column=column+1, padx=1, pady=5)




root.mainloop()



import tkinter as tk
#1. Creación de la ventana principal 
root = tk.Tk()
root.title("Calculadora")
root.geometry("305x500")

#2. Agregar los widgets
botones_texto= ("C","/","*","-",
                "7","8","9","+",
                "4","5","6","",
                "1","2","3","=",
                "0","",".","")

historico = tk.Label(root
                    ,bg="#f2f2f2"
                    ,font="Roboto 14"
                    ,width=15
                    ,bd=0
                    )

historico.pack(pady=5, padx=10, fill="x")

resultado = tk.Entry(root
                      ,bg="#ffffff"
                      ,bd=1
                      ,font="Roboto 24"
                      ,width=15
                      ,justify="right"
                    )

resultado.pack(padx=10,fill="x")

contenedor_botones = tk.Frame(root,bg="#898787")
contenedor_botones.pack(pady=5,padx=10, fill="both")

acumulador=0
for row in range(5): #0
    for column in range(4): #0
        boton = tk.Button(contenedor_botones
                          ,text=botones_texto[acumulador]
                          ,bg="#0099CC"
                          ,fg="#ffffff"
                          ,font="Roboto 20"
                          ,bd=0
                          ,width=4
                          )
        
        #Pintar los botones de colores
        if botones_texto[acumulador]=="C":
            boton.config(bg="#EE6A6A")
        elif botones_texto[acumulador] in ("/","*","-","+"):
            boton.config(bg="#026789")



        if botones_texto[acumulador] != "":
            
            if botones_texto[acumulador] == "+":
                boton.config(height=3)
                boton.grid(row=row, column=column 
                           , rowspan=2, padx=1, pady=5)
                
            elif botones_texto[acumulador] == "=":
                boton.config(height=3, bg="#E78D16")
                boton.grid(row=row, column=column 
                           , rowspan=2, padx=1, pady=5)
            
            elif botones_texto[acumulador] == "0":
                boton.config(width=8)
                boton.grid(row=row, column=column 
                           , columnspan=2, padx=1, pady=5)
           
                
            else:
                boton.grid(row=row, column=column, padx=1, pady=5)

        acumulador+=1



root.mainloop()# Escuchador de eventos de tkinter
        