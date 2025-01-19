import json
from datetime import datetime

def seleccion_1():
    while True:
        print("📒 BIENVENIDO AL INVENTARIO, QUE VAMOS HACER EL DIA DE HOY ? ")
        print("             1. REGISTRAR PRODUCTO                         ")
        print("             2. INGRESAR PRODUCTO                          ")
        print("             3. SACAR PRODUCTO                             ")
        print("             4. VOLVER AL MENI                             ")
        try:
          respuesta = int(input())
          if respuesta == 1 :
           registrar_producto()
          elif respuesta == 2:
           ingresar_producto()
          elif respuesta == 3:
           sacar_producto()
          elif respuesta == 4:
              break
          else:
              print("❌ EL NUMERO DE LA OPCIÓN QUE ELEGISTE NO EXISTE")
        except ValueError:
            print(" 😒 LETRAS COMO OPCION NO SE PUEDE ")

DATA_FILE = 'inventario.json'

def cargar_datos():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_datos(datos):
    with open(DATA_FILE, 'w') as file:
        json.dump(datos, file, indent=4)

def registrar_producto():
    datos = cargar_datos()
    codigo = input("         INGRESA EL CODIGO DE TU PRODUCTO:   ")
    nombre = input("         INGRESA EL NOMBRE DE TU PORDUCTO:   ")
    proveedor = input("      INGRESA EL NOMBRE DEL PORVEEDOR:    ")
    
    if codigo in datos:
        print("😉 EL PRODUCTO YA EXISTE")    
    else:
        datos[codigo] = {
            'nombre': nombre,
            'proveedor': proveedor,
            'stock': {'norte': 0, 'centro': 0, 'oriente': 0},
            'historial': []
        }
        guardar_datos(datos)
        print("😊 TU PRODUCTO YA SE GUARDO EN EL INVENTARIO")

def ingresar_producto():
    datos = cargar_datos()
    codigo = input("INGRESA EL CODIGO DEL PRODUCTO:")
    if codigo not in datos:
        print("   😏 EL PRODUCTO NO SE ENCUENTRA REGISTRARDO   ")
        return
    
    cantidad = int(input(" CUANTAS UNIDADES VAS AÑADIR A TU PRODUCTO:  "))
    print(" A QUE BODEGA VA TU PORDUCTO ?")
    print("   SEDE NORTE   ")
    print("   SEDE CENTRO  ")
    print("   SEDE ORIENTE ")
    bodega = input()  
    descripcion = input("  INGRESA UNA DESCRIPCIÓN DE LA ENTRADA DEL PRODUCTO ")
    
    if bodega not in datos[codigo]['stock']:
        print(F"🤨 LA BODEGA: {bodega} NO EXISTE")
        return
    
    datos[codigo]['stock'][bodega] += cantidad
    datos[codigo]['historial'].append({
        'fecha': str(datetime.now()),
        'tipo': 'Entrada',
        'cantidad': cantidad,
        'bodega': bodega,
        'descripcion': descripcion
    })
    guardar_datos(datos)
    print("👍 LAS CANTIDADES DEL PORDUCTO YA SE ENCUENTRAN EN EL INVENTARIO")

def sacar_producto():
    datos = cargar_datos()
    codigo = input(" INGRESA EL CODIGO DEL PRODUCTO A SACAR: ")
    if codigo not in datos:
        print(" 😑 EL PORDUCTO NO EXISTE EN EL INVENTARIO")
        return
    
    cantidad = int(input("CUANTAS UNIDADES VAS A SACAR: "))
    print(" DE QUE  BODEGA VAS A SACAR EL PORDUCTO ?")
    print("   SEDE NORTE   ")
    print("   SEDE CENTRO  ")
    print("   SEDE ORIENTE ")
    bodega = input("")
    descripcion = input("Ingrese una descripción: ")
    
    if bodega not in datos[codigo]['stock']:
        print("LA BODEGA NO EXISTE")
        return
    
    if datos[codigo]['stock'][bodega] < cantidad:
        print("😯 NO HAY SUFICIENTES UNIDADES DEL PRODUCTO")
        return
    
    datos[codigo]['stock'][bodega] -= cantidad
    datos[codigo]['historial'].append({
        'fecha': str(datetime.now()),
        'tipo': 'Salida',
        'cantidad': cantidad,
        'bodega': bodega,
        'descripcion': descripcion
    })
    guardar_datos(datos)
    print("😀 LAS UNIDADES RETIRADAS DEL PORDUCTO YA SON UN ECHO")