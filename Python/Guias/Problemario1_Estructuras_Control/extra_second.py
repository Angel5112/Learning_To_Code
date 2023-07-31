"""
Ejercicio 16:

Se introduce por teclado una hora determinada con el formato H, M, S. Se pide
calcular la hora que será dentro de un segundo.
"""


def add_second(time: list) -> str:

    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])

    if hours < 0 or minutes < 0 or seconds < 0 or minutes > 60 or seconds > 60:
        raise Exception("\nError! Time can not be a negative value or a value greater than 60 (for min and sec)...")
    elif seconds < 60:
        seconds += 1
    else:
        seconds = 0
        if minutes < 60:
            minutes += 1
        else:
            minutes = 0
            hours += 1

    return str(hours) + ":" + str(minutes) + ":" + str(seconds)


def extra_second() -> None:

    # Getting the hour in HH:MM:SS format

    time = input("Enter the hour in HH:MM:SS format: ")
    time = time.split(":")

    # Adding a second to the time

    time = add_second(time)
    print(f"\nAfter adding one second, the time is {time}")


if __name__ == '__main__':
    extra_second()
