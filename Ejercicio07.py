#Ejercicio 7. Número par o impar

#Solicite un número entero e indique si es par o impar. El programa debe utilizar el operador módulo (%) y una estructura condicional if-else.

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
