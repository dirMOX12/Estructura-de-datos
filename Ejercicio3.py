#Ejercicio 3. Calculadora de operaciones básicas

#Solicite dos números al usuario y calcule su suma, resta, multiplicación, división, división entera, módulo y potencia. Muestre cada operación con un mensaje descriptivo. El programa debe evitar errores cuando el segundo número sea cero en las operaciones de división.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
if num2 != 0:
    division = num1 / num2
    division_entera = num1 // num2
    modulo = num1 % num2
    potencia = num1 ** num2
else:
    division = "Error: División por cero"
    division_entera = "Error: División por cero"
    modulo = "Error: División por cero"
    potencia = num1 ** num2  # Potencia no depende de la división
