"""
Ejercicio 5:

Dada una cantidad en bolívares, obtener la equivalencia en dólares, asumiendo que la unidad cambiaría es un
dato desconocido.
"""

DOLLAR = 29.314


def change_currency(bolivars: float) -> float:
    return bolivars / DOLLAR


def bolivars_to_dollars() -> None:

    # Getting the amount of bolivars

    bolivars = float(input("Enter your amount of bolivars: "))

    # Change of currency

    dollars = round(change_currency(bolivars), 2)
    print(f"\n{bolivars} Bs. --------> {dollars} $")


if __name__ == '__main__':
    bolivars_to_dollars()
