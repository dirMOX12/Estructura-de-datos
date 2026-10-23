#Ejercicio 16. Recorrido de una cadena

#Solicite una palabra al usuario y utilice for para recorrer cada uno de sus caracteres. Imprima cada carácter en una línea diferente, acompañado de su posición comenzando desde 1.

#Puede utilizar una variable contadora que se incremente en cada iteración.

#Instrucción general: Resuelva los ejercicios utilizando ciclos for. No utilice ciclos while, listas ni funciones definidas por el estudiante, salvo que el enunciado indique lo contrario.

palabra = input("Ingrese una palabra: ")
for i in range(len(palabra)):
    print(f"Posición {i + 1}: {palabra[i]}")
    
