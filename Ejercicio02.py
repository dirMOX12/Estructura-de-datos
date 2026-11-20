#Ejercicio 2. Conversión de temperatura

#Solicite una temperatura en grados Celsius, conviértala a un número decimal y calcule su equivalente en grados Fahrenheit mediante la fórmula:
#F = C × 9/5 + 32

Celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = Celsius * 9/5 + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
