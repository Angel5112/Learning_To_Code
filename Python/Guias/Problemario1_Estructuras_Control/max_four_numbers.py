"""
Ejercicio 5:

Escribir un algoritmo que lea cuatro números y a continuación imprima el mayor de
ellos.
"""


def max_four_numbers() -> None:

    # Getting the four numbers

    numbers = [float(input(f"Enter a new number ({i + 1}): ")) for i in range(0, 4)]

    # Getting the max number

    print(f"\nThe maximum number in {numbers} is: {max(numbers)}")


if __name__ == '__main__':
    max_four_numbers()
