# Funciones para:
# 1. Detectar la presencia de UNA instancia del elemento dentro de una lista, en cualquier posición.
# 2. Detectar la presencia de N instancias dentro de una lista, en cualquier posición
# 3. Detectar la presencia de N elementos SEGUIDOS dentro de una lista.
# 4. Detectar la presencia de N elementos SEGUIDOS dentro de una matriz en vertical y horizontal.

vector1=["o", "x", "o", "x", "-", "-"]
vector2=["x", "x", "x", "x", "-", "-"]
vector3=["x", "x", "o", "o", "x", "-"]
vector4=["o", "x", "o", "x", "-", "-"]
vector5=["x", "o", "x", "x", "-", "-"]
vector6=["x", "o", "x", "-", "-", "-"]


def find_streak(list, char, n):
    # inicializo el contador de veces que he encontrado char
    # inicializo el indice del elemento actual
    i = 0
    count = 0

    # evito requests sin sentido
    if n <= 0:
        print("El parámetro n debe ser mayor que 0")
        return False 

    # mientras no termine la lista
    while i < len(list):
        # busco char, si lo encuento, actualizo el contador 
        if list[i] == char :
            count += 1
            # y compruebo si vale n, en cuyo caso devuelvo True
            if count == n:
                return True
        # si el elemento i es distinto de char, reseteo el contador
        else:
            count = 0

        # hago avanzar el índice
        i += 1

    # si llego al final del bucle y no he encontrado ningún streak, devuelvo False
    return False

matriz = [vector1, vector2, vector3, vector3, vector2, vector3]
matriz1 =[[1,2,3],[4,5,6],[7,8,9]] 

def find_streak_hor(matrix, char, n):
    # por cada fila de la matriz
    for j in range(len(matrix)):
        # cada vez que empiezo una nueva fila inicializo el contador y el índice i (horizontal)
        i = 0
        count = 0
        #mientras el índice no acabe la fila
        while i < len(matrix[j]):
            # si encuentro char, actualizo el contador 
            if matrix[j][i] == char :
                count += 1
                #y compruebo si vale n
                if count == n:
                    return True
            # si el elemento no es char, reseteo el contador
            else:
                count = 0
            # hago avanzar el índice horizontal
            i += 1

    # si llego al final del bucle y no he encontrado ningún streak, devuelvo False
    return False


def transpose(matrix):
    matrix_t=[]
    for i in range (len(matrix[0])):
        row_t=[]
        for column in matrix:
            row_t.append(column[i])
        matrix_t.append(row_t)
    return matrix_t


matriz=[[1,2],[3,4],[5,6]]