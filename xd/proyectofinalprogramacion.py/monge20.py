import pandas
from pandas import Series
import matplotlib.pyplot as plt
from colorama import Style, Fore,Back,init
from modulospros import empleados
import os
trabajdores='trabajadoressuid.csv'
stocksito='iostockinventar.csv'
df=pandas.read_csv(stocksito)
if os.path.exists(trabajdores):
    df_temp = pandas.read_csv(trabajdores, index_col=0, dtype=str)
    trabajadores_uid = df_temp.to_dict(orient='index')
    trabajadores_uid_limpio = {}
    for uid, datos in trabajadores_uid.items():
        # Fuerza que el uid sea una cadena de texto str
        uid_str = str(uid).strip() 
        # Si tienes valores sin nada, esta línea los limpia.
        #el K es un notahumber que es para que los espacios en vacio no sean una limitante
        # y el V es para evitar que sea un caracter 
        datos_limpios = {k: v for k, v in datos.items() if pandas.notna(v) and v is not None}
        trabajadores_uid_limpio[uid_str] = datos_limpios
        
    trabajadores_uid = trabajadores_uid_limpio
def entrada_trabajador():
    mostrar_titulo()
    uid_entrada=input(Fore.WHITE+"            ingresa tu uid :"+Style.RESET_ALL).strip()
    uid_entrada_str=str(uid_entrada)
    #se manda en str para manejarlo asi en nuestro archivo csv
    if uid_entrada=="171007":
        mostrar_titulo()
        mostrar_menu_administrador()
    elif uid_entrada_str in trabajadores_uid:
        mostrar_titulo()
        nombre_empleado = trabajadores_uid.get(uid_entrada_str, {}).get('nombre', 'Usuario')
        print(Fore.GREEN+Style.BRIGHT+f"                   Bienvenido {nombre_empleado}"+Style.RESET_ALL)
        mostrar_menu()
    else:
            print(Fore.RED+"ingrese un UID valido"+Style.RESET_ALL)
            entrada_trabajador()
verduras_venta=0
carne_vetas=0
jugo_venta=0
lacteos_ventas=0
abarrotes_ventas=0
limpieza_venta=0
venta_turno=0
def mostrar_titulo():
    print(Fore.WHITE+"Bienvenido a nuestra tienda favorita y de nuestros clientes"+Style.RESET_ALL)
    print(Fore.RED+Style.BRIGHT+"                   HUEVOS CORP                       "+ Style.RESET_ALL)
def venta_producto():
    yn=input("deseas vender? ").lower()
    cuuenta=0
    ticket=""
    global verduras_venta, carne_vetas, jugo_venta, lacteos_ventas, abarrotes_ventas, limpieza_venta, venta_turno, df
    while yn=="si":
        print(Fore.WHITE+Style.BRIGHT+"""
            -------CATEGORIAS---------
            Verdura
            carne
            jugo
            lacteos
            abarrotes
            limpieza"""+Style.RESET_ALL)
        categoria_a_vender=input(Fore.BLACK+Style.BRIGHT+"           que seas vender: "+Style.RESET_ALL).capitalize()
        print(df[df['categoria'] == categoria_a_vender])
        porducto_a_vender=input("que producto deseas vender: ").title()
        if porducto_a_vender in df['producto'].values:
            cuanto_producto_venderas=int(input("cuanto vas a vende: "))
            stock_de_producto_a_vender=df.loc[df['producto'] == porducto_a_vender, 'stock'].values[0]
            #aqui busca el producto y  busca que haya producto
            if cuanto_producto_venderas>stock_de_producto_a_vender:
                print("invalido no se puede hay menos producto del solicitado: ")
                yn=input("quieres seguir? ")
            elif cuanto_producto_venderas==0:
                print("ingrese un valor valido")
                yn=input("quieres seguir? ")
            else:
                print(Fore.GREEN+Style.BRIGHT+"----------SE HA COMPLETADO TU COMPRA-------------"+Style.RESET_ALL)
                df.loc[df['producto'] == porducto_a_vender, 'stock'] -= cuanto_producto_venderas
                #aqui se le reduce el stock al producto
                df.to_csv('iostockinventar.csv', index=False)
                #aqui guarda eso en el archivo de csv
                stock_producto = df.loc[df['producto']==porducto_a_vender,'stock'].values[0]
                ticket += f"{porducto_a_vender} - Cantidad: {cuanto_producto_venderas}\n"
                #aqui se va creando el ticket del cliente
                precio_unitario = df.loc[df['producto'] == porducto_a_vender, 'precios'].values[0]
                #se le da el valor del producto a esta variable
                total = precio_unitario * cuanto_producto_venderas
                cuuenta+=total
                if categoria_a_vender == 'Verdura':
                    verduras_venta += total
                elif categoria_a_vender == 'Carne':
                    carne_vetas += total
                elif categoria_a_vender == 'Jugo':
                    jugo_venta += total
                elif categoria_a_vender == 'lacteos':
                    lacteos_ventas += total
                elif categoria_a_vender == 'Abarrotes':
                    abarrotes_ventas += total
                elif categoria_a_vender == 'Limpieza':
                    limpieza_venta += total
                print(Fore.GREEN+Style.BRIGHT+ticket)
                yn=input("quieres seguir? ")
                venta_turno+=1
        else:
            print("producto invalido")
    print(Fore.BLUE+f"tu cuenta total fue: {cuuenta}"+Style.RESET_ALL)      
    print(Fore.WHITE+Style.BRIGHT+f"tu ticket fue {ticket}"+Style.RESET_ALL)
    iva=cuuenta*1.16
    print(f"tu iva fue de {iva}")
def agregar_stock():
    print(df['producto'])
    producto_agregar_stock=input("A que producto deseas agregar?: ").strip().title()
    if producto_agregar_stock in df['producto'].values:
        #verifica si esta el producto en stock (me pegue un tiro en hacerlo por que no leia el archivo csv)
        cuant_desea_agregar=input("cuanto stock agregar? (no letras) ")
        abecedario=("qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM")
        try:
            #el try hace que se haga la funcion pero si da error entra el except value error, el cual si este da error 
            #automaticamnete da un mensaje 
            cuant_desea_agregar = int(cuant_desea_agregar)
            if cuant_desea_agregar > 0:
                print(df['producto'])
                #verificar si es mayor
                df.loc[df['producto'] == producto_agregar_stock, 'stock'] += cuant_desea_agregar
                df.to_csv('iostockinventar.csv', index=False)
                #aqui lo guarda en el archivo csv
                stock_producto = df.loc[df['producto'] == producto_agregar_stock, 'stock'].values[0]
                #a una variable se le da el stock actualizado del producto like booss
                print("-"*60)
                print(Fore.GREEN+Style.BRIGHT+"              SE HA AGREGADO EL PRODUCTO"+Style.RESET_ALL)
                print(f"Stock actualizado Nuevo stock de {producto_agregar_stock} es: {stock_producto}")
            else:
                print(" La cantidad debe ser mayor que cero.")
                agregar_stock()
        except ValueError:
            print(Fore.RED+Style.BRIGHT+"-------------ingrese solo números enteros--------------"+Style.RESET_ALL)
            agregar_stock()
    else:
        print(Fore.RED+Style.BRIGHT+"Producto no encontrado"+Style.RESET_ALL)
        agregar_stock()
def graficar_stock_productos():
    print("Generando gráfica de stock por producto...")
    plt.figure(figsize=(12, 8))
    plt.bar(df['producto'], df['stock'], color='skyblue')
    #se crea una grafica en base al producto y su stock
    plt.title('Inventario de Stock por Producto', fontsize=16)
    #titulo
    plt.ylabel('Cantidad en Stock')
    #lateral en y
    plt.xlabel('Productos')
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def graficar_por_categoria_venta():
    print("Generando gráfica de ventas totales por categoría...")
    categorias = ['Verduras', 'Carne', 'Jugo', 'Lácteos', 'Abarrotes', 'Limpieza']
    totales_ventas = (
        lacteos_ventas,
        verduras_venta,
        carne_vetas,
        jugo_venta,
        abarrotes_ventas,
        limpieza_venta
    )
    if sum(totales_ventas) == 0:
        print(Fore.YELLOW + "Aún no hay ventas para graficar." + Style.RESET_ALL)
        return
    plt.figure(figsize=(10, 6))
    colores = ['#4CAF50', '#FF5722', '#FFC107', '#03A9F4', '#9C27B0', '#795548']
    plt.bar(categorias, totales_ventas, color=colores)
    plt.title('Ventas Totales ($) por Categoría', fontsize=16)
    plt.ylabel('Total Vendido ($)')
    plt.xlabel('Categoría')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def mostrar_menu():
      while True:
        mostrar_titulo()
        print("-"*60)
        print(Fore.WHITE + Style.BRIGHT + "                   MENU DE OPCIONES")
        print("""
              1. Mostrar productos
              2. Mostrar precios por producto
              3. Venta de producto
              4. Agregar producto (stock)
              5. Gráfica de stock de producto
              6. Gráfica de venta por categoría
              7. Terminar tu turno
              8.cambiar usuario
              """)
        opcion = input(Fore.WHITE+Style.BRIGHT+"¿Qué opción deseas hacer?: "+Style.RESET_ALL)
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            mostrar_precio()
        elif opcion == "3":
            venta_producto()
        elif opcion == "4":
            filtro_para_agregar_stock=int(input(Fore.CYAN+"Ingrese el UID del Administrador para continuar:"+Style.RESET_ALL))
            if filtro_para_agregar_stock==171007:
                agregar_stock()
            else:
                print(Fore.RED+Style.BRIGHT+"-----BUSQUE AL ADMIN---------")
        elif opcion == "5":
            graficar_stock_productos()
        elif opcion == "6":
            graficar_por_categoria_venta()
        elif opcion == "7":
            terminar_turno()
            break 
        elif opcion=="8":
            cambiar_de_usuario()
        else:
            print(Fore.RED + "Opción inválida. Por favor, elige un número del 1 al 7.")
        input(Fore.MAGENTA + "\nPresiona espacio para continuar ")
def terminar_turno():
       print("--------------terminastes tu turno-------------")
       print(f"tus ventas fueron {venta_turno}")
       print(Fore.BLACK+"-"*40+Style.RESET_ALL)
def mostrar_menu_administrador():
    while True:
        
        print("-"*60)
        print(Fore.WHITE + Style.BRIGHT + "                   MENU DE OPCIONES")
        print("""
              1. Mostrar productos
              2. Mostrar precios por producto
              3. Venta de producto
              4. Agregar producto (stock)
              5. Gráfica de stock de producto
              6. Gráfica de venta por categoría
              7.eliminar empleado
              8.agregar nuevo empleado
              9. Terminar tu turno
              10.cambiar usuario
              11.agregar nuevo producto
              """)
        opcion = input("¿Qué opción deseas hacer?: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            mostrar_precio()
        elif opcion == "3":
            venta_producto()
        elif opcion == "4":
            agregar_stock()
        elif opcion == "5":
            graficar_stock_productos()
        elif opcion == "6":
            graficar_por_categoria_venta()
        elif opcion=="7":
            empleados.eliminar_nuevo_empleado()
        elif opcion=="8":
            empleados.agregar_nuevo_empleado()
        elif opcion == "9":
            terminar_turno()
            break 
        elif opcion=="10":
            cambiar_de_usuario()
        elif opcion=="11":
            agregar_nuevo_producto()
        else:
            print(Fore.RED + "Opción inválida. Por favor, elige un número del 1 al 7.")
        input(Fore.MAGENTA + "\nPresiona espacio para continuar...")
def cambiar_de_usuario():
    entrada_trabajador()
def mostrar_productos():
    print(df[['producto','stock']])
def mostrar_precio():
    print(df[['producto','precios']])
def agregar_nuevo_producto():
    global df
    
    print(Fore.BLUE+"         AGREGAR UN NUEVO PRODUCTO            ")
    nombre_del_nuevo_producto=input("Ingresa el nombre del nuevo producto: ")
    if nombre_del_nuevo_producto in df["producto"].values :
        print(Fore.RED+Style.BRIGHT+" ESTE PRODUCTO YA ESTA ")
        return
    print
    print(Fore.GREEN+"                CATEGORIAS DISPONIBLES"+Style.RESET_ALL)
    print(Fore.GREEN+"  Verdura | Carne | Jugo | Lacteos | Abarrotes | Limpieza"+Style.RESET_ALL)
    categoria=input("ingrese su categoria: ")
    try:
        precio = float(input("Ingresa el precio: "))
        stock = int(input("Ingresa el stock inicial: "))
        if precio <= 0 or stock < 0:
            print(Fore.RED + "El precio debe ser positivo y el stock no puede ser negativo." + Style.RESET_ALL)
            return
    except ValueError:
        print(Fore.RED + "Error: Asegúrate de ingresar números válidos para precio y stock." + Style.RESET_ALL)
        return

    nuevo_registro = pandas.DataFrame({
            'producto': [nombre_del_nuevo_producto], 
            'categoria': [categoria],               
            'stock': [stock],                      
            'precios': [precio]                     
        })
    #crear una lista del producto
    
    df = pandas.concat([df, nuevo_registro], ignore_index=True)
    df.to_csv('iostockinventar.csv', index=False)
    #el index es para evitar el 0 en el archivo y el concat es para concatenar
entrada_trabajador()