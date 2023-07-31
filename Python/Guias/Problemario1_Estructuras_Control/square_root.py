"""
Ejercicio 18:

Calcular la raíz cuadrada de un número, si este es positivo calcular su resultado, si
no, visualizar un mensaje de raíz imaginaria.
"""


from math import sqrt


def find_sqrt(x: float) -> str:

    if x > 0:
        return str(round(sqrt(x), 2))
    else:
        return str(round(sqrt(-1 * x), 2)) + "i"


def square_root() -> None:

    # Getting the number

    number = float(input("Enter the number: "))

    # Find the square root of the number

    square_r = find_sqrt(number)
    print(f"\nThe square root of {number} is {square_r}")


if __name__ == '__main__':
    square_root()
