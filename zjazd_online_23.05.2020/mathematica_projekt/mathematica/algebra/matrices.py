def add_matrices(m1:list,m2:list):
    result = []
    # for i,row in enumerate(m1):
    #     n_row = []
    #     for j,col in enumerate(row):
    #         n_row.append(col + m2[i][j])
    #     result.append(n_row)
    # return print(result)
    for row_m1,row_m2 in zip(m1,m2):
        row = []
        for col_m1,col_m2 in zip(row_m1,row_m2):
            row.append(col_m1 + col_m2)
        result.append(row)
    return result



def sub_matrices(m1,m2):
    result = []
    for row_m1,row_m2 in zip(m1,m2):
        row = []
        for col1,col2 in zip(row_m1,row_m2):
            row.append(col1 - col2)
        result.append(row)
    return result

mat = [[1,1],[2,2]]
ma = [[4,4],[3,3]]
print(add_matrices(mat,ma))
print(sub_matrices(ma,mat))


