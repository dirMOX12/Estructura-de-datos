#Ejercicio 34. Registro de ventas de una tienda

#Una tienda necesita calcular el resultado de sus ventas diarias. Solicite cuántas ventas se van a registrar y, mediante un ciclo for, pida el valor de cada venta.

#El programa debe calcular:

#El total de dinero vendido.
#El valor promedio de las ventas.
#La venta de mayor value.
#La cantidad de ventas superiores a $100.000 COP.
#La cantidad de ventas inferiores a $20.000 COP.

#Los valores ingresados deben ser mayores que cero. Si una venta no cumple esta condición, solicite nuevamente el dato.

#No utilice listas ni las funciones max() o min().

n = int(input("Ingrese la cantidad de ventas a registrar: "))
if n > 0:
    total_ventas = 0
    venta_mayor = 0
    cantidad_superiores_100k = 0
    cantidad_inferiores_20k = 0

    for i in range(1, n + 1):
        while True:
            venta = float(input(f"Ingrese el valor de la venta {i} (mayor que cero): "))
            if venta > 0:
                break
            else:
                print("Valor inválido. Por favor, ingrese un valor mayor que cero.")

        total_ventas += venta

        if venta > venta_mayor:
            venta_mayor = venta

        if venta > 100000:
            cantidad_superiores_100k += 1
        elif venta < 20000:
            cantidad_inferiores_20k += 1

    promedio_ventas = total_ventas / n

    print(f"Total de dinero vendido: ${total_ventas} COP")
    print(f"Valor promedio de las ventas: ${promedio_ventas} COP")
    print(f"Venta de mayor value: ${venta_mayor} COP")
    print(f"Cantidad de ventas superiores a $100.000 COP: {cantidad_superiores_100k}")
    print(f"Cantidad de ventas inferiores a $20.000 COP: {cantidad_inferiores_20k}")