#Ejercicio 20. Conteo de consonantes

#Solicite una frase y cuente las consonantes que contiene. Ignore espacios, números, signos de puntuación y vocales.

#El programa debe funcionar tanto con letras mayúsculas como minúsculas.


frase = input("Ingrese una frase: ")
contador_consonantes = 0

for caracter in frase:
    if (caracter >= 'A' and caracter <= 'Z') or (caracter >= 'a' and caracter <= 'z'):
        if caracter not in "aeiouAEIOU":
            contador_consonantes += 1

print(f"Total de consonantes encontradas: {contador_consonantes}")



