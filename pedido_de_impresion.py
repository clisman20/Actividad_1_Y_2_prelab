#en la carpeta dice actividad 1 y 2, pero me equivoque, es la 1, personal.
#entendamos cuales son las entradas: son la cantidad de paquetes, y el tamaño de cada paquete
#las restricciones son que solo puede ingresar un numero del 1 al 50 por cada tamaño del paquete, incluyendo estos 2 limites.
#la salida es el total de paquetes, y el tamaño de cada paquete, y el total de tamaño de todos los paquetes, y el precio total a pagar.

from dbm import error


from copy import error


def calcular_subtotal(total_paginas, precio_por_pagina):
    return total_paginas * precio_por_pagina

paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]

PRECIO_PAGINA = 2
PORCENTAJE_DESCUENTO = 0.10

total_paginas = 0
cantidad_paquetes_aceptados = 0



for indice in range(len(paquetes)):
    print(paquetes[indice])
    try:
        cantidad = int(input("cantidad de paginas del paquete (1-50): "))
    except ValueError:
        print("Error: debes ingresar un numero entero, su paquete enviado se omitira")
        continue

    if cantidad < 1 or cantidad > 50:
        print("Ingrese una cantidad válida entre 1 y 50, incluyendo ambos límites. Su paquete será omitido.")
        continue
    total_paginas += cantidad
    cantidad_paquetes_aceptados += 1

subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
descuento = 0
if total_paginas > 100:
    descuento = subtotal * PORCENTAJE_DESCUENTO

total_a_pagar = subtotal - descuento

print("\n--- RESUMEN DEL PEDIDO ---")

if cantidad_paquetes_aceptados == 0:
    print("No se generó un pedido.")

print("Paquetes aceptados:", cantidad_paquetes_aceptados)
print("Total de páginas:", total_paginas)
print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total a pagar:", total_a_pagar)
