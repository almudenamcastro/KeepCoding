# these two lists contain the gpa numeric values values
letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
numbers = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]

# we could work with a dictionary
grades = {'A+': 4, 'A': 4, 'B': 3, 'C': 2.5, 'D': 2, 'E': 1, 'F': 0}

def numeric_grade(grade):
    """numeric_grade turns letter grades (A, B, C...) into numberic grades"""
    i = 0
    if grade not in letters:
        raise ValueError("El valor {} no es correcto".format(grade))
    while i < len(letters):
        if grade == letters[i]:
            return numbers[i]
        else:
            i += 1
            

def letter_grade(grade):
    """ letter_grade turns numeric grades into letters A, B, C..."""
    if grade > max(numbers) or grade < 0:
        raise ValueError ("Introduce un valor positivo menor o igual que {}".format(max(numbers)))
    for i in range(0, len(letters)):
        if grade == numbers[i] or grade > numbers[i+1]:
            return letters[i]
            
# gpa calculates the grades average
def gpa(values):
    numbervalues = []
    for value in values:
        try:
            numbervalues.append(numeric_grade(value))
        except:
            print("El valor", value, "se ha excluido")
    if len(numbervalues) == 0:
        raise ValueError ("No se han introducido notas válidas")
    numeric_average = sum(numbervalues) / len(numbervalues)
    return numeric_average, letter_grade(numeric_average)


# we ask for the grades
values = input("Introduce las notas separadas por comas: ")
values = values.upper().replace(" ", "").split(",")

# print average
print("La media es {nota[0]}, es decir: {nota[1]}".format(nota = gpa(values)))
