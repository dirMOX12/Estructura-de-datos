#Ejercicio 9. Mayor de tres números

#Solicite tres números diferentes y determine cuál es el mayor. Resuelva el problema mediante estructuras condicionales, sin utilizar la función max().

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 > num2 and num1 > num3:
    print(f"El primer número ({num1}) es el mayor.")
elif num2 > num1 and num2 > num3:
    print(f"El segundo número ({num2}) es el mayor.")
else:
    print(f"El tercer número ({num3}) es el mayor.")