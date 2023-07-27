"""
Ejercicio 11:

Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad
distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.
"""


def calculate_individual_investment(individual_investment: float, complete_investment: float) -> float:
    return (individual_investment * 100) / complete_investment


def investment_percentage() -> None:

    # Getting amount of funds invested

    first_investor = float(input("Enter the amount of money invested on the company (first owner): "))
    second_investor = float(input("Enter the amount of money invested on the company (second owner): "))
    third_investor = float(input("Enter the amount of money invested on the company (third owner): "))

    complete_investment = first_investor + second_investor + third_investor

    # Calculating each investment percentage

    first_investment = round(calculate_individual_investment(first_investor, complete_investment), 2)
    second_investment = round(calculate_individual_investment(second_investor, complete_investment), 2)
    third_investment = round(calculate_individual_investment(third_investor, complete_investment), 2)

    print(f"\nThe share of individual investment is:\n" +
          f"\n* First Investor: {first_investment}" +
          f"\n* Second Investor: {second_investment}" +
          f"\n* Third Investor: {third_investment}")


if __name__ == '__main__':
    investment_percentage()
