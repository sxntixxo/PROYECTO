import json
from registrar import cargar_datos

def seleccion_2():
     while True:
        print("📒 BIENVENIDO A REPORTES, QUE VAS HACER EL DIA DE HOY ?")
        print("             1. BUSCAR PRODUCTO                       ")
        print("             2. HISTORIAL DE UN PRODUCTO              ")
        print("             3. GENERAR UN REPORTE                    ")
        print("             4. VOLVER AL MENU                        ")
        
        opcion = int(input())
        
        if opcion == 1:
            buscar_producto()
        elif opcion == 2:
            historial_producto()
        elif opcion == 3:
            generar_reporte()
        elif opcion == 4:
            break
        else:
            print(f"😑LA OPCION ({opcion}) ESCOGIDA NO EXISTE")


def buscar_producto():
        datos = cargar_datos()
        codigo = input(" PARA PODER BUSCAR EL PORDUCTO ESCRIBE EL CODIGO DEL PRODUCTO: ")
        if codigo not in datos:
            print(" 😣 NO EXISTE EL CODIGO")
            return
        
        producto = datos[codigo]
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Proveedor: {producto['proveedor']}")
        for bodega, cantidad in producto['stock'].items():
            print(f"Bodega {bodega}: {cantidad}")

def historial_producto():
        datos = cargar_datos()
        
        codigo = input(" PARA PODER VER EL HISTORIAL DEL PORDUCTO ESCRIBE EL CODIGO DEL PRODUCTO: ")
        if codigo not in datos:
            print("😣 NO EXISTE EL CODIGO")
            return
        
        print("iNGRESA EL NOMBRE DE LA BODEGA DONDE QUIERES MIRAR EL PORDUCTO")
        print(" BODEGA NORTE")
        print(" BODEGA CENTRO")
        print(" BODEGA ORIENTE")
        bodega = input(" ")
        if bodega not in ['norte', 'centro', 'oriente']:
            print("🤨 LA BODEGA NO EXISTE")
            return
        
        producto = datos[codigo]
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Proveedor: {producto['proveedor']}")
        print(f"Historial de la bodega {bodega}:")
        for movimiento in producto['historial']:
            if movimiento['bodega'] == bodega:
                print(f"Fecha: {movimiento['fecha']}, Tipo: {movimiento['tipo']}, Cantidad: {movimiento['cantidad']}, Descripción: {movimiento['descripcion']}")

def generar_reporte():
        datos = cargar_datos()
        reporte = {}
        for codigo, producto in datos.items():
            total = sum(producto['stock'].values())
            reporte[codigo] = {
                'nombre': producto['nombre'],
                'total': total,
                'bodegas': producto['stock']
            }
        
        print(" 📄 VAMOS A GENERAR EL REPORTE")
        for codigo, info in reporte.items():
            print(f"Código: {codigo}, Nombre: {info['nombre']}, Total: {info['total']}, Bodegas: {info['bodegas']}")
        
        opcion = input("¿QIERES GUARDAR EL REPORTE? (s/n): ")
        if opcion.lower() == 's':
            with open('reporte_inventario.json', 'w') as file:
                json.dump(reporte, file, indent=4)
            print("👍 EL REPORTE YA ESTA GUARDADO 'reporte_inventario.json'.")
