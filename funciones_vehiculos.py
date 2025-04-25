#funciones vehículos

import json
from funciones_archivos import *
#from funciones_transacciones import *
from tabulate import tabulate


def agregar_vehiculos(ruta):
    vehiculos = abrir_archivo(ruta)
    quiere_salir = False
    print("\nAgregar vehículo:\n")

    while quiere_salir == False:
        nuevo_id = 1
        if len(vehiculos) > 0:
            ultimo_vehiculo = vehiculos[-1]
            ultimo_id = ultimo_vehiculo['id_vehiculo']
            nuevo_id = ultimo_id + 1
    
        patente = input("Ingrese patente: ")
        marca = input("Ingrese marca: ")
        modelo = input("Ingrese modelo: ")
        tipo = input("Ingrese tipo: ")
        anio = input("Ingrese año: ")
        kilometraje = input("Ingrese kilometraje: ")
        precio_compra = input("Ingrese precio compra: ")
        precio_venta = input("Ingrese precio venta: ")
        estado = input("Ingrese estado: ")

        vehiculo = {
            'id_vehiculo':nuevo_id ,
            'patente': patente,
            'marca': marca,
            'modelo': modelo,
            'tipo': tipo,
            'anio': anio,
            'kilometraje': kilometraje,
            'precio_compra': precio_compra,
            'precio_venta': precio_venta,
            'estado': estado
            }

        vehiculos.append(vehiculo)
        salir = input('Escriba SI si quiere salir de lo contrario un caracter: ')
        if salir == 'SI':
            quiere_salir = True
            print("\n")   
    escribir_archivo(ruta, vehiculos)         

def listar_vehiculos(ruta):
    vehiculos = abrir_archivo(ruta)
    if len(vehiculos) == 0:
        print("No hay vehiculos en base de datos.")

    with open('vehiculos.json') as f:
        data = json.load(f)  

    # Extraer las claves del primer diccionario para obtener los encabezados de la tabla data[0].keys()
    #Pongo encabezados de manera manual como quiero que se muestren
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']

    # Crear una lista de listas para los datos (filas de la tabla)
    rows = [list(row.values()) for row in data]

    # Imprimir la tabla usando tabulate, tablefmt= fancy_grid o pgsql
    print("\n")
    print(tabulate(rows, headers=headers, tablefmt="pgsql"))      #
       

def eliminar_vehiculo(ruta, ruta_transacciones):
    from funciones_transacciones import listar_todas_las_transacciones
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = 0
    patente = (input("Ingrese la patente del vehículo a eliminar: "))
    lista = []
    lista = listar_todas_las_transacciones(ruta_transacciones, 'vehiculo')
    
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            vehiculo_encontrado = 1
            headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
            datos= [[vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']]]
           
            
            if lista.count(vehiculo['id_vehiculo']) > 0:
                print("No se puede eliminar el vehiculo ya que cuenta con una transacción en la base de datos.")
            else:
                vehiculos.remove(vehiculo)
                escribir_archivo(ruta, vehiculos)
                print("\nVehículo eliminado:")
                print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
                       
    if vehiculo_encontrado == 0:       
        print('\nNo se ha encontrado el vehículo')    
            
            

def editar_vehiculo(ruta): 
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    patente = (input("Ingrese la patente del vehículo a actualizar: "))
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            vehiculo_encontrado = True

            datos= [[vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']]]
           
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            print("\nEdite el registro: ")
            nueva_patente = input("Actualice patente: ")
            nueva_marca = input("Actualice marca: ")
            nuevo_modelo = input("Actualice modelo: ")
            nuevo_tipo = input("Actualice tipo: ")
            nuevo_anio = input("Actualice año: ")
            nuevo_kilometraje = input("Actualice kilometraje: ")
            nuevo_precio_compra = input("Actualice precio compra: ")
            nuevo_precio_venta = input("Actualice precio venta: ")
            nuevo_estado = input("Actualice estado: ")

            vehiculo["patente"] = nueva_patente
            vehiculo["modelo"] = nuevo_modelo
            vehiculo["tipo"] = nuevo_tipo
            vehiculo["anio"] = nuevo_anio
            vehiculo["kilometraje"] =  nuevo_kilometraje
            vehiculo["precio_compra"] = nuevo_precio_compra
            vehiculo["precio_venta"] = nuevo_precio_venta  
            vehiculo["estado"] = nuevo_estado  

            datos= [[vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']]]
           
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            escribir_archivo(ruta, vehiculos)  

    if vehiculo_encontrado == False:
        print("\nVehículo no encontrado")  

def buscar_por_marca(ruta): 
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    marca = input("Ingrese marca: ")
    marca = marca.capitalize()
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['marca'] == marca:
            vehiculo_encontrado = True                       
            datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
            vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
            vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
                        
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")
        return False

def buscar_por_modelo(ruta): 
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    modelo = input("Ingrese modelo: ")
    modelo.capitalize()
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['modelo'] == modelo:
            vehiculo_encontrado = True                       
            datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
            vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
            vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
                        
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")
        return False     
    
def buscar_por_patente(ruta): 
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    patente = (input("\nIngrese la patente: "))
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            vehiculo_encontrado = True
            #id_para_transaccion = vehiculo['id_vehiculo']
            datos = [[vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']]]
            id_vehiculo = datos[0][0]
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            return id_vehiculo
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")

def buscar_por_tipo(ruta): 
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    tipo = (input("\nIngrese el tipo de vehículo Sedan/Hatchback/SUV/Pick Up etc): "))
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['tipo'] == tipo:
            vehiculo_encontrado = True
            
            datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
            id_vehiculo = datos[0][0]
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            return id_vehiculo
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")        
    
    
def mostrar_por_pc(ruta):
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    precio_compra = input("\nIngrese el precio de compra: ")
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['precio_compra'] == precio_compra:
            vehiculo_encontrado = True

            datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
           
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")
        return False           

def mostrar_por_pv(ruta):
    vehiculos = abrir_archivo(ruta)
    vehiculo_encontrado = False
    precio_venta = input("\nIngrese el precio de venta: ")
    headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
    datos = []
    for vehiculo in vehiculos:
        if vehiculo['precio_venta'] == precio_venta:
            vehiculo_encontrado = True

            datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                    vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                    vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
           
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    if vehiculo_encontrado == False:
        print("Vehículo no encontrado")
        return False  

def buscar_vehiculo(ruta):
    #vehiculos = abrir_archivo(ruta)
    print("\nBuscar por: ")
    opcion = int(input("\n1. Marca \t2. Modelo \t3. Patente \t4. P. de compra \t5. P. de venta \t0. Salir: "))
    #vehiculo_encontrado = False

    
    while opcion != 0:
        match opcion:
            case 1:
                buscar_por_marca(ruta)
                if buscar_por_marca == False:
                    opcion = 0
                    
            case 2:
                buscar_por_modelo(ruta)
                if buscar_por_modelo == False:
                    opcion = 0
            case 3:
                buscar_por_patente(ruta)
                if buscar_por_patente == False:
                    opcion = 0
            case 4:
                mostrar_por_pc(ruta)
                if mostrar_por_pc == False:
                    opcion = 0
            case 5:                
                mostrar_por_pv(ruta)
                if mostrar_por_pv == False:
                    opcion = 0
            case 0: 
                print("salir")    

        print("\nBuscar por: ")
        opcion = int(input("\n1. Marca \t2. Modelo \t3. Patente \t4. P. de compra \t5. P. de venta \t0. Salir: "))            
            

def menu_vehiculos():
    ruta = 'vehiculos.json'
    ruta_transacciones = 'transacciones.json'
    existe = abrir_archivo(ruta)
    # si no existe

    if existe == False:
        crear_archivo(ruta)
        #vehiculos = abrir_archivo(ruta) 

    print("\nMenú vehículos: ")   
    print("\n1. Listar vehículos  \n2. Agregar vehículos \n3. Editar vehículo  \n4. Eliminar vehiculo \n5. Buscar vehiculo \n0. Salir")
    opcion_ingresada = int(input("Ingrese opción: "))    

    while opcion_ingresada != 0:
        match opcion_ingresada:
            case 1:
                listar_vehiculos(ruta)
                    
            case 2:
                agregar_vehiculos(ruta)
                listar_vehiculos(ruta)
            case 3:
                editar_vehiculo(ruta)
                    
            case 4:
                eliminar_vehiculo(ruta, ruta_transacciones)
                
            case 5:
                buscar_vehiculo(ruta)    
            case 0: 
                print("Saliendo del programa")

        print("\nMenú vehículos: ")            
        print("\n1. Listar vehículos  \n2. Agregar vehículos \n3. Editar vehículo  \n4. Eliminar vehiculo \n5. Buscar vehiculo \n0. Salir") 
        opcion_ingresada = int(input("\nIngrese opción: ")) 

      