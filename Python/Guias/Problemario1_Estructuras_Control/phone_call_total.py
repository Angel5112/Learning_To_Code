"""
Ejercicio 12:

Escriba un Algoritmo, que determine el monto a pagar de una llamada
telefónica teniendo en cuenta lo siguiente: toda llamada que dure hasta 3
minutos tiene un costo de 35 Bs. Por cada minuto adicional se cobra una
tari fa de 15 Bs. Se debe leer el tiempo de llamadas en el formato hh:mm.
Salida: tiempo de llamada y costo
"""


def calculate_total(call_duration: list) -> int:

    hours = int(call_duration[0])
    minutes = int(call_duration[1])

    if hours < 0 or minutes < 0:
        raise Exception("Error: Hours or Minutes can not be less than zero!")
    elif hours == 0 and minutes <= 3:
        return 35
    else:
        minutes -= 3
        return 35 + (hours * 60 * 15) + (minutes * 15)


def phone_call_total() -> None:

    # Getting the duration of the call

    duration = input("Enter the duration of the call in the hh:mm format: ")
    time = duration.split(":")

    # Calculate the total

    total = calculate_total(time)
    print(f"A call duration of {time[0]}:{time[1]} will cost {total} Bs.")


if __name__ == '__main__':
    phone_call_total()
