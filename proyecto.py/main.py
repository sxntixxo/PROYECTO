from registrar import seleccion_1
from reporte import seleccion_2
while True:
        print("📒   BIENVENIDO A SU PROGRAMA DE GESTIÓN DE INVENTARIO   ")
        print("                1. INVENTARIO                            ")
        print("                2. REPORTES                              ")
        print("                3. Salir                                 ")
        
        try:
          opcion = int(input("SELECCIONA UNA OPCION: "))
          if opcion == 1:
            seleccion_1()
          elif opcion == 2:
            seleccion_2()
          elif opcion == 3:
            break
          else:
            print("❌ LA OPCION SELECCIONADA NO EXISTE")
        except ValueError:
           print(" 😣 SOLO SE PUEDE ELEGIR UNA DE LAS 3 OPCIONES QUE SE TE MUESTRA ") 

