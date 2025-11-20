import pandas
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from colorama import Style, Fore,Back,init
import os
trabajadores_uid={
        '0321':{
            'nombre':'Omar'},
        '8149':{
            'nombre':'Monge'},
        '281818':{
            'nombre':'Isaias'},
        '371442':{
            'nombre':'Akzel'},
        '171007':{
            'nombre':"Chris"
        }
}
trabajdores='trabajadoressuid.csv'
if os.path.exists(trabajdores):
    df_temp = pandas.read_csv(trabajdores, index_col=0, dtype=str)
    trabajadores_uid = df_temp.to_dict(orient='index')
    trabajadores_uid_limpio = {}
    for uid, datos in trabajadores_uid.items():
        uid_str = str(uid) 
        datos_limpios = {k: v for k, v in datos.items() if pandas.notna(v) and v is not None}
        trabajadores_uid_limpio[uid_str] = datos_limpios
    trabajadores_uid = trabajadores_uid_limpio
else:

    df_temp = pandas.DataFrame.from_dict(trabajadores_uid, orient='index')
    df_temp.to_csv(trabajdores, index_label='uid')

def eliminar_nuevo_empleado():
    global trabajadores_uid, trabajdores
    print("-"*50)
    a_quien_vamos_a_eliminar=input("Que empleado vamos a eliminar: (uid) ").strip()
    if a_quien_vamos_a_eliminar in trabajadores_uid:
        if a_quien_vamos_a_eliminar=="171007":
            print(Fore.RED+Style.BRIGHT+"no se puede eliminar el admin"+Style.RESET_ALL)
            return
        del trabajadores_uid[a_quien_vamos_a_eliminar]
        guardar_empleados_csv()
        print(Fore.RED+"se ha eliminado de manera correcta")
        print(trabajadores_uid)
    else:
        print("invalido")
        input("enter para continuar ")
        eliminar_nuevo_empleado()
def guardar_empleados_csv():
    global trabajadores_uid, trabajdores
    df_guardar = pandas.DataFrame.from_dict(trabajadores_uid, orient='index')
    df_guardar.to_csv(trabajdores, index_label='uid')
    print(Fore.CYAN + " se han guardado los datos chaval" + Style.RESET_ALL)


def agregar_nuevo_empleado():
    global trabajadores_uid, trabajdores
    nombre_nuevo_empleado=input(Fore.WHITE+"cual es el nombre del nuevo usuario: ").upper()
    uid_nuevo_empleado=input(Fore.WHITE+"cual es el uid del nuevo usuario: ").upper()
    if uid_nuevo_empleado in trabajadores_uid:
        print("-------------ESTE YA ESTA-----------")
        return 
    trabajadores_uid[uid_nuevo_empleado] = {'nombre': nombre_nuevo_empleado}
    guardar_empleados_csv()
    print("/"*60)
    print(Fore.GREEN+Style.BRIGHT+"SE HA AGREGADO EXITOSAMENTE"+Style.RESET_ALL)
    print(trabajadores_uid)
    return trabajadores_uid