"""
Ejercicio 6:

Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de
ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que
obtenga una calificación mayor que a un mínimo dado en cualquiera de los
exámenes es aceptado; en caso contrario es rechazado. Reali ce un
Algoritmo, que lea el nombre y calificaciones del aspirante. Realice un
Algoritmo, que indique si es aceptado o rechazado. (Ejemplo mínimo = 90)
"""

# Minimum

MINIMUM = 90.0


def applicant_data(num_applicants: int) -> {}:

    applicant_status = {}

    for i in range(0, num_applicants):
        name = input(f"\nEnter the applicant {(i + 1)} name: ")
        exams = [float(input(f"Enter the grade of the exam {(j + 1)}: ")) for j in range(0, 2)]

        applicant_status[name] = exams

    return applicant_status


def is_accepted(applicants: dict) -> dict:

    accepted_applicants = {}

    for key, value in applicants.items():
        if max(value) >= MINIMUM:
            accepted_applicants[key] = value

    return accepted_applicants


def two_exams() -> None:

    # Getting the number of applicants

    applicants = int(input("Enter the number of applicants: "))

    # Getting the applicants data

    applicant_status = applicant_data(applicants)

    # Determine whether an applicant was accepted or rejected

    applicant_status = is_accepted(applicant_status)
    print(f"\nThe accepted applicants can be found on the next list: (Name: Grades)" +
          f"\n {applicant_status}")


if __name__ == '__main__':
    two_exams()
