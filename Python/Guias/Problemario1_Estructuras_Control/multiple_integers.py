"""
Ejercicio 21:

Escriba un algoritmo que:

a) Dado un grupo de números enteros (terminado en -1), calcule e imprima el cubo de
cada uno de estos números.

b) Dados como datos 270 números enteros, obtenga la suma de los números impares
y el promedio de los números pares.

c) Dados como datos N números enteros, determine cuántos de ellos son pares y
cuántos impares.
"""


def first_option() -> None:

    nums = []
    num = 0

    while num != -1:
        num = int(input("Enter the next number of the series (It will end at -1): "))
        if num != -1:
            nums.append(num)

    cube_nums = list(map(lambda x: pow(x, 3), nums))
    print(f"\nThe original numbers are: {nums}" +
          f"\nThe cubed numbers are: {cube_nums}")


def second_option() -> None:

    odds_sum = 0
    even_sum = 0
    even_amount = 0

    for i in range(1, 271):
        if i % 2 == 0:
            even_sum += i
            even_amount += 1
        else:
            odds_sum += i

    print(f"\nThe sum of odd numbers are: {odds_sum}" +
          f"\nThe average of even numbers is: {even_sum / even_amount}")


def third_option() -> None:

    odd = 0
    even = 0

    nums_quantity = int(input("Enter the amount of numbers to record: "))

    for i in range(0, nums_quantity):
        num = int(input(f"Enter the next number ({i}): "))

        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print(f"\nThe amount of even numbers is: {even}" +
          f"\nThe amount of odd numbers is: {odd}")

def multiple_integers() -> None:

    # App menu

    is_running = True

    while is_running:

        print("\nSelect the type of operation desired (a, b, c, d): " +
              "\n a - Enter a group of integers (while -1 is not the number) to show the cube root of each" +
              "\n b - Obtain the sum between the odd numbers and the average of even numbers (from 1 to 270)" +
              "\n c - Enter n numbers to determine how many of them are even or odd" +
              "\n d - Close the application\n")

        option = input("Enter your decision...  ")

        # Handling decision

        if option.lower() == 'a':
            first_option()
        elif option.lower() == 'b':
            second_option()
        elif option.lower() == 'c':
            third_option()
        else:
            is_running = False


if __name__ == '__main__':
    multiple_integers()
