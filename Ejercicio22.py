#Ejercicio 22. Conteo inverso

#Solicite un número entero positivo e imprima una cuenta regresiva desde ese número hasta 1.

#Al finalizar, muestre el mensaje "¡Despegue!".

#Utilice range() con un paso negativo.

n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    for i in range(n, 0, -1):
        print(i)
    print("¡Despegue!")

    