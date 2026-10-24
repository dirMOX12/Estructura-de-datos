#Ejercicio 33. Análisis de múltiplos en un intervalo

#Solicite dos números enteros: un límite inferior y un límite superior. Compruebe que el límite inferior sea menor que el superior.

#Recorra todos los números del intervalo, incluidos sus extremos, y determine:

#Cuántos números son múltiplos de 3.
#Cuántos números son múltiplos de 5.
#Cuántos números son múltiplos de ambos números.
#La suma de los números que son múltiplos de 3, pero no de 5.

#Muestre cada resultado por separado.

límite_inferior = int(input("Ingrese el límite inferior: "))
límite_superior = int(input("Ingrese el límite superior: "))

if límite_inferior < límite_superior:
    cantidad_multiplos_3 = 0
    cantidad_multiplos_5 = 0
    cantidad_multiplos_ambos = 0
    suma_multiplos_3_no_5 = 0

    for i in range(límite_inferior, límite_superior + 1):
        if i % 3 == 0:
            cantidad_multiplos_3 += 1
            if i % 5 != 0:
                suma_multiplos_3_no_5 += i
        if i % 5 == 0:
            cantidad_multiplos_5 += 1
        if i % 3 == 0 and i % 5 == 0:
            cantidad_multiplos_ambos += 1

    print(f"Cantidad de números múltiplos de 3: {cantidad_multiplos_3}")
    print(f"Cantidad de números múltiplos de 5: {cantidad_multiplos_5}")
    print(f"Cantidad de números múltiplos de ambos (3 y 5): {cantidad_multiplos_ambos}")
    print(f"Suma de los números que son múltiplos de 3 pero no de 5: {suma_multiplos_3_no_5}")
