#Ejercicio 35. Suma selectiva de números

#Solicite un número entero positivo n y recorra los números desde 1 hasta n.

#El programa debe calcular tres sumas diferentes:

#La suma de todos los números pares.
#La suma de todos los números impares.
#La suma de los números que son múltiplos de 3.

#Al finalizar, muestre las tres sumas y determine cuál de ellas es la mayor. Si dos o más sumas tienen el mismo valor máximo, indíquelo.


n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    suma_pares = 0
    suma_impares = 0
    suma_multiplos_3 = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i

        if i % 3 == 0:
            suma_multiplos_3 += i

    print(f"Suma de números pares: {suma_pares}")
    print(f"Suma de números impares: {suma_impares}")
    print(f"Suma de múltiplos de 3: {suma_multiplos_3}")

    max_suma = max(suma_pares, suma_impares, suma_multiplos_3)
    max_count = sum([suma_pares == max_suma, suma_impares == max_suma, suma_multiplos_3 == max_suma])

    if max_count > 1:
        print("Hay más de una suma con el valor máximo.")
    else:
        if max_suma == suma_pares:
            print("La mayor suma es la de números pares.")
        elif max_suma == suma_impares:
            print("La mayor suma es la de números impares.")
        else:
            print("La mayor suma es la de múltiplos de 3.")