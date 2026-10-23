#Ejercicio 25. Tabla de multiplicar

#Solicite un número entero e imprima su tabla de multiplicar desde el 1 hasta el 10.

#Cada línea debe presentar la operación completa y su resultado.

n = int(input("Ingrese un número entero: "))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")

