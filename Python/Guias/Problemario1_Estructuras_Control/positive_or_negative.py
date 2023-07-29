"""
Ejercicio 2:

Deducir si un número es negativo o positivo.
"""


def is_positive(number: float) -> bool:
    if number >= 0:
        return True

    return False


def positive_or_negative() -> None:

    # Getting the number

    number = float(input("Enter the number: "))

    # Determine if the number is positive

    if is_positive(number):
        print("The number is positive (Number >= 0)")
    else:
        print("The number is negative (Number < 0)")


if __name__ == '__main__':
    positive_or_negative()
