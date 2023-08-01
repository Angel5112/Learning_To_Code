"""
Ejercicio 22:

Escriba un algoritmo que calcule el resultado de la siguiente serie:
a) 2, 5, 7, 10, 12, 15, 17, 20, …. 1800
b) 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
c) 1 - 1/2 + 1/3 - 1/4 + ... 1/n
"""


def first_series() -> None:

    start = 2
    end = 1800
    counter = 0
    result = 2

    while start <= end:
        if counter == 0:
            start += 3
            result += start
            counter += 1
        else:
            start += 2
            result += start
            counter = 0

    print(f"\nThe series' result is {result}")


def second_series() -> None:

    result = 1
    end = int(input("Enter the last number of the series (1/n): "))

    for i in range(2, end + 1):
        result += 1 / i

    print(f"\nThe result of the series is {round(result, 2)}")


def third_series() -> None:

    result = 1
    counter = 0
    end = int(input("Enter the last number of the series (1/n): "))

    for i in range(2, end + 1):
        if counter == 0:
            result -= 1 / i
            counter += 1
        else:
            result += 1 / i
            counter = 0

    print(f"\nThe result of the series is {round(result, 2)}")


def series_result() -> None:

    # App menu

    is_running = True

    while is_running:

        print("\nSelect the next options: " +
              "\na. Result of the first series (2, 5, 7, 10, 12, 15, 17, 20, …. 1800): " +
              "\nb. Result of the second series (1 + 1/2 + 1/3 + 1/4 + ... + 1/n)" +
              "\nc. Result of the third series (1 - 1/2 + 1/3 - 1/4 + ... 1/n)" +
              "\nd. Close the application\n")

        operation = input("Enter your decision...  ")

        if operation.lower() == 'a':
            first_series()
        elif operation.lower() == 'b':
            second_series()
        elif operation.lower() == 'c':
            third_series()
        else:
            is_running = False


if __name__ == '__main__':
    series_result()
