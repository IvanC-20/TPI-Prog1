#funciones vehículos

import json
#import datetime
from funciones_archivos import *
from funciones_vehiculos import *
from funciones_clientes import *
from tabulate import tabulate

def agregar_transacciones(ruta, ruta_vehiculos, ruta_clientes, tipo):
    transacciones = abrir_archivo(ruta)
    vehiculos = abrir_archivo(ruta_vehiculos)
    clientes = abrir_archivo(ruta_clientes)
    tipo_tr = tipo
    ciclo_continua = ''
    id_vehiculo_transaccion = 0
    quiere_salir = False
    quiere_salir_2 = False
    quiere_salir_principal=False
    print(f"\nRegistrar {tipo_tr}")
    patente = (input("\nIngrese la patente del vehículo: "))
    while quiere_salir_principal == False: 
        #Con este while consigo id vehiculo, buscando y mostrando por patente   
        while quiere_salir == False:
            
            vehiculo_encontrado = False
                
            headers = ['ID', 'Patente', 'Marca', 'Mod.', 'Tipo', 'Año', 'Kmts', 'P. compra', 'P. venta', 'Estado']
            datos = []

            for vehiculo in vehiculos:
                if vehiculo['patente'] == patente:
                    vehiculo_encontrado = True
                    id_vehiculo_transaccion = vehiculo['id_vehiculo']
                    datos.append([vehiculo['id_vehiculo'], vehiculo['patente'], vehiculo['marca'], 
                                vehiculo['modelo'], vehiculo['tipo'], vehiculo['anio'], vehiculo['kilometraje'],
                                vehiculo['precio_compra'], vehiculo['precio_venta'], vehiculo['estado']])
                    
            print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
            #quiere_salir = True
            if vehiculo_encontrado == False:
                print("Vehículo no encontrado")
                   
                salir = input('Escriba SI si quiere salir de lo contrario un caracter: ')
                if salir == 'SI':
                  ciclo_continua = 'no'
                  quiere_salir_principal = True
                  quiere_salir = True
                else:
                    print(f"\nRegistrar {tipo_tr}")
                    patente = (input("\nIngrese la patente del vehículo: "))  
            elif vehiculo_encontrado == True:
                quiere_salir = True
        
        if ciclo_continua != 'no':

            
            dni = (input("\nIngrese dni del cliente: "))        
            #Ahora debo buscar y encontrar el cliente por dni para llenar datos transacción
            while quiere_salir_2 == False:
            
                cliente_encontrado = False
            
                headers = ['ID', 'Nombre', 'Apellido', 'dni', 'Dirección', 'Teléfono', 'Correo Electrónico']
                datos_cliente = []
                for cliente in clientes:
                    if cliente['dni'] == dni:
                        cliente_encontrado = True
                        id_cliente_transaccion = cliente['id_cliente']
                        nombre = cliente['nombre']
                        apellido = cliente['apellido']
                        datos_cliente= [[cliente['id_cliente'], cliente['nombre'], cliente['apellido'], 
                                cliente['dni'], cliente['direccion'], cliente['telefono'], cliente['email']]]
           
                print("\n",tabulate(datos_cliente, headers= headers, tablefmt='pgsql'))
            
                if cliente_encontrado == False:
                    print("Dni no encontrado") 
                    salir = input('Escriba SI si quiere salir de lo contrario un caracter: ')
                    if salir == 'SI':
                        quiere_salir_principal = True
                        quiere_salir_2 = True
                    else:
                        dni = (input("\nIngrese dni del cliente: "))  
                elif cliente_encontrado == True:
                    quiere_salir_2 = True

        if quiere_salir_principal == False:    
            print(f"\nRegistrar {tipo_tr} de este vehículo:\n")

            nuevo_id = 1
            if len(transacciones) > 0:
                ultimo_transaccion = transacciones[-1]
                ultimo_id = ultimo_transaccion['id_transaccion']
                nuevo_id = ultimo_id + 1

        
        
        
        
            monto = input("Ingrese monto: ")
            fecha = input("Ingrese fecha dd/mm/aa: ")
            observaciones = input("Observaciones: ")

            transaccion = {
            'id_transaccion': nuevo_id ,
            'id_vehiculo': id_vehiculo_transaccion,
            'id_cliente': id_cliente_transaccion,
            
            'tipo': tipo,
            'fecha': fecha,
            'monto': monto,
            'observaciones': observaciones
        }    

            transacciones.append(transaccion)
            
            escribir_archivo(ruta, transacciones)
            if tipo == 'compra':
                print(f"El vehículo patente {patente}  se lo hemos comprado al cliente {nombre} {apellido} ")
            elif tipo == 'venta':
                print(f"El vehículo patente {patente}  se lo hemos vendido al cliente {nombre} {apellido} ")   
            quiere_salir_principal = True
                #print("\n")   
            
                
            
             

             

def listar_transacciones(ruta):
    transacciones = abrir_archivo(ruta)
    if len(transacciones) == 0:
        print("No hay transacciones en base de datos.")

    with open('transacciones.json') as f:
        data = json.load(f)  

    # Extraer las claves del primer diccionario para obtener los encabezados de la tabla data[0].keys()
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']

    # Crear una lista de listas para los datos (filas de la tabla)
    rows = [list(row.values()) for row in data]

    # Imprimir la tabla usando tabulate, tablefmt= fancy_grid o pgsql
    print("\n")
    print(tabulate(rows, headers=headers, tablefmt="pgsql"))             
             

def listar_transacciones_por_compra(ruta): 
    transacciones = abrir_archivo(ruta)
    transaccion_encontrado = False
    total = 0
    #opcion = int(input("\nListar por: \n1. Compras \n2. Ventas \nIngrese opción: "))
    datos= []
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']
    for transaccion in transacciones:
        if transaccion['tipo'] == 'compra':          
            
            transaccion_encontrado = True
            datos.append([transaccion['id_transaccion'], transaccion['id_vehiculo'], transaccion['id_cliente'], 
                    transaccion['tipo'], transaccion['fecha'], transaccion['monto'], transaccion['observaciones']])
            total = total + float(transaccion['monto'])
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    print(f"\nMonto total compras: $ {total:2}")     
              
            
    if transaccion_encontrado == False:
        print("No hay transacciones")
        return False
    
def listar_transacciones_compra_por_cliente(ruta, ruta_clientes): 
    transacciones = abrir_archivo(ruta)
    clientes = abrir_archivo(ruta_clientes)
    transaccion_encontrado = False
    total = 0
    
    print("\nBuscar compras por cliente")
    
    #llamo a la función y asigno valor que retorna a la variable id_encontrado
    id_encontrado = buscar_por_dni(ruta_clientes)
    
    datos= []
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']
    for transaccion in transacciones:
        if transaccion['tipo'] == 'compra' and transaccion['id_cliente'] == id_encontrado:

            ids_clientes_con_transaccion_compra = []   
            ids_clientes_con_transaccion_compra.append(transaccion['id_cliente'])     
            transaccion_encontrado = True
            datos.append([transaccion['id_transaccion'], transaccion['id_vehiculo'], transaccion['id_cliente'], 
                    transaccion['tipo'], transaccion['fecha'], transaccion['monto'], transaccion['observaciones']])
            total = total + float(transaccion['monto'])
            
    if transaccion_encontrado == True: 
        for cliente in clientes:  
            if cliente['id_cliente'] == id_encontrado:     
                nombre = cliente['nombre'] 
                apellido = cliente['apellido'] 
        print("\nCompras realizadas a este cliente: ")       
        print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
        print(f"\nMonto total compras a {nombre} {apellido}: $ {total:2}")
        return ids_clientes_con_transaccion_compra 
    if transaccion_encontrado == False:
        print("\n\tNo hay transacciones")
        return False        
    
def listar_transacciones_por_venta(ruta): 
    transacciones = abrir_archivo(ruta)
    total = 0
    transaccion_encontrado = False
    datos= []
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']
    for transaccion in transacciones:
        if transaccion['tipo'] == 'venta':
                    
            transaccion_encontrado = True
            datos.append([transaccion['id_transaccion'], transaccion['id_vehiculo'], transaccion['id_cliente'], 
                    transaccion['tipo'], transaccion['fecha'], transaccion['monto'], transaccion['observaciones']])
            total = total + float(transaccion['monto'])
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    print(f"\nMonto total ventas: $ {total:2}")
         
             
            
    if transaccion_encontrado == False:
        print("No hay transacciones")
        return False    
    
def listar_transacciones_venta_por_cliente(ruta, ruta_clientes): 
    transacciones = abrir_archivo(ruta)
    clientes = abrir_archivo(ruta_clientes)
    transaccion_encontrado = False
    total = 0
    
    print("\nBuscar ventas por cliente")
    
    #llamo a la función y asigno valor que retorna a la variable id_encontrado
    id_encontrado = buscar_por_dni(ruta_clientes)
    
    datos= []
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']
    for transaccion in transacciones:
        if transaccion['tipo'] == 'venta' and transaccion['id_cliente'] == id_encontrado:
            #ids_clientes_con_transaccion_venta = []   
            #ids_clientes_con_transaccion_venta.append(transaccion['id_cliente'], transaccion['id_vehiculo'])         
            transaccion_encontrado = True
            datos.append([transaccion['id_transaccion'], transaccion['id_vehiculo'], transaccion['id_cliente'], 
                    transaccion['tipo'], transaccion['fecha'], transaccion['monto'], transaccion['observaciones']])
            total = total + float(transaccion['monto'])
    if transaccion_encontrado == True:
        for cliente in clientes:  
            if cliente['id_cliente'] == id_encontrado:     
                nombre = cliente['nombre'] 
                apellido = cliente['apellido']        
        print("\nVentas realizadas a este cliente: ")       
        print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
        print(f"\nMonto total ventas a {nombre} {apellido}: $ {total:2}")
        #return ids_clientes_con_transaccion_venta

    if transaccion_encontrado == False:
        print("\n\tNo hay transacción")
        return False

#def eliminar_si_o_no()
#    lista = []

def listar_todas_las_transacciones(ruta, dato = 'nada'): 
    transacciones = abrir_archivo(ruta)
    transaccion_encontrado = False
    total = 0
    ids_vehiculos = []
    ids_clientes = []
    
    datos= []
    headers = ['ID', 'ID_vehiculo', 'ID_cliente', 'Tipo', 'Fecha', 'Monto', 'Observaciones']
    for transaccion in transacciones:
            datos.append([transaccion['id_transaccion'], transaccion['id_vehiculo'], transaccion['id_cliente'], 
                    transaccion['tipo'], transaccion['fecha'], transaccion['monto'], transaccion['observaciones']])
            ids_vehiculos.append(transaccion['id_vehiculo'])
            ids_clientes.append(transaccion['id_cliente'])
            total = total + float(transaccion['monto'])
    if dato == 'cliente':
        return ids_clientes
    elif dato == 'vehiculo':
        return ids_vehiculos  
           
    print("\nListado de transacciones: ")       
    print("\n",tabulate(datos, headers= headers, tablefmt='pgsql'))
    print(f"\nMonto total en transacciones: $ {total:2}")
        
    if len(transacciones) == 0:
        print("\n\tNo hay transacciones")
        return False

def eliminar_transaccion(ruta):
    transacciones = abrir_archivo(ruta)
    transaccion_encontrada = 0
    id_transaccion = int(input("Ingrese el nro de transacción a eliminar: "))
    for transaccion in transacciones:
        if transaccion['id_transaccion'] == id_transaccion:
            transacciones.remove(transaccion)
            escribir_archivo(ruta, transacciones)
            print(f"\nTransacción con ID: {id_transaccion}  eliminada")
            transaccion_encontrada = 1
       
    if transaccion_encontrada == 0:       
        print('\nNo se ha encontrado la transacción.')  
               
      
def menu_buscar_venta(ruta, ruta_clientes):

    print("\nBuscar compras/ventas: ")
    opcion = int(input("\n1. Ventas por cliente \t2. Compras por cliente  \t0. Salir \tIngrese opción: "))
    
    while opcion != 0:
        match opcion:
            case 1:
                listar_transacciones_venta_por_cliente(ruta, ruta_clientes)
                if listar_transacciones_venta_por_cliente == False:
                    opcion = 0
                    
            case 2:
                listar_transacciones_compra_por_cliente(ruta, ruta_clientes)
                if listar_transacciones_compra_por_cliente == False:
                    opcion = 0
            
            case 0: 
                print("salir")    

        print("\nBuscar compras/ventas: ")
        opcion = int(input("\n1. Ventas por Cliente \t2. Compras por cliente \t0. Salir \tIngrese opción: "))    


def menu_transacciones():
    ruta = 'transacciones.json'
    ruta_vehiculos = 'vehiculos.json'
    ruta_clientes = 'clientes.json'
    existe = abrir_archivo(ruta)
    # si no existe

    if existe == False:
        crear_archivo(ruta)
       

    print("\nMenú transacciones: ")   
    print("\n1. Registrar compra  \n2. Registrar venta \n3. Listado compras  \n4. Listado ventas \n5. Buscar por cliente \n6. Listar todas las transacciones \n7. Eliminar transaccion \n0. Salir")
    opcion_ingresada = int(input("Ingrese opción: "))    

    while opcion_ingresada != 0:
        match opcion_ingresada:
            case 1:
                agregar_transacciones(ruta, ruta_vehiculos, ruta_clientes, 'compra')
                    
            case 2:
                agregar_transacciones(ruta, ruta_vehiculos, ruta_clientes, 'venta')
                
            case 3:
                listar_transacciones_por_compra(ruta)
                
                    
            case 4:
                listar_transacciones_por_venta(ruta)
                
            case 5:
                    menu_buscar_venta(ruta, ruta_clientes)
            case 6:
                    listar_todas_las_transacciones(ruta) 
            case 7: 
                    eliminar_transaccion(ruta)                           
            case 0: 
                print("Saliendo del programa")

        print("\nMenú transacciones: ")            
        print("\n1. Registrar compra  \n2. Registrar venta \n3. Listado compras  \n4. Listado ventas \n5. Buscar por cliente \n6. Listar todas las transacciones \n7. Eliminar transaccion \n0. Salir") 
        opcion_ingresada = int(input("\nIngrese opción: "))