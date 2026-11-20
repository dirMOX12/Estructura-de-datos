#Ejercicio 6. Promedio de calificaciones

#Solicite tres calificaciones numéricas, calcule su promedio e imprima el resultado. Si el promedio es igual o superior a 3.0, muestre el mensaje "Aprobado"; de lo contrario, muestre "Reprobado".

calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
print(f"El promedio de las calificaciones es: {promedio}")
if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado") 

