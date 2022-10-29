import pytest
from matrix.process_matrix import *

def approx_matrix(calculated, computed, rel=0.01):
    '''
    receives 2 matrix
    returns True if they are equal within certain tolerance
    '''
    # we only need to check every value if the matrices are not equal in the first place. 
    if calculated != computed: 
        # explore the matrix row by row
        for i in range(len(calculated)):
            # and if the rows are not equal
            if calculated[i] != pytest.approx(computed[i], rel):
                return False
    return True

matrices =[
    [[1,2,3],[4,5,6],[7,8,9]],
    [[-1.5,-2.5,-3.5],[-4.5,-5.5,-6.5],[-7.5,-8.5,-9.5]],
    [[1,2,3,4]],
    [[1]],
    []
]

matrices_avg = [
    [[2.33, 2.75, 3.67], [4.25, 5.0, 5.75], [6.33, 7.25, 7.67]], 
    [[-2.83, -3.25, -4.17], [-4.75,- 5.5, -6.25], [-6.83, -7.75, -8.17]], 
    [[1.5, 2, 3, 3.5]], 
    [[1]],
    []
]

matrices_sum = [
    [[7,11,11],[17,25,23],[19,29,23]],
    [[-8.5, -13.0, -12.5], [-19.0, -27.5, -25.0], [-20.5, -31.0, -24.5]],
    [[3,6,9,7]],
    [[1]],
    []
]

def test_process_matrix_avg():
    for i in range(len(matrices)):
        assert approx_matrix(process_matrix(matrices[i]), matrices_avg[i])

def test_process_matrix_sum():
    for i in range(len(matrices)):
        assert approx_matrix(process_matrix(matrices[i], sum), matrices_sum[i])

tests_errors = [
    1,
    "hello",
    [[1],[1,2]],
    [[[1],[1,2]]],
    [[1,2],[1,"a"]]
]

def test_errors():
    for test in tests_errors:
        with pytest.raises(TypeError):
            process_matrix(test)

if __name__ == "__main__":
    test_process_matrix_avg()
    test_process_matrix_sum()
    test_errors()
