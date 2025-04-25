from funciones_vehiculos import menu_vehiculos
from funciones_clientes import menu_clientes
from funciones_transacciones import *

#menu_transacciones

def main():
    print("Bienvenido")   
    print("\n1. Clientes  \n2. Vehículos \n3. Transacciones  \n0. Salir: ")
    opcion_ingresada = int(input("\nIngrese opción: "))    

    while opcion_ingresada != 0:
        match opcion_ingresada:
            case 1:
                menu_clientes()
                    
            case 2:
                menu_vehiculos()
            case 3:
                menu_transacciones()      
              
            case 0: 
                print("Saliendo del programa")
        print("\nMenú principal")            
        print("\n1. Clientes  \n2. Vehículos \n3. Transacciones  \n0. Salir")
        opcion_ingresada = int(input("\nIngrese opción: "))

main()       