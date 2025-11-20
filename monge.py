from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from colorama import Style, Fore,Back,init
trabajadores_uid={
      '0321':{
            'nombre':'Omar'},
      '8149':{
            'nombre':'Monge'},
      '281818':{
            'nombre':'Isaias'},
      '171007':{
            'nombre':'Akzel'}
}
stock = {
    'producto': [
        'Tomate', 'Cebolla Blanca', 'Lechuga', 'Papa', 'Zanahoria', 'Brócoli',
        'Pechuga de Pollo', 'Carne Molida', 'Bistec de Res', 'Chuleta de Cerdo', 'Salmón',
        'Jugo de Naranja', 'Jugo de Manzana', 'Jugo de Uva',
        'Leche Entera', 'Queso', 'Yogurt Natural', 'Mantequilla', 'Crema',
        'Arroz', 'Frijoles Negros', 'Atún', 'Aceite Vegetal', 'Pasta', 'Azúcar', 'Sal',
        'Jabón de trastes', 'Cloro', 'Limpiador de Pisos', 'Servilletas'
    ],
    'stock': [
        150, 200, 80, 300, 120, 60,
        50, 40, 30, 35, 20,
        90, 70, 65,
        100, 80, 75, 50, 60,
        200, 150, 180, 90, 100, 110, 130,
        70, 60, 50, 100
    ],
    'precios': [
        # Verduras
        28.50, 15.00, 18.00, 35.00, 12.00, 40.00,
        # Carnes
        140.00, 180.00, 190.00, 130.00, 350.00,
        # Jugos
        32.00, 28.00, 29.00,
        # Lácteos
        26.00, 55.00, 45.00, 25.00, 18.00,
        # Abarrotes
        34.00, 16.50, 22.00, 52.00, 15.00, 48.00, 20.00,
        # Limpieza
        38.00, 21.00, 29.00, 35.00
    ],
    'categoria': [
        # Verduras
        'Verdura', 'Verdura', 'Verdura', 'Verdura', 'Verdura', 'Verdura',
        # Carnes
        'Carne', 'Carne', 'Carne', 'Carne', 'Carne',
        # Jugos
        'Jugo', 'Jugo', 'Jugo',
        # Lácteos
        'lacteos', 'lacteos', 'lacteos', 'lacteos', 'lacteos',
        # Abarrotes
        'Abarrotes', 'Abarrotes', 'Abarrotes', 'Abarrotes', 'Abarrotes', 'Abarrotes', 'Abarrotes',
        # Limpieza
        'Limpieza', 'Limpieza', 'Limpieza', 'Limpieza'
    ],
}
df=DataFrame(stock)
def entrada_trabajador():
    uid_entrada=input(Fore.WHITE+"ingresa tu uid: "+Style.RESET_ALL)
    if uid_entrada in trabajadores_uid:
            mostrar_titulo()
            print(Fore.GREEN+Style.BRIGHT+"Bienvenido")
            mostrar_menu()
    else:
            print(Fore.RED+"ingrese un UID valido"+Style.RESET_ALL)
            entrada_trabajador

def mostrar_titulo():
    print(Fore.WHITE+"Bienvenido a nuestra tienda favorita y de nuestros clientes"+Style.RESET_ALL)
    print(Fore.RED+Style.BRIGHT+"                   HUEVOS CORP                       "+ Style.RESET_ALL)

def mostrar_productos():
    print(df[['producto','stock']])
    mostrar_menu()

def mostrar_precio():
    print(df[['producto','precios']])
    mostrar_menu()

verduras=df[df['categoria']=='Verdura']
carne=df[df['categoria']=='Carne']
Jugo=df[df['categoria']=='Jugo']
lacteos=df[df['categoria']=='lacteos']
abarrotes=df[df['categoria']=='Abarrotes']
Limpieza=df[df['categoria']=='Limpieza']
verduras_venta=0
carne_vetas=0
jugo=0
lacteos=0
abarrotes_ventas=0
limpieza_venta=0
venta_turno=0

def venta_producto():
    yn=input("deseas vender? ")
    cuuenta=0
    ticket=""
    while yn=="si":

        print(Fore.WHITE+Style.BRIGHT+"""
            verduras
            carne
            jugo
            lacteos
            abarrotes
            limpieza"""+Style.RESET_ALL)
        categoria=input("que seas vender: ")

        
        if categoria== "verduras":
                print(verduras)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        stock_actual = df.loc[df['producto'] == producto, 'stock'].values[0]
                        if cuanto_producto>stock_actual:
                              print("invalido ingrese una cantidad adecuada de: ")
                        else:
                            print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                            df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                            stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                            print(f"el stock del {producto} es {stock_producto}")
                            precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                            total=precio_unitario * cuanto_producto
                            print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                            verduras_venta+=cuanto_producto
                            cuuenta+=total
                            ticket+=producto + cuanto_producto
                            venta_turno+=1
                yn=input("deseas continuar: ")
        elif categoria=="carne":
                print(carne)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                        df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                        stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                        print(f"el stock del {producto} es {stock_producto}")
                        precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                        total=precio_unitario * cuanto_producto
                        print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                        verduras_venta+=cuanto_producto
                        cuuenta+=total
                        ticket+=producto + cuanto_producto
                        venta_turno+=1
                yn=input("deseas continuar: ")
        elif categoria=="jugo":
                print(Jugo)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                        df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                        stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                        print(f"el stock del {producto} es {stock_producto}")
                        precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                        total=precio_unitario * cuanto_producto
                        print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                        verduras_venta+=cuanto_producto
                        cuuenta+=total
                        ticket+=producto + cuanto_producto
                        venta_turno+=1
                yn=input("deseas continuar: ")
        elif categoria=="lacteos":
                print(lacteos)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                        df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                        stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                        print(f"el stock del {producto} es {stock_producto}")
                        precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                        total=precio_unitario * cuanto_producto
                        print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                        verduras_venta+=cuanto_producto
                        cuuenta+=total
                        ticket+=producto + cuanto_producto
                        venta_turno+=1
                yn=input("deseas continuar: ")
        elif categoria=="abarrotes":
                print(abarrotes)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                        df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                        stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                        print(f"el stock del {producto} es {stock_producto}")
                        precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                        total=precio_unitario * cuanto_producto
                        print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                        abarrotes_ventas +=cuanto_producto
                        cuuenta+=total
                        ticket+=producto + cuanto_producto
                        venta_turno+=1
                yn=input("deseas continuar: ")
        elif categoria=="limpieza":
                print(Limpieza)
                producto=input("que producto deseas vender? ")
                if producto in df['producto'].values:
                        cuanto_producto=int(input("cuanto deseas vender: "))
                        print(Fore.GREEN+"listo se ha completado tu compra"+Style.RESET_ALL)
                        df.loc[df['producto'] == producto, 'stock'] -= cuanto_producto
                        stock_producto=df.loc[df['producto']==producto,'stock'].values[0]
                        print(f"el stock del {producto} es {stock_producto}")
                        precio_unitario = df.loc[df['producto'] == producto, 'precios'].values[0]
                        total=precio_unitario * cuanto_producto
                        print(Fore.GREEN+f"tu total de esto es {total} "+Style.RESET_ALL)
                        verduras_venta+=cuanto_producto
                        cuuenta+=total
                        ticket+=producto + cuanto_producto
                        venta_turno+=1
                yn=input("deseas continuar: ")
        else:
            print("invalido")
            yn=input("deseas continuar: ")
    print(Fore.BLUE+f"tu cuenta total fue: {cuuenta}"+Style.RESET_ALL)      
    print(Fore.WHITE+Style.BRIGHT+f"tu ticket fue {ticket}"+Style.RESET_ALL)
    iva=cuuenta*1.16
    print(f"tu iva fue de {iva}")
    mostrar_menu()
def agregar_stock():
    print(df['producto'])
    producto_agregar_stock=input("A que producto deseas agregar?: ").strip()
    cuant_desea_agregar=int(input("cuanto stock agregar? "))
    df.loc[df['producto'] == producto_agregar_stock, 'stock'] += cuant_desea_agregar
    stock_producto = df.loc[df['producto'] == producto_agregar_stock, 'stock'].values[0]
    print(f"Stock actualizado Nuevo stock de {producto_agregar_stock} es: {stock_producto}")
    mostrar_menu()
    return stock_producto
    

def graficar_stock_productos():
    print("Generando gráfica de stock por producto...")
    plt.figure(figsize=(12, 8))
    plt.bar(df['producto'], df['stock'], color='skyblue')
    plt.title('Inventario de Stock por Producto', fontsize=16)
    plt.ylabel('Cantidad en Stock')
    plt.xlabel('Productos')
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    mostrar_menu()
def graficar_por_categoria():
    print("Generando gráfica de ventas totales por categoría...")
    categorias = ['Verduras', 'Carne', 'Jugo', 'Lácteos', 'Abarrotes', 'Limpieza']
    
    totales_ventas = (
        lacteos,
        verduras_venta,
        carne_vetas,
        jugo,
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
    mostrar_menu()
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
              6. Gráfica de stock por categoría
              7. Terminar tu turno
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
            graficar_por_categoria()
        elif opcion == "7":
            terminar_turno()
            break 
        else:
            print(Fore.RED + "Opción inválida. Por favor, elige un número del 1 al 7.")
        input(Fore.MAGENTA + "\nPresiona espacio para continuar...")
entrada_trabajador()
def terminar_turno():
       print("--------------terminastes tu turno-------------")
       print(f"tus ventas fueron {venta_turno}")
       print(Fore.BLACK+"-"*40+Style.RESET_ALL)