# def diagonal_sum(matrix):
#     total_diagonal_left=0
#     total_diagonal_right=0
#     for i,elem in enumerate(matrix):
#         for j,ele in enumerate(elem):
#             if i==j:
#                 total_diagonal_left+=ele
#             if i+j==len(matrix)-1:
#                 total_diagonal_right+=ele
             
#     return total_diagonal_left,total_diagonal_right


# best solution is by far

def diagonal_sum(matrix:list):
    total=0
    for i in range(len(matrix)):
        total+=matrix[i][i]
    for i in range(len(matrix)):
         total+=matrix[i][(len(matrix)-1)-i]
    return total


print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))