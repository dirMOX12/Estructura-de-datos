#Ejercicio 18. Análisis de caracteres

#Solicite una cadena de texto y cuente por separado:

#Cuántas letras contiene.
#Cuántos dígitos contiene.
#Cuántos espacios contiene.

#Recorra la cadena carácter por carácter y utilice condicionales para clasificar cada elemento.

cadena = input("Ingrese una cadena de texto: ")
contador_letras = 0
contador_digitos = 0
contador_espacios = 0

for caracter in cadena:
    if (caracter >= 'A' and caracter <= 'Z') or (caracter >= 'a' and caracter <= 'z'):
        contador_letras += 1
    elif caracter >= '0' and caracter <= '9':
        contador_digitos += 1
    elif caracter == ' ':
        contador_espacios += 1
        

print(f"Total de letras: {contador_letras}")
print(f"Total de dígitos: {contador_digitos}")
print(f"Total de espacios: {contador_espacios}")
