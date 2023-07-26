"""
Ejercicio 3:

Un profesor desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de
estudiantes.
"""


def calculate_percentage(students_number: int, total_students: int) -> float:
    return (students_number * 100) / total_students


def calculate_student_percentage() -> None:

    # Getting the number of male and female students

    male_students = int(input("Enter the number of male students: "))
    female_students = int(input("Enter the number of female students: "))

    # Calculate the total of students

    total_students = male_students + female_students

    # Calculate the percentage for male and female students

    male_percentage = round(calculate_percentage(male_students, total_students), 2)
    female_percentage = round(calculate_percentage(female_students, total_students), 2)

    print(f"For {total_students} students, there is a percentage of {male_percentage} male students" +
          f" and a percentage of {female_percentage} female students!")


if __name__ == '__main__':
    calculate_student_percentage()
