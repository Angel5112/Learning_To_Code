"""
Ejercicio 4:

Calcule la edad de una persona.
"""

# Today's date

YEAR = 2023
MONTH = 7
DAY = 26


def age_calculator() -> None:

    # Getting the birthdate

    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))

    # Calculate the age

    age = YEAR - birth_year - 1

    if MONTH > birth_month:
        age += 1
    elif MONTH >= birth_month and DAY >= birth_day:
        age += 1

    print(f"The user is {age} years old!")


if __name__ == '__main__':
    age_calculator()
