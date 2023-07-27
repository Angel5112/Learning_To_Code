"""
Ejercicio 10:

Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos.
Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera.
"""


def calculate_average_time(monday: float, wednesday: float, friday: float) -> float:
    total_time = monday + wednesday + friday
    return total_time / 3


def route_average() -> None:

    # Getting route's times

    monday_time = float(input("Enter the amount of minutes required to complete the route on Monday: "))
    wednesday_time = float(input("Enter the amount of minutes required to complete the route on Wednesday: "))
    friday_time = float(input("Enter the amount of minutes required to complete the route on Friday: "))

    # Calculate the average time

    average_time = round(calculate_average_time(monday_time, wednesday_time, friday_time), 2)
    print(f"The average time required to complete the route on any week is: {average_time} minutes")


if __name__ == '__main__':
    route_average()
