"""
Ejercicio 9:

Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula siguiente:

(Presion x Volumen) / (0.37 x (Temperatura + 460))
"""


def mass_formula(pressure: float, volume: float, temperature: float) -> float:
    return (pressure * volume) / (0.37 * (temperature + 460))


def mass_calculator() -> None:

    # Getting required data

    pressure = float(input("Enter the pressure: "))
    volume = float(input("Enter the volume: "))
    temperature = float(input("Enter the temperature: "))

    # Calculate mass

    mass = round(mass_formula(pressure, volume, temperature), 2)
    print(f"The amount of mass is: {mass}")


if __name__ == '__main__':
    mass_calculator()
