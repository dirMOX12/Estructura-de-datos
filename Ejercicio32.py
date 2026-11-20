#Ejercicio 32. Estadísticas de calificaciones

#Un docente desea analizar las calificaciones de un grupo de estudiantes. Solicite la cantidad de estudiantes y, mediante un ciclo for, pida la calificación de cada uno en una escala de 0.0 a 5.0.

#El programa debe:

#Validar que cada calificación esté dentro del rango permitido.
#Contar cuántos estudiantes aprobaron con una nota igual o superior a 3.0.
#Contar cuántos estudiantes reprobaron.
#Calcular el promedio general del grupo.
#Identificar cuántos estudiantes obtuvieron una calificación igual o superior a 4.5.

#Si una calificación no es válida, no debe incluirse en los cálculos y debe solicitarse nuevamente.

n = int(input("Ingrese la cantidad de estudiantes: "))
if n > 0:
    cantidad_aprobados = 0
    cantidad_reprobados = 0
    suma_calificaciones = 0
    cantidad_altas = 0

    for i in range(1, n + 1):
        while True:
            calificacion = float(input(f"Ingrese la calificación del estudiante {i} (0.0 - 5.0): "))
            if 0.0 <= calificacion <= 5.0:
                break
            else:
                print("Calificación inválida. Por favor, ingrese un valor entre 0.0 y 5.0.")

        suma_calificaciones += calificacion

        if calificacion >= 3.0:
            cantidad_aprobados += 1
        else:
            cantidad_reprobados += 1

        if calificacion >= 4.5:
            cantidad_altas += 1

    promedio_general = suma_calificaciones / n

    print(f"Cantidad de estudiantes aprobados: {cantidad_aprobados}")
    print(f"Cantidad de estudiantes reprobados: {cantidad_reprobados}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")
    print(f"Cantidad de estudiantes con calificación igual o superior a 4.5: {cantidad_altas}")