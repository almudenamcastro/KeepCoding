def numeric_grade(grade):
    """
    input: letter grades (A, B, C...)
    returns: numberic grades
    """
    # letter values
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    numbers = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
    grade = grade.upper()
    
    # raise error: invalid letter
    if grade not in letters:
        raise ValueError("El valor {} no es correcto".format(grade))
    
    # find number value
    for i in range(len(letters)):
        if grade == letters[i]:
            return numbers[i]

            
def gpa(*values):
    
    # initialize the number grades vector
    numbervalues = []
    
    # convert letters into numbers
    for value in values:
        try:
            numbervalues.append(numeric_grade(value))
        except:
            print("El valor", value, "se ha excluido")
    
    # calculate average
    if len(numbervalues) == 0:
        raise ValueError ("No se han introducido notas válidas")
    return sum(numbervalues) / len(numbervalues)

def gpa2(*values):
    sum = 0
    len = 0
    
    for value in values:
        try:
            sum += numeric_grade(value)
            len += 1
        except:
            print("El valor", value, "se ha excluido")
    if len == 0:
        raise ValueError ("No se han introducido notas válidas")
    
    return sum / len


