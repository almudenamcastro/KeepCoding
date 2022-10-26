from copy import deepcopy 

def process_element(matrix, i, j):

    values = [matrix[i][j]]
    move = [-1,1]

    for value in move: 

        k = i + value
        values.append(matrix[k][j])
        
        k = j + value
        values.append(matrix[i][k])
    
    values = [x for x in values if x is not None]
    
    return sum(values)/len(values)


def process_matrix(matrix):
    avg_matrix = deepcopy(matrix)
    aux_matrix = deepcopy(matrix)

    for fila in aux_matrix:
        fila.append(None)
    aux_matrix.append([None]*len(aux_matrix[0]))

    for i, row in enumerate(matrix): 
        for j in range(len(row)): 
            avg_matrix[i][j] = process_element(aux_matrix, i, j)

    return avg_matrix

test=[[1,2,3],[4,5,6],[7,8,9]]

process_matrix(test)
process_element(test, 2, 2)