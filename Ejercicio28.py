#Ejercicio 28. Promedio de números ingresados

#Solicite al usuario cuántos números desea ingresar. Después, utilice un ciclo for para solicitar esa cantidad de números, acumular sus valores y calcular el promedio.

#Al finalizar, muestre la suma y el promedio.

#No almacene los números en una lista.

n = int(input("Ingrese la cantidad de números que desea ingresar: "))
if n > 0:
    suma_total = 0
    for i in range(n):
        numero = float(input(f"Ingrese el número {i + 1}: "))
        suma_total += numero
    promedio = suma_total / n
    print(f"La suma de los números ingresados es: {suma_total}")
    print(f"El promedio de los números ingresados es: {promedio}")