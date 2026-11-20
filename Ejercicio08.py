#Ejercicio 8. Comparación de dos números

#Solicite dos números y determine si el primero es mayor, menor o igual al segundo. Utilice los operadores de comparación y una estructura if-elif-else para presentar el resultado correspondiente.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El primer número ({num1}) es mayor que el segundo número ({num2}).")
elif num1 < num2:
    print(f"El primer número ({num1}) es menor que el segundo número ({num2}).")
else:
    print(f"El primer número ({num1}) es igual al segundo número ({num2}).")


    