#Ejercicio 24. Conteo inverso con saltos

#Solicite un número entero n mayor o igual que 10. Imprima los números desde n hasta llegar al primer valor de la secuencia que sea mayor que cero, disminuyendo de 3 en 3.

#Utilice range() con un paso de -3.

n = int(input("Ingrese un número entero mayor o igual que 10: "))
if n >= 10:
    for i in range(n, 0, -3):
        print(i)

