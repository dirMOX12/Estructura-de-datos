#Ejercicio 14. Calculadora con selección de operación

#Solicite dos números y un símbolo de operación (+, -, * o /).

#Según el símbolo introducido, ejecute la operación correspondiente utilizando if-elif-else.

#Si el símbolo no es válido, muestre un mensaje de error. Controle también la división entre cero.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese el símbolo de operación (+, -, * o /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Error: Símbolo de operación no válido.")