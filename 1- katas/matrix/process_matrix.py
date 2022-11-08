def rook_neighbours(matrix, i, j):
    '''
    receives an element in a matrix (defined by its indexes i and j) 
    returns a list with the element and those around it, the rook neigbours (top, down, left, right)
    '''
    # create empty list and a vector to define the moves
    values = []
    move = [-1,1]

    # append matrix element 
    values.append(matrix[i][j])

    for value in move: 
        # make sure that neighbour index belongs to the matrix:
        if i + value in range(len(matrix)):  
            # append top down neightbours       
            values.append(matrix[i + value][j])     
        if j + value in range(len(matrix[i])):
            # append left right neightbours
            values.append(matrix[i][j + value])

    return values 

def array_depth(object):
    '''
    receives an object of any type
    returns its array_depth (0 if its an int or str, 1 a vector, 2 matrix etc.)
    '''
    depth = 0
    temp = object

    while type(temp) == list:
        depth += 1
        # in case the list is empty
        if temp == []:
            break
        else:
            temp = temp[0] 

    return depth

def is_num_matrix(matrix):
    '''
    receives a list of lists
    returns True if: 
    - the object is a list of list (array_depth = 2)
    - all the rows have the same lenght
    - all the elements in the matrix are a number
    ''' 
    # check matrix array_depth
    if array_depth(matrix) != 2:
        return False  
    
    # validate that all rows have the same lenght
    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            return False

        # validate that all elements are int or float number:
        for element in row:
            if type(element) != int and type(element) != float:
                return False
    
    #if the function gets to this point wihtout finding any issues, return True
    return True

def process_matrix(matrix, aggregation = lambda x: sum(x)/len(x), neighbours = rook_neighbours):
    '''
    receives a matrix 
    returns a new_matrix where all the elements have been calculated from the matrix element neighbours: 
    - neighbours is a function that returns the element neighbours in a list. rook_neighbours is the default value
    - aggregation: receives the element neighbours and returns their aggregated value, acording to some calculatiion. avg value is calculated by default.
    '''
    # VALIDATE INPUT MATRIX: 

    # if the matrix is empty, we return it without change. 
    if matrix == [[]] or matrix == []:
        return matrix

    # if it's not empty, we verify the input is a proper matrix: 
    if is_num_matrix(matrix) != True:
        raise TypeError('input must be matrix of numbers')

    # PROCESS MATRIX: 
    # create empty matrix to store the processed values
    new_matrix = []

    # this loop will go through all the elements in the matrix  
    for i, row in enumerate(matrix): 
        new_row = []
        for j in range(len(row)):
            # we use a function to return the element neighbours
            temp = neighbours(matrix,i,j)
            # include their aggregated value in the new matrix
            new_row.append(aggregation(temp))
        new_matrix.append(new_row)

    return new_matrix

