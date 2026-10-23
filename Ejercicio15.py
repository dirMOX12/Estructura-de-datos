#Ejercicio 15. Validación de una contraseña

#Solicite al usuario una contraseña y compruebe si cumple las siguientes condiciones:

#Tiene al menos 8 caracteres.
#Contiene al menos un número.
#No es igual a la palabra "python123".

#Para este ejercicio, evalúe la longitud con len(), la presencia de números con los métodos de cadenas y las condiciones mediante operadores lógicos.

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8:
    caracteres_validos = False
    for numeros in contraseña:
        if numeros in "0123456789":
            caracteres_validos = True
    if caracteres_validos:
        if contraseña != "python123":
            print("La contraseña es válida.")
        else:
            print("Error: La contraseña no puede ser 'python123'.")
    else:
        print("Error: La contraseña debe contener al menos un número.")
else:
    print("Error: La contraseña debe tener al menos 8 caracteres.")
