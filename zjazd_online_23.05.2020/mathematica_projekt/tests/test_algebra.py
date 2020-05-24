from mathematica.algebra.matrices import add_matrices, sub_matrices

def test_add_matrices():
    m1 = [[1, 1], [2, 2]]
    m2 = [[2, 2], [3, 3]]
    assert add_matrices(m1,m2) == print([[3, 3], [5, 5]])

def test_sub_matrices():
    pass