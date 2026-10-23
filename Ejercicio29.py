#Ejercicio 29. Número mayor y menor de una secuencia

#Solicite una cantidad n de números y léalos uno por uno mediante un ciclo for.

#Determine cuál fue el mayor y cuál fue el menor, sin utilizar max(), min() ni listas.

#Inicialice las variables de comparación utilizando el primer número ingresado o una estrategia equivalente.

n = int(input("Ingrese la cantidad de números a comparar: "))
if n > 0:
    primer_numero = float(input("Ingrese el número 1: "))
    mayor = primer_numero
    menor = primer_numero

    for i in range(2, n + 1):
        numero = float(input(f"Ingrese el número {i}: "))
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero

    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")


    