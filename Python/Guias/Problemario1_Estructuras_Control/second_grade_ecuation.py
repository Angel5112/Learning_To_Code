"""
Ejercicio 4:

Diseñar un algoritmo para resolver una ecuación de segundo grado.
"""

from math import sqrt


def calculate_discriminant(a: float, b: float, c: float) -> float:
    return (b ** 2) - 4 * a * c


def solve_equation(a: float, b: float, discriminant: float) -> None:

    if discriminant < 0:
        print("\nThe equation has a non-real number solution!")
    elif discriminant == 0:
        solution = round((-1 * b) / (2 * a), 2)
        print(f"\nThe discriminant equals 0, so there is a repeated real number solution, which is: {solution}")
    else:
        first_solution = ((-1 * b) + sqrt(discriminant)) / (2 * a)
        second_solution = ((-1 * b) - sqrt(discriminant)) / (2 * a)

        print("\nThe discriminant is positive, so there are 2 real number solutions, which are:" +
              f"\n First solution: {first_solution}" +
              f"\n Second solution: {second_solution}")


def second_grade_ecuation() -> None:

    # Getting the ecuation terms

    second_grade_element = float(input("Enter the cuoficient of the second grade term: "))
    first_grade_element = float(input("Enter the cuoficiente of the first grade term: "))
    independent_term = float(input("Enter the independent term: "))

    # Calculate discriminant

    discriminant = calculate_discriminant(second_grade_element, first_grade_element, independent_term)

    # Solve the equation

    solve_equation(second_grade_element, first_grade_element, discriminant)


if __name__ == '__main__':
    second_grade_ecuation()
