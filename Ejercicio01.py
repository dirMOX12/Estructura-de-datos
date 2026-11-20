#Ejercicio 1. Datos personales

#Escriba un programa que solicite al usuario su nombre, edad, estatura en metros y si es estudiante. Almacene cada dato en una variable del tipo apropiado e imprima los valores junto con el tipo de dato de cada variable utilizando la función type().

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
estudiante = bool(input("¿Es usted estudiante? (si/no): ")) == "si"

print("Nombre:", nombre, "Tipo de dato:", type(nombre))
print("Edad:", edad, "Tipo de dato:", type(edad))   
print("Estatura:", estatura, "Tipo de dato:", type(estatura))
print("Estudiante:", estudiante, "Tipo de dato:", type(estudiante))
