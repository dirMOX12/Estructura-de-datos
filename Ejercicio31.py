#Ejercicio 31. Clasificación de una secuencia de números

#Solicite al usuario un número entero positivo n. A continuación, utilice un ciclo for para leer n números enteros.

#El programa debe determinar:

#Cuántos números son positivos, cuántos son negativos y cuántos son iguales a cero.
#Cuántos números son pares y cuántos son impares.
#La suma de todos los números ingresados.

#Al finalizar, muestre los resultados de cada clasificación y la suma total.


n = int(input("Ingrese un número entero positivo n: "))
if n > 0:
    cantidad_positivos = 0
    cantidad_negativos = 0
    cantidad_ceros = 0
    cantidad_pares = 0
    cantidad_impares = 0
    suma_total = 0

    for i in range(n):
        suma_total += i

        if i > 0:
            cantidad_positivos += 1
        elif i < 0:
            cantidad_negativos += 1
        else:
            cantidad_ceros += 1

        if i % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1

    print(f"Cantidad de números positivos: {cantidad_positivos}")
    print(f"Cantidad de números negativos: {cantidad_negativos}")
    print(f"Cantidad de ceros: {cantidad_ceros}")
    print(f"Cantidad de números pares: {cantidad_pares}")
    print(f"Cantidad de números impares: {cantidad_impares}")
    print(f"Suma total de los números ingresados: {suma_total}")