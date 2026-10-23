#Ejercicio 23. Conteo de números pares

#Solicite un número entero positivo n e imprima todos los números pares desde 2 hasta el mayor número par menor o igual que n.

#Resuelva el problema usando el tercer argumento de range(), sin utilizar una condición if para identificar los pares.

n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    if n % 2 == 0:
        limite = n
    else:
        limite = n - 1
    for i in range(2, limite + 1, 2):
        print(i)
