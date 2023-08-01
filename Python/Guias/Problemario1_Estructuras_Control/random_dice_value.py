"""
Ejercicio 23:

Con dos dados al azar se pueden obtener los números: 2..12. Por ejemplo, para
obtener el número 2, la única forma es que ambos salgan con el uno; para obtener un
cuatro existen dos combinaciones posibles, que ambos tengan un dos o que un dado
salga con uno y el otro con tres. Diseñe un algoritmo (utilizando estructuras iterativas)
que leyendo un valor N, validado entre 2 y 12, genere cuáles son las combinaciones
posibles, sin repetición, para ese valor.
"""


def validate_number(n: int) -> bool:
    if 2 <= n <= 12:
        return True

    return False


def dice_combination(n: int) -> set:

    combinations = set()
    aux_list = []

    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                aux_list.append(i)
                aux_list.append(j)
                aux_list.sort()
                combinations.add(tuple(aux_list))
                aux_list.clear()

    return combinations


def random_dice_value() -> None:

    # Getting the valid number between 2 and 12

    num = int(input("Enter the number: "))

    if validate_number(num):

        # Finding the possible dice combination

        valid_combinations = dice_combination(num)
        print(f"\nIn order to get {num}, the only valid combinations are: {valid_combinations}")
    else:
        raise Exception("Error! Number is not between 2 and 12...")


if __name__ == '__main__':
    random_dice_value()
