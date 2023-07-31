"""
Ejercicio 20:

La amistad cuadrática entre números se podría explicar en la siguiente
conversación entre el numero 13 y el numero 16

16 al 13: Quiero ofrecerte mi homenaje amigo, mi cuadrado es 256 cuya suma
de guarismos es 13

13 al 16: Agradezco tu bondad y quiero retribuirla en la misma forma. Mi
cuadrado es 169 cuya suma de guarismos es 16.

Dado este pequeño fragmento de “El hombre que calculaba” realice un programa que
diga si dos números son amigos matemáticos
"""


def is_quadratic_friendship(x: int, y: int) -> bool: # x = 16, y = 13

    squared_x = str(pow(x, 2))
    squared_y = str(pow(y, 2))
    is_friendship = False
    figures_x = 0
    figures_y = 0

    # Determine quadratic friendship

    for num in squared_x:
        figures_x += int(num)

    for num in squared_y:
        figures_y += int(num)

    if figures_x == y and figures_y == x:
        is_friendship = True

    return is_friendship


def qudratic_friendship() -> None:

    # Getting the two numbers

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    # Finding quadratic friendship

    quadratic_friend = is_quadratic_friendship(first_number, second_number)

    if quadratic_friend:
        print(f"\n{first_number} and {second_number} have a quadratic friendship!")
    else:
        print(f"\n{first_number} and {second_number} DO NOT have a quadratic friendship")


if __name__ == '__main__':
    qudratic_friendship()
