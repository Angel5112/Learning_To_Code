"""
Ejercicio 12:

 En un hospital existen tres áreas. El presupuesto anual del hospital se reparte conforme a la siguiente tabla:
Área                Porcentaje del presupuesto
Ginecología                    40%
Traumatología                  30%
Pediatría                      30%

Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestario.
"""

# Hospital Zones

GYNECOLOGY = 0.40
TRAUMATOLOGY = 0.30
PEDIATRICS = 0.30


def calculate_gynecology_budget(annual_budget: float) -> float:
    return annual_budget * GYNECOLOGY


def calculate_traumatology_budget(annual_budget: float) -> float:
    return annual_budget * TRAUMATOLOGY


def calculate_pediatrics_budget(annual_budget: float) -> float:
    return annual_budget * PEDIATRICS


def hospital_budget() -> None:

    # Getting the annual budget of the hospital

    total_budget = float(input("Enter the total annual budget for the hospital: "))

    # Calculate individual shares of the annual budget

    gynecology_budget = round(calculate_gynecology_budget(total_budget), 2)
    traumatology_budget = round(calculate_traumatology_budget(total_budget), 2)
    pediatrics_budget = round(calculate_pediatrics_budget(total_budget), 2)

    print(f"\nThe annual budget of the hospital ({total_budget}) is shared in the next 3 specialities:" +
          f"\n* Gynecology: {gynecology_budget}" +
          f"\n* Traumatology: {traumatology_budget}" +
          f"\n* Pediatrics: {pediatrics_budget}")


if __name__ == '__main__':
    hospital_budget()
