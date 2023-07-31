"""
Ejercicio 15:

Dados dos números enteros realizar el algoritmo que calcule el cociente y el resto
(suponiendo que no existe los operadores para ello)
"""


def find_quotient(dividend: float, divisor: float) -> float:
    return dividend // divisor


def find_remainder(dividend: float, divisor: float, quotient: float) -> float:
    return dividend - (divisor * quotient)


def remainder_quotient() -> None:

    # Enter the dividend and divisor

    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))

    # Finding the quotient and remainder

    quotient = find_quotient(dividend, divisor)
    remainder = find_remainder(dividend, divisor, quotient)
    print(f"Given the dividend: {dividend} and the divisor: {divisor}, " +
          f"the quotient and remainder are {quotient}, {remainder}")


if __name__ == '__main__':
    remainder_quotient()
