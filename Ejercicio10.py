#Ejercicio 10. Acceso a un evento

#Solicite la edad de una persona y pregunte si tiene una entrada válida, almacenando la respuesta como un valor booleano.

#Permita el acceso únicamente si la persona tiene 18 años o más y posee una entrada válida. Utilice el operador lógico and.

edad = int(input("Ingrese su edad: "))
entrada_valida = input("¿Tiene una entrada válida? (si/no): ") == "si"

if edad >= 18 and entrada_valida:
    print("Puede acceder al evento.")
else:
    print("No puede acceder al evento.")

