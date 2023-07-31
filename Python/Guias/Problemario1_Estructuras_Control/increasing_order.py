"""
Ejercicio 14:

Leer tres números del teclado y deducir si se han introducido en orden creciente.
"""


def increasing_order() -> None:

    # Getting the three numbers

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    third_number = float(input("Enter the third number: "))

    # Determine if they were introduced in increasing order

    if first_number <= second_number <= third_number and first_number <= third_number:
        print("The numbers were introduced in increasing order!")
    else:
        print("The numbers WERE NOT introduced in increasing order!")


if __name__ == '__main__':
    increasing_order()
