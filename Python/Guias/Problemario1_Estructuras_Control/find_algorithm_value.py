"""
Ejercicio 7:

Cual es el valor impreso del siguiente algoritmo

Inicio
    Suma  25
    Código  15
    Total  45
    SBruto  Suma + Código
    Escribir(SBruto)
Fin
"""


def find_algorithm_value() -> None:

    # Writing algorithm

    sum = 25
    code = 15
    total = 45
    brute_salary = sum + code
    print(f"The value of the algorithm is: {brute_salary}")


if __name__ == '__main__':
    find_algorithm_value()
