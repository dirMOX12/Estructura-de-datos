#Ejercicio 4. Área y perímetro de un rectángulo

#Solicite la base y la altura de un rectángulo. Calcule su área y su perímetro e imprima los resultados. Antes de realizar los cálculos, compruebe que ambas dimensiones sean mayores que cero.

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
if base > 0 and altura > 0:
    area = base * altura
    perimetro = 2 * (base + altura)
    print(f"Área del rectángulo: {area}")
    print(f"Perímetro del rectángulo: {perimetro}")
else:  
    print("Error: La base y la altura deben ser mayores que cero.")
