"""
Ejercicio 8:

Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá
pagar finalmente por su compra.

"""


def calculate_total(sale_total: float) -> float:
    return sale_total - (sale_total * 0.15)


def calculate_store_discount() -> None:

    # Getting total cost

    sale_total = float(input("Enter the sale's total: "))

    # Calculate total with applied discount (15%)

    total = round(calculate_total(sale_total), 2)
    print(f"\nThe sale total will be: {total}")


if __name__ == '__main__':
    calculate_store_discount()
