import json
import os

def abrir_archivo(ruta):
    if os.path.exists(ruta) == False:
        return False
    
    archivo = open(ruta,'r', encoding='utf-8')

    contenido = archivo.read()
    #json loads toma un objeto de archivo y devuelve un objeto json
    obj_json = json.loads(contenido)

    archivo.close()
    return obj_json
    


def crear_archivo(ruta):
    #revisar si el archivo existe para no sobreescribirlo
    if os.path.exists(ruta) == True:
        return ruta
    #inicializar el archivo con algo(si este no existe) y dps cerramos
    archivo = open(ruta, 'w', encoding='utf-8')
    lista_vacia = []
    string_lista = json.dumps(lista_vacia)
    archivo.write(string_lista)
    archivo.close()
    return ruta

def escribir_archivo(ruta, datos):
    if os.path.exists(ruta) == False:
        return False
    
    archivo = open(ruta, 'w', encoding='utf-8')
    #transformamos de object(json) a string 
    string_datos = json.dumps(datos)
    #escribimos el string y luego cerramos el archivo
    archivo.write(string_datos)
    archivo.close()
    return True #retornamos true por ahora para probar, no es necesario