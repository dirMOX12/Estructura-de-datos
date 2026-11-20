#Ejercicio 5. Conversión de segundos

#Solicite una cantidad entera de segundos y conviértala en horas, minutos y segundos restantes.

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos son equivalentes a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
