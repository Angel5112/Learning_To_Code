"""
Ejercicio 17:

Un capital C se coloca a un interés anual R. Al cabo de cuantos años se doblará?
"""


def find_number_years(capital: float, rate: float) -> int:

    years = 0
    double_capital = capital * 2

    while True:
        capital += (capital * rate) / 100
        years += 1

        if capital >= double_capital:
            return years


def doubly_interest() -> None:

    # Getting the capital and the interest rate

    capital = float(input("Enter the amount of capital: "))
    interest_rate = float(input("Enter the interest rate per year (%): "))

    # Find the number of years that it would take for that capital to double

    years_to_double = find_number_years(capital, interest_rate)
    print(f"\nThe number of years required to double: " +
          f"\n Original capital: {capital}" +
          f"\n Yearly Interest Rate: {interest_rate}" +
          f"\n Years to Double: {years_to_double}")


if __name__ == '__main__':
    doubly_interest()
