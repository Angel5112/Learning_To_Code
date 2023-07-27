"""
Ejercicio 1:

Se desea calcular el salario neto semanal de un trabajador en función del número
de horas trabajadas y la tasa de impuestos d acuerdo a lo siguiente:

- Las primeras 35 horas se pagan a tarifa normal
- Las horas que pasen de 35 se pagan a 1.5 veces la tarifa normal

Las tasas de impuesto son:

- Los rimeros 50$ son libres de impuesto
- Los siguientes 40$ tienen un 25% de impuesto
- Los restantes un 45% de impuesto

Se pide mostrar el nombre del trabajador, salario bruto, tasas y salario neto.
"""

# Rates

TARIFA = 100.0


def calculate_brute_salary(work_hours: float) -> float:
    if work_hours <= 35:
        return work_hours * TARIFA
    elif work_hours > 35:
        extra_hours = work_hours - 35
        return (35 * TARIFA) + (extra_hours * (TARIFA * 1.5))


def calculate_taxes(brute_salary: float) -> float:
    if brute_salary <= 50:
        return 0
    elif 50 < brute_salary <= 90:
        return 40 * 0.25
    else:
        return (40 * 0.25) + ((brute_salary - 90) * 0.45)


def calculate_net_salary() -> None:

    # Getting required user input

    worker_name = input("Enter the name of the worker: ")
    work_hours = float(input("Enter the number of work hours: "))

    # Calculate brute salary, taxes and net salary

    brute_salary = round(calculate_brute_salary(work_hours), 2)
    taxes = round(calculate_taxes(brute_salary), 2)
    net_salary = brute_salary - taxes

    print(f"\nWorker: {worker_name}" +
          f"\nWork hours: {work_hours}"
          f"\nHourly rate: {TARIFA}" +
          f"\nBrute salary: {brute_salary}" +
          f"\nTaxes: {taxes}" +
          f"\nNet salary: {net_salary}")


if __name__ == '__main__':
    calculate_net_salary()
