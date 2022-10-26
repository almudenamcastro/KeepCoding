def process_element(matrix, i, j):
    '''
    given a position from a matrix (defined by the indexes i, j) 
    it takes the elements around it and calculates the average value
    '''
    
    values = [matrix[i][j]]
    move = [-1,1]

    for value in move: 
        k = i + value
        if k in range(len(matrix)):
            values.append(matrix[k][j])
        k = j + value
        if k in range(len(matrix[0])):
            values.append(matrix[i][k])
    
    return sum(values)/len(values)

def process_matrix(matrix):
    '''
    calculates the average value for all elements in a matrix
    '''
    avg_matrix = []

    for i, row in enumerate(matrix): 
        avg_row = []
        for j in range(len(row)): 
            avg_row.append(process_element(matrix, i, j))
        avg_matrix.append(avg_row)

    return avg_matrix

test = [[1,2,3],[4,5,6],[7,8,9]]

process_matrix(test)
process_element(test, 2, 2)
