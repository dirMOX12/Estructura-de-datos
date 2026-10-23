#Ejercicio 21. Conteo directo

#Solicite un número entero positivo n e imprima todos los números desde 1 hasta n, incluyendo ambos extremos.

#Utilice un ciclo for con range().

n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    for i in range(1, n + 1):
        print(i)


        