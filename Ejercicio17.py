#Ejercicio 17. Conteo de vocales

#Solicite una frase y recorra sus caracteres con un ciclo for. Cuente cuántas vocales contiene, sin distinguir entre mayúsculas y minúsculas.

#Al finalizar, muestre el total de vocales encontradas.

frase = input("Ingrese una frase: ")
contador_vocales = 0
vocales = "aeiouAEIOU"

for caracter in frase:
    if caracter in vocales:
        contador_vocales += 1

print(f"Total de vocales encontradas: {contador_vocales}")

