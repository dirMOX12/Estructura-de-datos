#Ejercicio 30. Detección de números primos

#Solicite un número entero mayor que 1 y determine si es primo.

#Utilice un ciclo for para comprobar si existe algún divisor entre 2 y el número anterior al valor ingresado.

#Si encuentra un divisor exacto, registre que el número no es primo. Al finalizar, muestre el resultado.

#No utilice funciones externas para determinar si un número es primo.

n = int(input("Ingrese un número entero mayor que 1: "))
if n > 1:
    Numero_primo = True
    for i in range(2, n):
        if n % i == 0:
            Numero_primo = False
    if Numero_primo:
        print(f"El número {n} es primo.")
    else:
        print(f"El número {n} no es primo.")
