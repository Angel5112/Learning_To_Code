"""
Ejercicio 2:

Un alumno desea saber cuál será su calificación final en la asignatura: Introducción a la informática. Dicha
calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
"""


def calculate_exams_grades(grade_exam1: float, grade_exam2: float, grade_exam3: float) -> float:
    grades_sum_total = grade_exam1 + grade_exam2 + grade_exam3
    return (grades_sum_total * 55) / 60


def calculate_final_grades(grade_final_exam: float, grade_final_project: float) -> float:
    final_grades_total = grade_final_exam + grade_final_project
    return (final_grades_total * 45) / 40


def grades_calculator() -> None:

    # Getting the grades of the three exams

    first_exam = float(input("Enter the grade of your 1st exam: "))
    second_exam = float(input("Enter the grade of your 2nd exam: "))
    third_exam = float(input("Enter the grade of your 3rd exam: "))

    # Getting the grades of the final exam and project

    final_exam = float(input("Enter the grade of your final exam: "))
    final_project = float(input("Enter the grade of your final project: "))

    # Calculate the percentage with the obtained grades

    exams_grades = calculate_exams_grades(first_exam, second_exam, third_exam)
    final_grades = calculate_final_grades(final_exam, final_project)

    # Obtain the total grade

    total_grade = (exams_grades + final_grades) / 5
    total_grade = round(total_grade, 2)
    print(f"The final grade of Introduccion a la Informatica is: {total_grade}")


if __name__ == '__main__':
    grades_calculator()
