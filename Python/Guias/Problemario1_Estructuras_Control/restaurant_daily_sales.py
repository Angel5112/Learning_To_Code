"""
Ejercicio 10:

El menú de un restaurante de comida rápida es:

Hamburguesa 250 Ptas.
Cerveza 100 Ptas.
Coca cola 125 Ptas.
Ensalada 200 Ptas.
Salchichas 275 Ptas.
Sopa 260 Ptas.
Pastel 300 Ptas.

Se desea un algoritmo que calcule las ventas totales al final del día, así como los
impuestos a pagar (12%). El algoritmo tendrá como entrada el número de cada uno e
los productos vendidos ese día.
"""

# Restaurant Menu

menu = {"hamburguesa": 250,
        "cerveza": 100,
        "coca_cola": 125,
        "ensalada": 200,
        "salchichas": 275,
        "sopa": 260,
        "pastel": 300}


def daily_sales() -> float:

    # Getting the number of sales made

    hamburguesa = int(input("Enter the number of Hamburguesas sold today: "))
    cerveza = int(input("Enter the number of Cerveza sold today: "))
    coca_cola = int(input("Enter the number of Coca Cola sold today: "))
    ensalada = int(input("Enter the number of Ensalada sold today: "))
    salchichas = int(input("Enter the number of Salchichas sold today: "))
    sopa = int(input("Enter the number of Sopa sold today: "))
    pastel = int(input("Enter the number of Pastel sold today: "))

    total = round((hamburguesa * menu["hamburguesa"]) +
                  (cerveza * menu["cerveza"]) +
                  (coca_cola * menu["coca_cola"]) +
                  (ensalada * menu["ensalada"]) +
                  (salchichas * menu["salchichas"]) +
                  (sopa * menu["sopa"]) +
                  (pastel * menu["pastel"]), 2)

    return total


def calculate_taxes(total: float) -> float:
    return total * 0.12


def restaurant_daily_sales() -> None:

    # Getting the total sales of today

    daily_total = daily_sales()

    # Getting taxes total (12%)

    taxes = calculate_taxes(daily_total)

    print(f"\nThe daily total consists of: " +
          f"\n Daily Total (No Taxes): {daily_total}" +
          f"\n Taxes (12%): {taxes}" +
          f"\n Daily Total: {daily_total - taxes}")


if __name__ == '__main__':
    restaurant_daily_sales()
