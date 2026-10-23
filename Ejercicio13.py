#Ejercicio 13. Clasificación de un número

#Solicite un número entero e indique si es positivo, negativo o igual a cero. Si es positivo, determine además si es par o impar.

#El programa debe combinar condiciones utilizando if, elif y else.

numero = int(input("Ingrese un número entero: "))
if numero > 0:
    if numero % 2 == 0:
        print(f"El número {numero} es positivo y par.")
    else:
        print(f"El número {numero} es positivo e impar.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:   
    print("El número es igual a cero.")
    