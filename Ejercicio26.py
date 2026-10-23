#Solicite un número entero positivo n y calcule la suma de todos los números desde 1 hasta n, utilizando un ciclo for.

#Al finalizar, imprima la suma total.

#No utilice fórmulas matemáticas directas ni la función sum().

n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    suma_total = 0
    for i in range(1, n + 1):
        suma_total += i
    print(f"La suma de los números desde 1 hasta {n} es: {suma_total}")

    