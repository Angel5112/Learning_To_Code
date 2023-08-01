"""
Ejercicio 24:

Dada una secuencia de enteros terminada en cero, elabore un algoritmo para
resolver cada uno de los siguientes problemas:

a) Calcular el promedio de dicha secuencia.
b) Calcular el porcentaje de números impares y el porcentaje de números pares.
c) Calcular la cantidad de valores iguales a un valor N dado por el usuario.
d) Contar la cantidad de números primos
"""


def create_sequence() -> list:

    sequence = []

    while True:
        num = int(input("Enter the next number of the sequence (Ends with zero): "))
        if num != 0:
            sequence.append(num)
        else:
            break

    return sequence


def find_average(sequence: list) -> None:

    sum = 0
    length = len(sequence)

    for i in range(0, length):
        sum += sequence[i]

    average = round(sum / length, 2)
    print(f"\nThe average of the sequence is {average}")


def find_percentage(sequence: list) -> None:

    odds = 0
    evens = 0
    length = len(sequence)

    for i in range(0, length):
        if sequence[i] % 2 == 0:
            evens += 1
        else:
            odds += 1

    percentage_odds = (odds * 100) / length
    percentage_evens = (evens * 100) / length

    print(f"\nThe percentage of odds is {percentage_odds}% and the percentage of evens is {percentage_evens}%")


def find_value(sequence: list) -> None:

    num = int(input("Enter the number to see how many times it appears in the sequence: "))
    print(f"\nThe number {num} can be found {sequence.count(num)} times in the sequence!")


def find_primes(sequence: list) -> None:

    primes = 0

    for i in range(0, len(sequence)):
        if sequence[i] > 1:
            # Iterate from 2 to n / 2
            for j in range(2, int(sequence[i] / 2) + 1):
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if sequence[i] % j == 0:
                    break
            else:
                primes += 1

    print(f"The number of primes in the sequence is: {primes}")


def integer_sequence() -> None:

    # Getting the sequence

    sequence = create_sequence()

    # App menu

    is_running = True

    while is_running:

        print("\nSelect an option: " +
              "\na. Find sequence's average" +
              "\nb. Find the percentage of odds and evens" +
              "\nc. Find the amount of an N value in the sequence" +
              "\nd. Find the amount of prime numbers in the sequence" +
              "\ne. Close the application\n")

        option = input("Enter your decision...  ")

        if option.lower() == 'a':
            find_average(sequence)
        elif option.lower() == 'b':
            find_percentage(sequence)
        elif option.lower() == 'c':
            find_value(sequence)
        elif option.lower() == 'd':
            find_primes(sequence)
        else:
            is_running = False


if __name__ == '__main__':
    integer_sequence()
