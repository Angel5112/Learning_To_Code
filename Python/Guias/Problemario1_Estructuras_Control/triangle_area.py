"""
Ejercicio 9:

Diseñar un algoritmo que calcule el área de un triangulo en función de las
longitudes de sus lados.

Area = sqrt(p(p - A)(p - B)(p - C)) en donde A, B y C son los lados y p el semiperimetro,
p = (A + B + C) / 2
"""

from math import sqrt


def find_perimeter(a: float, b: float, c: float) -> float:
    return (a + b + c) / 2


def find_area(p: float, a: float, b: float, c: float) -> float:
    try:
        return round(sqrt(p * ((p - a) * (p - b) * (p - c))), 2)
    except ValueError as e:
        print(repr(e) + "! The introduced values must be incorrect!")


def triangle_area() -> None:

    # Getting the triangle sides

    first_side = float(input("Enter the value of the triangle's first side: "))
    second_side = float(input("Enter the value of the triangle's second side: "))
    third_side = float(input("Enter the value of the triangle's third side: "))

    # Find perimeter

    perimeter = find_perimeter(first_side, second_side, third_side)

    # Calculate triangle's area

    area = find_area(perimeter, first_side, second_side, third_side)

    if area is not None:
        print(f"\nThe area of the triangle is {area} cm^2")


if __name__ == '__main__':
    triangle_area()
