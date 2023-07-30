"""
Ejercicio 8:

Tres numero naturales A, B y C forman una terna pitagórica cuando se cumple la
relación A^2 + B^2 = C^2. Escriba un algoritmo que leídos tres números diga si forman una
terna pitagórica.

"""


def is_pythagorean_triple(a: int, b: int, c: int) -> bool:

    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)

    if a + b == c:
        return True

    return False


def pythagorean_triple() -> None:

    # Gettting three natural numbers

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

    # Determine if the numbers represent a pythagorean triple

    if is_pythagorean_triple(first_number, second_number, third_number):
        print("\nThe numbers represent a pythagorean triple!")
    else:
        print("\nThe numbers DO NOT represent a pythagorean triple!")


if __name__ == '__main__':
    pythagorean_triple()
