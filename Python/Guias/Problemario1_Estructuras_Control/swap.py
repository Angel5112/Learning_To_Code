"""
Ejercicio 11:

Realizar un algoritmo que permita intercambiar entre si los valores de dos
variables A y B.
"""


def swap() -> None:

    # Getting the values to change

    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))

    # Changing the value

    a, b = b, a
    print(f"\nNow A = {a} and B = {b}!")


if __name__ == '__main__':
    swap()
