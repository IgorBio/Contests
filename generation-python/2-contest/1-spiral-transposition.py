'''
Реализуйте функцию spiral_transposition(), которая принимает в качестве аргумента матрицу (двумерный список)
и возвращает одномерный список со значениями исходной матрицы, расположенными по спирали (начиная с верхнего левого угла).
'''

# def spiral_transposition(matrix):
#     result = []
#     for i in range(len(matrix) // 2 + len(matrix) % 2):
#         for j in range(i, len(matrix) - i):
#             result.append(matrix[i][j])
#         for j in range(i + 1, len(matrix) - i):
#             result.append(matrix[j][len(matrix) - i - 1])
#         for j in range(len(matrix) - i - 2, i - 1, -1):
#             result.append(matrix[len(matrix) - i - 1][j])
#         for j in range(len(matrix) - i - 2, i, -1):
#             result.append(matrix[j][i])
#     return result

def spiral_transposition(matrix):
    result = []
    left_col = 0
    right_col = len(matrix[0]) - 1
    top_row = 0
    bottom_row = len(matrix) - 1
    while left_col <= right_col and top_row <= bottom_row:
        for i in range(left_col, right_col + 1):
            result.append(matrix[top_row][i])
        top_row += 1
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_col])
        right_col -= 1
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                result.append(matrix[bottom_row][i])
        bottom_row -= 1
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                result.append(matrix[i][left_col])
        left_col += 1
    return result

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    print(spiral_transposition(matrix))

    matrix = [['a', 'b', 'c', 'd', 'e'],
              ['f', 'g', 'h', 'i', 'j'],
              ['k', 'l', 'm', 'n', 'o']]
    print(spiral_transposition(matrix))