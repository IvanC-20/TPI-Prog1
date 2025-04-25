#funciones vehículos

import json
from funciones_archivos import *
#from funciones_transacciones import * 
from tabulate import tabulate

#listar_todas_las_transacciones



def agregar_clientes(ruta):
    clientes = abrir_archivo(ruta)
    quiere_salir = False
    print("\nAgregar cliente:\n")

    while quiere_salir == False:
        nuevo_id = 1
        if len(clientes) > 0:
            ultimo_cliente = clientes[-1]
            ultimo_id = ultimo_cliente['id_cliente']
            nuevo_id = ultimo_id + 1
    
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        direccion = input("Ingrese dirección: ")
        telefono = input("Ingrese teléfono: ")
        email = input("Ingrese correo electrónico: ")
        

        cliente = {
            'id_cliente': nuevo_id ,
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni,
            'direccion': direccion,
            'telefono': telefono,
            'email': email
        }    

        clientes.append(cliente)
        salir = input('Escriba SI si quiere salir de lo contrario un caracter: ')
        if salir == 'SI':
            quiere_salir = True
            print("\n")   
    escribir_archivo(ruta, clientes)         

def listar_clientes(ruta):
    clientes = abrir_archivo(ruta)
    if len(clientes) == 0:
        print("No hay clientes en base de datos.")

    with open('clientes.json') as f:
        data = json.load(f)  

    # Encabezados
    headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']

    # Crear una lista de listas para los datos (filas de la tabla)
    rows = [list(row.values()) for row in data]

    # Imprimir la tabla usando tabulate, tablefmt= fancy_grid o pgsql
    print("\n")
    print(tabulate(rows, headers=headers, tablefmt="pgsql"))      #
       



def eliminar_cliente(ruta, ruta_transacciones):
    from funciones_transacciones import listar_todas_las_transacciones
    clientes = abrir_archivo(ruta)
    cliente_encontrado = 0
    dni = (input("Ingrese el dni del cliente a eliminar: "))
    lista = []
    lista = listar_todas_las_transacciones(ruta_transacciones, 'cliente')
    
    for cliente in clientes:
        if cliente['dni'] == dni:
            cliente_encontrado = 1
            headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
            datos= [[cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
                    cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']]]
           
            
            if lista.count(cliente['id_cliente']) > 0:
                print("No se puede eliminar el cliente ya que cuenta con una transacción en la base de datos.")
            else:
                clientes.remove(cliente)
                escribir_archivo(ruta, clientes)
                print("\nCliente eliminado")
                print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
                       
    if cliente_encontrado == 0:       
        print('\nNo se ha encontrado el cliente')    
            
           

def editar_cliente(ruta): 
    clientes = abrir_archivo(ruta)
    cliente_encontrado = False
    dni = (input("Ingrese el dni del cliente a actualizar: "))
    headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
    for cliente in clientes:
        if cliente['dni'] == dni:
            cliente_encontrado = True

            datos= [[cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
                    cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']]]
           
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            print("\nEdite el registro: ")
            nuevo_nombre = input("Actualice nombre: ")
            nuevo_apellido = input("Actualice apellido: ")
            nuevo_dni = input("Actualice dni: ")
            nueva_direccion = input("Actualice direccion: ")
            nuevo_tel = input("Actualice teléfono: ")
            nuevo_email = input("Actualice correo electrónico: ")

            cliente['nombre'] = nuevo_nombre
            cliente['apellido'] = nuevo_apellido
            cliente['dni'] = nuevo_dni
            cliente['direccion'] = nueva_direccion
            cliente['telefono'] = nuevo_tel
            cliente['email'] = nuevo_email
            
            
            datos= [[cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
                    cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']]]
                    
           
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            print("Datos del cliente actualizados")
            escribir_archivo(ruta, clientes)  

    if cliente_encontrado == False:
        print("\nCliente no encontrado")  

def buscar_por_dni(ruta): 
    clientes = abrir_archivo(ruta)
    cliente_encontrado = False
    dni = input("Ingrese el dni: ")
    headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
    for cliente in clientes:
        if cliente['dni'] == dni:
            cliente_encontrado = True
            
            datos= [[cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
                    cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']]]
            
            id_cliente = datos[0][0]
           
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            return id_cliente
            
    if cliente_encontrado == False:
        print("\n\tDni no encontrado")
        return False

def buscar_por_nombre(ruta): 
    clientes = abrir_archivo(ruta)
    cliente_encontrado = False
    nombre = input("Ingrese nombre: ")
    nombre = nombre.capitalize()
    headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
    datos = []
    for cliente in clientes:
        if cliente['nombre'] == nombre:
            cliente_encontrado = True                       
            datos.append([cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
            cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']])
                        
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            
    if cliente_encontrado == False:
        print("Nombre no encontrado")
        return False     
    
def buscar_por_apellido(ruta): 
    clientes = abrir_archivo(ruta)
    cliente_encontrado = False
    apellido = input("\nIngrese el apellido: ")
    apellido = apellido.capitalize()
    headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
    datos = []
    for cliente in clientes:
        if cliente['apellido'] == apellido:
            cliente_encontrado = True

            datos.append([cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
            cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']])
           
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    if cliente_encontrado == False:
        print("Apellido no encontrado")
        return False    
         

def menu_buscar_cliente(ruta):
    print("\nBuscar por: ")
    opcion = int(input("\n1. Nombre \t2. Apellido \t3. DNI \t0. Salir: "))
    
    while opcion != 0:
        match opcion:
            case 1:
                buscar_por_nombre(ruta)
                if buscar_por_nombre == False:
                    opcion = 0
                    
            case 2:
                buscar_por_apellido(ruta)
                if buscar_por_apellido == False:
                    opcion = 0
            case 3:
                buscar_por_dni(ruta)
                if buscar_por_dni == False:
                    opcion = 0
            case 0: 
                print("salir")    

        print("\nBuscar por: ")
        opcion = int(input("\n1. Nombre \t2. Apellido \t3. DNI \t0. Salir: "))           
            

def menu_clientes():
    ruta = 'clientes.json'
    ruta_transacciones = 'transacciones.json'
    existe = abrir_archivo(ruta)
    
    # si no existe
    if existe == False:
        crear_archivo(ruta)
       

    print("\nMenú clientes: ")   
    print("\n1. Listar Clientes  \n2. Agregar cliente \n3. Editar cliente  \n4. Eliminar cliente \n5. Buscar cliente \n0. Salir")
    opcion_ingresada = int(input("Ingrese opción: "))    

    while opcion_ingresada != 0:
        match opcion_ingresada:
            case 1:
                listar_clientes(ruta)
                    
            case 2:
                agregar_clientes(ruta)
                listar_clientes(ruta)
            case 3:
                editar_cliente(ruta)
                    
            case 4:
                eliminar_cliente(ruta, ruta_transacciones)
            case 5:
                menu_buscar_cliente(ruta)    
            case 0: 
                print("Saliendo del programa")

        print("\nMenú Clientes: ")            
        print("\n1. Listar Clientes  \n2. Agregar cliente \n3. Editar cliente  \n4. Eliminar cliente \n5. Buscar cliente \n0. Salir") 
        opcion_ingresada = int(input("\nIngrese opción: ")) 

      