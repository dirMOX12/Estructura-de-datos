#Ejercicio 27. Conteo de múltiplos

#Solicite dos números enteros positivos n y k. Recorra los números desde 1 hasta n y cuente cuántos son múltiplos de k.

#Muestre los múltiplos encontrados y la cantidad total. Para este ejercicio, utilice una condición con el operador módulo.

n = int(input("Ingrese un número entero positivo n: "))
k = int(input("Ingrese un número entero positivo k: "))
if n > 0 and k > 0:
    cantidad_multiplos = 0
    print(f"Múltiplos de {k} desde 1 hasta {n}:")
    for i in range(1, n + 1):
        if i % k == 0:
            print(i)
            cantidad_multiplos += 1
    print(f"Cantidad total de múltiplos de {k} encontrados: {cantidad_multiplos}")

    