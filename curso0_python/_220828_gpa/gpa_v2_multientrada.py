from _220828_gpa.gpa_v2_functions import numeric_grade

def multientrada(*values):
    for value in values:
        print (value*2)
        
def multientrada2(**pares_kv):
    print (pares_kv)
    for key, value in pares_kv.items():
        print (key, value)
    
def boletin(**asignaturas):
    notas=[]
    for nota in asignaturas.values():
        print(nota)
        try: 
            notas.append(numeric_grade(nota))
        except:
            print("El valor de la nota", nota, "se ha excluido")
    if len(notas)==0:
        print("No se han introducido notas válidas")
    return sum(notas)/len(notas)