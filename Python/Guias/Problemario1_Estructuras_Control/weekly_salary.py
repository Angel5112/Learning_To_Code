"""
Ejercicio 13:

Los trabajadores de una fabrica de autos tiene tres turnos: mañana, noche y
festivos. Se desea calcular el sueldo semanal a razón de 5 días de trabajo a la semana
según la siguiente tarifa:
 600 Ptas./hora turno de la mañana
 800 Ptas./hora turno de la tarde
1000 Ptas./hora día festivo.
Se debe leer el turno y el número de horas trabajadas.
"""


# Rates per turn

rates = {
    "morning": 600,
    "afternoon": 800,
    "holiday": 1000
}


def calculate_salary(work_turn: str, daily_hours: float) -> float:
    try:
        return round(5 * daily_hours * rates[work_turn.lower()], 2)
    except KeyError as e:
        print(repr(e) + "! Enter a valid work turn")


def weekly_salary() -> None:

    # Getting the turn and daily work hours

    turn = input("Enter the work turn (Morning, Afternoon, Holiday): ")
    work_hours = float(input("Enter the amount of daily work hours: "))

    # Calculate the salary of 5 days worth of work

    salary = calculate_salary(turn, work_hours)
    print("\nThe worker salary consists of: " +
          f"\n Daily work hours: {work_hours}" +
          f"\n Turn: {turn}" +
          f"\n Weekly Salary: {salary}")


if __name__ == '__main__':
    weekly_salary()
