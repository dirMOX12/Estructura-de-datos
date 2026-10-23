#Ejercicio 11. Año bisiesto

#Solicite un año entero y determine si es bisiesto.
#Un año es bisiesto si es divisible entre 400, o si es divisible entre 4 pero no entre 100.
#Utilice operadores aritméticos, comparaciones, operadores lógicos y una estructura condicional.

año = int(input("Ingrese un año: "))
if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
