#Ejercicio 12. Descuento en una compra

#Solicite el valor de una compra y aplique las siguientes reglas:

#Si el valor es igual o superior a $200.000 COP, aplique un descuento del 15 %.
#Si el valor es igual o superior a $100.000 COP, pero inferior a $200.000 COP, aplique un descuento del 10 %.
#En los demás casos, no aplique descuento.
#Muestre el valor original, el descuento y el total a pagar.

valor_compra = float(input("Ingrese el valor de la compra en COP: "))
if valor_compra >= 200000:
    descuento = valor_compra * 0.15
    total_a_pagar = valor_compra - descuento
    print(f"Valor original: {valor_compra} COP")
    print(f"Descuento aplicado: {descuento} COP")
    print(f"Total a pagar: {total_a_pagar} COP")

elif valor_compra >= 100000:
    descuento = valor_compra * 0.10
    total_a_pagar = valor_compra - descuento
    print(f"Valor original: {valor_compra} COP")
    print(f"Descuento aplicado: {descuento} COP")
    print(f"Total a pagar: {total_a_pagar} COP")

else:
    print(f"Valor original: {valor_compra} COP")
    print(f"Descuento aplicado: 0.0 COP")
    print(f"Total a pagar: {valor_compra} COP")
