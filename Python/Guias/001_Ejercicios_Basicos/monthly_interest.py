"""
Ejercicio Nro. 1:

Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganara después
de un mes si el banco paga a razón de 2% mensual.
"""


def calculate_interest(capital: float) -> float:
    return capital * 0.02


def monthly_interest() -> None:
    capital = float(input("Enter the amount of funds to deposit: "))
    interest = calculate_interest(capital)
    print(f"The monthly interest at a 2% rate with a capital of {capital} will be: {interest}")


if __name__ == "__main__":
    monthly_interest()
