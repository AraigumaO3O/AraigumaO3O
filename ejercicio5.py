# Ejercicio 5: Descuento en compras
# Instrucciones:
# - Pedir al usuario el monto total de la compra.
# - Si el monto es mayor a $50.000, aplicar un 15% de descuento.
# - Mostrar el monto final a pagar y el descuento aplicado.

# Tu código aquí:

# Pedir el monto total:
monto = float(input("Ingresa el monto total de la compra: "))

# Verificar si corresponde descuento:
if monto > 50000:
    descuento = monto * 0.15
    total = monto - descuento
else:
    descuento = 0
    total = monto

# Calcular el monto final y el descuento si es necesario:


# Mostrar el resultado:
# print("El total a pagar es:", ...)
print("Descuento aplicado: $", round(descuento, 2))
print("El total a pagar es: $", round(total, 2))
