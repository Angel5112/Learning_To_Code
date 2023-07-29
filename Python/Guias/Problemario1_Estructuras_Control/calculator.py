"""
Ejercicio 3:

Escriba el algoritmo para simular una calculadora. Se debe leer los operandos y el
operador.
"""


def operation(a: float, b: float, operator: int) -> float:

    if operator == 1:
        return a + b
    elif operator == 2:
        return a - b
    elif operator == 3:
        return a * b
    else:
        return a / b


def interface(a: float, b: float) -> None:

    # Making the calculator

    is_running = True

    while is_running:
        print("\n***** CALCULATOR APP *****\n" +
              "\n1. Sum" +
              "\n2. Substraction" +
              "\n3. Multiplication" +
              "\n4. Division" +
              "\n0. Close calculator\n")

        operator = int(input("Your decision -> "))

        if operator < 1 or operator > 4:
            print("\nError! Selected number is not in between 1 - 4. Closing the application...")
            is_running = False
        else:
            result = round(operation(a, b, operator), 2)
            print(f"\nThe result of the operation performed between {a} and {b} equals {result}")


def calculator() -> None:

    # Getting the numbers

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    # Starting the calculator

    interface(first_number, second_number)


if __name__ == '__main__':
    calculator()
